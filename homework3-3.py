import sympy as sp

# Define the inertia matrix from the problem using SymPy
I = sp.Matrix([[6.425,  -67.5,   -30  ],
               [-67.5,    15.18,  -30  ],
               [-30, -11.25, 16.25]])

print("Inertia Matrix I:")
sp.pprint(I)
print()

# Find eigenvalues and eigenvectors using SymPy
eigenvals_dict = I.eigenvals()
eigenvals = list(eigenvals_dict.keys())
eigenvects = I.eigenvects()

print("Eigenvalues (Principal Moments of Inertia):")
for i, val in enumerate(eigenvals):
    print(f"λ_{i+1} = {val}")
    # Check if the eigenvalue is real
    if val.is_real:
        print(f"     = {float(val):.6f} gm⋅cm²")
    else:
        print(f"     = {complex(val)} (complex)")
print()

print("Eigenvectors (Principal Axes):")
for i, (eigenval, multiplicity, eigenvect_list) in enumerate(eigenvects):
    print(f"For λ_{i+1} = {eigenval}:")
    for j, eigenvect in enumerate(eigenvect_list):
        print(f"  v_{i+1}_{j+1} = {eigenvect}")
        # Convert to float for numerical display if real
        try:
            float_vect = [float(val) for val in eigenvect]
            print(f"  v_{i+1}_{j+1} (numerical) = [{float_vect[0]:.6f}, {float_vect[1]:.6f}, {float_vect[2]:.6f}]")
        except:
            print(f"  v_{i+1}_{j+1} (complex) = {[complex(val) for val in eigenvect]}")
print()

# Convert eigenvalues to float for analysis (only real ones)
eigenvals_real = [val for val in eigenvals if val.is_real]
eigenvals_float = [float(val) for val in eigenvals_real]
eigenvals_float.sort()

print("Analysis:")
if len(eigenvals_float) >= 2:
    print(f"Smallest eigenvalue (easiest to spin around): λ_min = {eigenvals_float[0]:.6f} gm⋅cm²")
    print(f"Largest eigenvalue (hardest to spin around): λ_max = {eigenvals_float[-1]:.6f} gm⋅cm²")
else:
    print("Note: Some eigenvalues are complex. This suggests the matrix may not be properly symmetric.")
    print("Let's check the matrix symmetry...")
    print("I - I.T =")
    sp.pprint(I - I.T)
print()

