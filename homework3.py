import numpy as np

# Problem 1: Matrix Inversion
print("Problem 1: Matrix Inversion")
print("=" * 40)

# Given matrix A
A = np.array([[1, 3, -1],
              [3, 4, -2],
              [-1, -2, 2]], dtype=int)

print("Original matrix A:")
print(A)
print()

# Part C: Use Python to reproduce row operations to find the inverse
print("Part C: Finding inverse through row operations")
print("-" * 45)

# Create augmented matrix [A|I]
I = np.eye(3)
augmented = np.hstack([A, I])
print("Augmented matrix [A|I]:")
print(augmented)
print()

# Step-by-step row operations to get to reduced row echelon form
print("Step-by-step row operations:")

# Step 1: R2 = R2 - 3*R1 (eliminate below first pivot)
print("Step 1: R2 = R2 - 3*R1")
augmented[1] = augmented[1] - 3 * augmented[0]
print(augmented)
print()

# Step 2: R3 = R3 + R1 ( eliminate below first pivot)
print("Step 2: R3 = R3 + R1")
augmented[2] = augmented[2] + augmented[0]
print(augmented)
print()

# Step 3: R2 = R2 / (-5) (make second pivot = 1)
print("Step 3: R2 = R2 / (-5)")
augmented[1] = augmented[1] / (-5)
print(augmented)
print()

# Step 4: R3 = R3 - R2 (eliminate below second pivot)
print("Step 4: R3 = R3 - R2")
augmented[2] = augmented[2] - augmented[1]
print(augmented)
print()

# Step 5: R3 = R3 / (6/5) (make third pivot = 1)
print("Step 5: R3 = R3 / (6/5)")
augmented[2] = augmented[2] / (6/5)
print(augmented)
print()

# Now work backwards (back substitution)
# Step 6: R2 = R2 + (1/5)*R3 (eliminate above third pivot)
print("Step 6: R2 = R2 + (1/5)*R3")
augmented[1] = augmented[1] + (1/5) * augmented[2]
print(augmented)
print()

# Step 7: R1 = R1 + R3 (eliminate above third pivot)
print("Step 7: R1 = R1 + R3")
augmented[0] = augmented[0] + (1) * augmented[2]
print(augmented)
print()

# Step 8: R1 = R1 - 3*R2 (eliminate above second pivot)
print("Step 8: R1 = R1 - 3*R2")
augmented[0] = augmented[0] - 3 * augmented[1]
print(augmented)
print()

# Extract the inverse matrix from the right side of augmented matrix
A_inverse_manual = augmented[:, 3:6]
print("Inverse matrix A^(-1) from manual row operations:")
print(A_inverse_manual)
print()

# Part D: Confirm result using numpy.linalg.inv()
print("Part D: Confirmation using numpy.linalg.inv()")
print("-" * 45)

A_inverse_numpy = np.linalg.inv(A)
print("Inverse matrix using numpy.linalg.inv():")
print(A_inverse_numpy)
print()

# Verify the results are the same (within numerical precision)
print("Verification:")
print("Difference between manual and numpy results:")
difference = np.abs(A_inverse_manual - A_inverse_numpy)
print(difference)
print("Maximum difference:", np.max(difference))
print("Show if theyre the same disregarding FPP", np.allclose(A_inverse_manual, A_inverse_numpy))
print()

# Verify that A * A^(-1) = I
print("Verification that A * A^(-1) = I:")
product_manual = np.dot(A, A_inverse_manual)
product_numpy = np.dot(A, A_inverse_numpy)

print("A * A^(-1) (using manual inverse):")
print(product_manual)
print()

print("A * A^(-1) (using numpy inverse):")
print(product_numpy)
print()

print("Is the product close to identity matrix?")
print("Manual method:", np.allclose(product_manual, np.eye(3)))
print("Numpy method:", np.allclose(product_numpy, np.eye(3)))
