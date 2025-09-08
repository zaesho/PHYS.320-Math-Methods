import numpy as np

# Question One
# Defining arbitrary base vectors

A_x = np.random.randint(0, 100)
A_y = np.random.randint(0, 100)
A = np.array([[A_x, A_y]])

B_x = np.random.randint(0, 100) # Components for matrix B
B_y = np.random.randint(0, 100)
B = np.array([[B_x, B_y]])

M_xx = np.random.randint(0, 100)
M_xy = np.random.randint(0, 100)
M_yx = np.random.randint(0, 100)
M_yy = np.random.randint(0, 100)
M = np.array([[M_xx, M_xy], [M_yx, M_yy]]) # Defining matrix M

# Lets now define the cross product of A and B before the matrix transformation.
ab_cross_product = np.cross(A, B)

print("A x B =", ab_cross_product)

# Lets apply the matrix transformation to A and B
A_transformed = A @ M
B_transformed = B @ M

# Now we can compute the cross product of the transformed vectors
ab_cross_product_transformed = np.cross(A_transformed, B_transformed)

print("A' x B' =", ab_cross_product_transformed)

#Now we need to show that the cross product of the transformed vectors is 
# actually equal the original cross product by a scaling factor det|M|
det_M = np.linalg.det(M)
print("det|M| =", det_M)
print("A' x B' =", ab_cross_product * det_M)
print("A' x B' = (A x B) * det|M|", int(ab_cross_product * det_M) == int(ab_cross_product_transformed))

# Question Two

from sympy import symbols, Matrix

a, b, c, d, e, f, g , h = symbols('a b c d e f g h') # Defining symbolic variables

N = Matrix([[a,h,g],[h,b,f],[g,f,c]])
det_N = N.det()

print("det|N| =", det_N)

# Q2 (B)

B = Matrix([[1, 0, 2, 3], [0, 1, -2, 1], [3, -3, 4, -2],[-2, 1, -2 , 1]])
print("det|B| =", B.det())\

#Q3 (C)


C = Matrix([[g*c, g*e, a+g*e, g*b+g*e], [0, b, b, b], [c, e, e, b+3],[a, b, b+f , b+d]])
print("det|C| =", C.det())