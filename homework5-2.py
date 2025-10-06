"""
Homework 5

Problem 2: Using Python to verify the vector identity:
"""

import numpy as np
import sympy as sp
from sympy import symbols, diff, simplify, expand

# Define symbolic variables
x, y, z = symbols('x y z', real=True)

print("Homework 5 - Problem 2")
print("=" * 50)
print("Verifying the vector identity:")
print()

# Define the vector fields from problem 1
print("Given vector fields:")
print("v = (xhat+yhat+zhat)/(x²+y²+z²) ")
print("r = x x̂ + y ŷ + z ẑ")
print()

# Define v as a scalar field multiplied by position vector
v_scalar = (x + y + z) / (x**2 + y**2 + z**2)
v = [v_scalar * x, v_scalar * y, v_scalar * z]

# Define r vector
r = [x, y, z]

print("Vector components:")
print(f"v = [{v[0]}, {v[1]}, {v[2]}]")
print(f"r = [{r[0]}, {r[1]}, {r[2]}]")
print()

# Calculate cross product v × r
def cross_product(a, b):
    """Calculate cross product of two 3D vectors"""
    return [
        a[1]*b[2] - a[2]*b[1],  # i component
        a[2]*b[0] - a[0]*b[2],  # j component
        a[0]*b[1] - a[1]*b[0]   # k component
    ]

v_cross_r = cross_product(v, r)
for i, component in enumerate(['i', 'j', 'k']):
    print(f"({component}) component: {simplify(v_cross_r[i])}")
print()

# Calculate divergence of (v × r)
def divergence(vector_field):
    """Calculate divergence of a vector field"""
    return diff(vector_field[0], x) + diff(vector_field[1], y) + diff(vector_field[2], z)

div_v_cross_r = divergence(v_cross_r)

print(f"∇ · (v × r) = {simplify(div_v_cross_r)}")
print()

# Calculate curl of v
def curl(vector_field):
    """Calculate curl of a vector field"""
    return [
        diff(vector_field[2], y) - diff(vector_field[1], z),  # i component
        diff(vector_field[0], z) - diff(vector_field[2], x),  # j component
        diff(vector_field[1], x) - diff(vector_field[0], y)   # k component
    ]

curl_v = curl(v)
for i, component in enumerate(['i', 'j', 'k']):
    print(f"({component}) component: {simplify(curl_v[i])}")
print()

# Calculate curl of r
curl_r = curl(r)
for i, component in enumerate(['i', 'j', 'k']):
    print(f"({component}) component: {simplify(curl_r[i])}")
print()

# Calculate dot products
def dot_product(a, b):
    """Calculate dot product"""
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

r_dot_curl_v = dot_product(r, curl_v)
v_dot_curl_r = dot_product(v, curl_r)


print(f"r · (∇ x v) = {simplify(r_dot_curl_v)}")
print()


print(f"v · (∇ x r) = {simplify(v_dot_curl_r)}")
print()

# Calculate the right-hand side of the identity
rhs = r_dot_curl_v - v_dot_curl_r

print(f"RHS = {simplify(rhs)}")
print()

# Verify the identity

print("=" * 30)
print(f"LHS = ∇ · (v x r) = {simplify(div_v_cross_r)}")
print(f"RHS = r · (∇ x v) - v · (∇ x r) = {simplify(rhs)}")
print()

# Check if they are equal
difference = simplify(div_v_cross_r - rhs)
print(f"Difference (LHS - RHS) = {difference}")

if difference == 0:
    print("The vector identity holds!")
else:
    print("Identity does not hold")
    