# We'll use SymPy to verify four 3D vector-calculus identities symbolically.
import sympy as sp

# Coordinates
x, y, z = sp.symbols('x y z', real=True)

# Scalar fields
phi = sp.Function('phi')(x, y, z)
psi = sp.Function('psi')(x, y, z)

# Vector fields a(x,y,z), b(x,y,z)
ax = sp.Function('a_x')(x, y, z)
ay = sp.Function('a_y')(x, y, z)
az = sp.Function('a_z')(x, y, z)
bx = sp.Function('b_x')(x, y, z)
by = sp.Function('b_y')(x, y, z)
bz = sp.Function('b_z')(x, y, z)

a = sp.Matrix([ax, ay, az])
b = sp.Matrix([bx, by, bz])

# Differential operators
def grad(s):
    return sp.Matrix([sp.diff(s, x), sp.diff(s, y), sp.diff(s, z)])

def div(v):
    return sp.diff(v[0], x) + sp.diff(v[1], y) + sp.diff(v[2], z)

def curl(v):
    return sp.Matrix([
        sp.diff(v[2], y) - sp.diff(v[1], z),
        sp.diff(v[0], z) - sp.diff(v[2], x),
        sp.diff(v[1], x) - sp.diff(v[0], y)
    ])

def vec_equal(u, v):
    """Component-wise equality test for vectors."""
    diff = sp.simplify(u - v)
    return all(sp.simplify(comp) == 0 for comp in diff)

def scalar_equal(s1, s2):
    return sp.simplify(s1 - s2) == 0

# Identity 1:
lhs1 = grad(phi*psi)
rhs1 = phi*grad(psi) + psi*grad(phi)
id1_ok = vec_equal(lhs1, rhs1)

# Identity 2: 
lhs2 = div(phi*a)
rhs2 = phi*div(a) + grad(phi).dot(a)
id2_ok = scalar_equal(lhs2, rhs2)

# Identity 3:
lhs3 = div(a.cross(b))
rhs3 = b.dot(curl(a)) - a.dot(curl(b))
id3_ok = scalar_equal(lhs3, rhs3)

# Identity 4: 
lhs4 = curl(phi*a)
rhs4 = grad(phi).cross(a) + phi*curl(a)
id4_ok = vec_equal(lhs4, rhs4)

results = {
    "Identity 1 Holds?": id1_ok,
    "Identity 2 Holds?": id2_ok,
    "Identity 3 Holds?": id3_ok,
    "Identity 4 Holds?": id4_ok,
}

print(results)
