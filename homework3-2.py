import sympy as sp

# Question 2 Part D
# Solve λ³ - 7λ² + 6 = 0
lam = sp.Symbol('lambda')
cubic_eq = lam**3 - 7*lam**2 + 6
roots = sp.solve(cubic_eq, lam)

print("Roots of λ³ - 7λ² + 6 = 0:")
for i, root in enumerate(roots):
    print(f"λ{i+1} = {root}")

print("\n" + "="*50)

# Given matrix A
A = sp.Matrix([[1, 3, -1],
               [3, 4, -2],
               [-1, -2, 2]])

# Find eigenvalues and eigenvectors
eigenvals = A.eigenvals()
eigenvects = A.eigenvects()

print("Matrix A:")
sp.pprint(A)
print("\nEigenvalues:")
for eigenval, multiplicity in eigenvals.items():
    print(f"λ = {eigenval} (multiplicity: {multiplicity})")

print("\nEigenvalues and Eigenvectors:")
for i, (eigenval, multiplicity, eigenvecs) in enumerate(eigenvects):
    print(f"λ{i+1} = {eigenval}")
    for j, vec in enumerate(eigenvecs):
        print(f"v{i+1}_{j+1} = {vec}")
    print()