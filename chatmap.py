import pandas as pd
import random

# Row and column labels
rows = ["TR","ML","KN","PB","JE","UR","LW","CM","NG"]
cols = ["WI","NN","EM","AY","SY","TH","HI","KA","HR"]

# 0/1 adjacency matrix (from your candidate table)
A = [
    [0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ],
    [0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ],
    [0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ],
    [1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ],
    [0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ],
    [0 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ],
]

n = len(rows)

# Build adjacency as neighbor lists
neighbors = {i: [j for j in range(n) if A[i][j]==1] for i in range(n)}

# Order by degree to prune search faster
row_order = sorted(range(n), key=lambda i: len(neighbors[i]))

cap = 5000  # cap total matchings to avoid combinatorial explosion
solutions = []
used_cols = [False]*n

def dfs(k, partial):
    """Recursive backtracking to find one-to-one matchings."""
    if len(solutions) >= cap:
        return
    if k == n:
        solutions.append(partial.copy())
        return
    r = row_order[k]
    for c in neighbors[r]:
        if not used_cols[c]:
            used_cols[c] = True
            partial.append((r,c))
            dfs(k+1, partial)
            partial.pop()
            used_cols[c] = False

dfs(0, [])

def mapping_from_solution(sol):
    """Return a dict mapping row name -> col name."""
    return {rows[r]: cols[c] for r,c in sol}

# Convert all solutions into a list of dicts
records = []
for idx, sol in enumerate(solutions, start=1):
    mapping = mapping_from_solution(sol)
    mapping["Solution #"] = idx
    records.append(mapping)

df = pd.DataFrame(records)
df = df[["Solution #"] + rows]  # reorder columns

# Save to CSV
output_path = "matchings.csv"
df.to_csv(output_path, index=False)

print(f"✅ Saved {len(df)} one-to-one matchings to '{output_path}' (capped at {cap}).")
print(df.head(10).to_string(index=False))


def permanent_ryser(A):
    """
    Exact permanent via Ryser's formula using Gray-code iteration.
    A must be an n x n list-of-lists (numbers).
    Complexity: O(n * 2^n), fine for n <= ~20 with 0/1 matrices.
    """
    n = len(A)
    row_sums = [0]*n    
    per_sum = 0
    last_mask = 0
    for k in range(1, 1 << n):
        g = k ^ (k >> 1)                  # Gray code
        diff = g ^ last_mask              # bit that changed
        j = (diff.bit_length() - 1)       # column index toggled
        if (g >> j) & 1:                  # add column j
            for i in range(n):
                row_sums[i] += A[i][j]
        else:                             # remove column j
            for i in range(n):
                row_sums[i] -= A[i][j]
        # product of row sums
        prod = 1
        for s in row_sums:
            prod *= s
            if prod == 0:
                break
        per_sum += (-1 if (g.bit_count() % 2) else 1) * prod
        last_mask = g
    return (-1)**n * per_sum

import copy

def submatrix_rm_rc(A, ri, cj):
    """Return matrix with row ri and column cj removed."""
    return [[A[r][c] for c in range(len(A)) if c != cj]
            for r in range(len(A)) if r != ri]

# 1) Total perfect matchings
total_per = permanent_ryser(A)
print(f"Total perfect matchings (permanent): {total_per}")

if total_per == 0:
    raise RuntimeError("No perfect matchings exist; cannot rank contributions.")

# 2) Edge contributions (how many perfect matchings use this edge)
edge_contrib = []
for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            cnt = permanent_ryser(submatrix_rm_rc(A, i, j))
            edge_contrib.append({
                "Row_i": i, "Row": rows[i],
                "Col_j": j, "Col": cols[j],
                "EdgeContribution": cnt,
                "Probability_pij": cnt / total_per,     # optional: how often it appears
                "ForcedEdge": (cnt == total_per),       # True if removing kills all matchings
            })

