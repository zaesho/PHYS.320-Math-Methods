import sympy as sp

x, y, z = sp.symbols('x y z')

Ax = x**2 * y
Ay = -2*x*z
Az = 2*y*z

def curl(F):
    Fx, Fy, Fz = F
    Cx = sp.diff(Fz, y) - sp.diff(Fy, z)
    Cy = sp.diff(Fx, z) - sp.diff(Fz, x)
    Cz = sp.diff(Fy, x) - sp.diff(Fx, y)
    return (sp.simplify(Cx), sp.simplify(Cy), sp.simplify(Cz))

def div(F):
    Fx, Fy, Fz = F
    return sp.diff(Fx, x) + sp.diff(Fy, y) + sp.diff(Fz, z)

def laplacian(F):
    Fx, Fy, Fz = F
    def scalar_laplacian(f):
        return sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
    return (scalar_laplacian(Fx), scalar_laplacian(Fy), scalar_laplacian(Fz))

A = (Ax, Ay, Az)

curlA = curl(A)
curlcurlA = curl(curlA)

grad_divA = (sp.diff(div(A), x), sp.diff(div(A), y), sp.diff(div(A), z))
lapA = laplacian(A)
identity_rhs = (sp.simplify(grad_divA[0] - lapA[0]),
                sp.simplify(grad_divA[1] - lapA[1]),
                sp.simplify(grad_divA[2] - lapA[2]))

print(curlA, curlcurlA, grad_divA, lapA, identity_rhs)
