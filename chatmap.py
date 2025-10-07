import pandas as pd

# Row and column labels
rows = ["LA","RH","TD","RC","TR","ML","KN","PB","JE","UR","LW","CM","NG"]
cols = ["WI","NN","CO","EM","AY","SY","KY","CH","TH","HI","RY","KA","HR"]

# 0/1 adjacency matrix (from your candidate table)
A = [
    [0 ,0 ,1,1,1,1,1,1,1,0,0,1,0 ],
    [0 ,0 ,1,0,1,1,0,0,1,1,1,1,1 ],
    [1 ,0 ,0,0,0,0,1,0,0,0,1,0,1 ],
    [1 ,0 ,0,1,0,1,1,1,0,0,0,0,1 ],
    [0 ,1 ,0,1,1,1,0,0,1,1,1,1,1 ],
    [0 ,1 ,0,1,1,1,0,1,1,0,0,1,1 ],
    [1 ,1 ,1,1,1,1,0,0,0,1,0,1,0 ],
    [1 ,0 ,1,1,0,0,1,1,1,0,0,1,1 ],
    [0 ,1 ,1,0,1,1,0,0,1,1,1,1,0 ],
    [1 ,0 ,1,1,1,1,1,0,1,1,0,1,1 ],
    [0 ,0 ,0,1,1,1,1,1,0,0,1,1,1 ],
    [1 ,0 ,1,1,1,1,1,1,1,1,0,1,1 ],
    [1 ,1 ,0,1,1,1,1,1,1,1,0,1,0 ],
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

print(permanent_ryser(A))