edge_df = pd.DataFrame(edge_contrib).sort_values("EdgeContribution", ascending=False).reset_index(drop=True)
edge_df.to_csv("edge_contribution.csv", index=False)
print("\nTop 15 edges by contribution (higher = adds more options):\n")
print(edge_df.head(15).to_string(index=False))
print("\n✅ Saved full list to 'edge_contribution.csv'.")

# 3) Row/col aggregate “fat” (sum of contributions touching a row/col)
row_fat = (edge_df.groupby("Row", as_index=False)["EdgeContribution"].sum()
           .sort_values("EdgeContribution", ascending=False).reset_index(drop=True))
col_fat = (edge_df.groupby("Col", as_index=False)["EdgeContribution"].sum()
           .sort_values("EdgeContribution", ascending=False).reset_index(drop=True))
row_fat.to_csv("row_fat.csv", index=False)
col_fat.to_csv("col_fat.csv", index=False)
print("\nRows adding the most options (sum of edge contributions):")
print(row_fat.to_string(index=False))
print("\nCols adding the most options (sum of edge contributions):")
print(col_fat.to_string(index=False))
print("\n✅ Wrote 'row_fat.csv' and 'col_fat.csv'.")

# 4) Greedy trimming
def greedy_trim(A, target_min_per=1000, max_removals=50, forbid_forced=True, verbose=True):
    """
    Iteratively remove the single edge with the largest contribution,
    as long as per(A) stays >= target_min_per (and optionally we never remove forced edges).
    Writes intermediate choices; returns pruned matrix and log.
    """
    A_cur = copy.deepcopy(A)
    log = []
    per_cur = permanent_ryser(A_cur)
    step = 0

    while step < max_removals and per_cur >= target_min_per:
        # recompute contributions on current A
        contribs = []
        for i in range(n):
            for j in range(n):
                if A_cur[i][j] == 1:
                    cnt = permanent_ryser(submatrix_rm_rc(A_cur, i, j))
                    if forbid_forced and cnt == per_cur:
                        # this edge is currently forced—skip if user wants to keep feasibility
                        continue
                    contribs.append((cnt, i, j))
        if not contribs:
            if verbose:
                print("No removable edges left under current constraints.")
            break
        contribs.sort(reverse=True)  # largest contribution first
        cnt, i_best, j_best = contribs[0]

        # simulate removal
        A_next = copy.deepcopy(A_cur)
        A_next[i_best][j_best] = 0
        per_next = per_cur - cnt  # exact update law when removing a single edge

        if per_next <= 0:
            if verbose:
                print(f"Skipping removal ({rows[i_best]}->{cols[j_best]}): would eliminate all matchings.")
            # Try next best contribution
            # Remove candidate from the list and try the next; if exhausted, stop
            removed = False
            for cnt2, i2, j2 in contribs[1:]:
                A_try = copy.deepcopy(A_cur)
                A_try[i2][j2] = 0
                per_try = per_cur - cnt2
                if per_try > 0 and per_try >= target_min_per:
                    A_next = A_try
                    per_next = per_try
                    i_best, j_best, cnt = i2, j2, cnt2
                    removed = True
                    break
            if not removed:
                if verbose:
                    print("No safe removal meets the target_min_per constraint.")
                break

        # commit removal
        A_cur = A_next
        step += 1
        log.append({
            "step": step,
            "removed_row": rows[i_best],
            "removed_col": cols[j_best],
            "edge_contribution": cnt,
            "per_before": per_cur,
            "per_after": per_next,
        })
        per_cur = per_next
        if verbose:
            print(f"[{step}] Remove {rows[i_best]}->{cols[j_best]} | contrib={cnt} | per: {log[-1]['per_before']} → {per_cur}")

        # stop if we already dropped below target (guard; should not happen due to checks)
        if per_cur < target_min_per:
            if verbose:
                print("Reached below target_min_per; stopping.")
            break

    return A_cur, pd.DataFrame(log)

# Example usage:
# Keep at least 10,000 perfect matchings, remove up to 40 edges.
A_pruned, trim_log = greedy_trim(A, target_min_per=10000, max_removals=40, forbid_forced=True, verbose=True)
trim_log.to_csv("trim_log.csv", index=False)

# Save the pruned matrix for inspection
pd.DataFrame(A_pruned, index=rows, columns=cols).to_csv("A_pruned.csv")
print("\n✅ Greedy trimming complete. Wrote 'trim_log.csv' and 'A_pruned.csv'.")
print(trim_log.head(10).to_string(index=False))


print(permanent_ryser(A))

def submatrix_by_index(A, row_idx, col_idx):
    return [[A[r][c] for c in col_idx] for r in row_idx]

def edge_shapley_monte_carlo(A, rows, cols, samples_per_edge=1000, rng=None):
    """
    Monte Carlo, row/col–agnostic 'fatness' score for each allowed edge (i,j).
    For each sample:
      - choose k in [1..n] uniformly,
      - choose k-1 other rows (plus i) and k-1 other cols (plus j),
      - score = (# matchings that include (i,j)) / (# total matchings) on that kxk subproblem.
    Returns a DataFrame with columns: Row, Col, Score_MC, UsedSamples.
    """
    if rng is None:
        rng = random.Random(0)

    n = len(A)
    # Precompute index arrays for speed
    all_rows = list(range(n))
    all_cols = list(range(n))

    results = []
    for i in range(n):
        for j in range(n):
            if A[i][j] != 1:
                continue

            score_sum = 0.0
            used = 0

            for _ in range(samples_per_edge):
                # pick k uniformly from 1..n
                k = rng.randint(1, n)

                # if k == 1, the subproblem is just the single edge (i,j)
                if k == 1:
                    per_full = A[i][j]
                    if per_full == 1:
                        # removing the only row/col leaves 0x0 with permanent 1 by convention
                        cnt_with_edge = 1  # exactly one matching using (i,j)
                        score_sum += 1.0
                        used += 1
                    # if per_full == 0, nothing to add (edge absent)
                    continue

                # choose k-1 other rows and cols uniformly at random
                other_rows = [r for r in all_rows if r != i]
                other_cols = [c for c in all_cols if c != j]
                S_rows = [i] + rng.sample(other_rows, k-1)
                T_cols = [j] + rng.sample(other_cols, k-1)

                # form kxk submatrix
                subA = submatrix_by_index(A, S_rows, T_cols)

                # find local indices of (i,j)
                i_loc = S_rows.index(i)
                j_loc = T_cols.index(j)

                # total matchings in the subproblem
                per_full = permanent_ryser(subA)
                if per_full == 0:
                    continue  # no matchings in this sample; skip

                # matchings that USE (i,j) in this subproblem
                # equals permanent of (k-1)x(k-1) with row i_loc and col j_loc removed
                subA_rm = [row[:j_loc] + row[j_loc+1:] for idx, row in enumerate(subA) if idx != i_loc]
                cnt_with_edge = permanent_ryser(subA_rm)

                score_sum += (cnt_with_edge / per_full)
                used += 1

            score = (score_sum / used) if used > 0 else 0.0
            results.append({
                "Row": rows[i],
                "Col": cols[j],
                "Score_MC": score,
                "UsedSamples": used
            })

    df_mc = pd.DataFrame(results).sort_values("Score_MC", ascending=False).reset_index(drop=True)
    return df_mc

# --- Run it ---
df_shapley = edge_shapley_monte_carlo(A, rows, cols, samples_per_edge=2000, rng=random.Random(42))
df_shapley.to_csv("edge_shapley_mc.csv", index=False)
print("✅ Wrote unbiased row/col–agnostic scores to 'edge_shapley_mc.csv'. Top 15:\n")
print(df_shapley.head(15).to_string(index=False))