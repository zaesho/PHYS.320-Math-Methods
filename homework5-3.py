
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
psi = z*x**2/(x**2 + y**2 + z**2)

lap_sympy = sp.diff(psi, x, 2) + sp.diff(psi, y, 2) + sp.diff(psi, z, 2)
lap_simplified = sp.simplify(lap_sympy)

# Our result
lap_manual = 2*z*(y**2 + z**2 - 4*x**2)/(x**2 + y**2 + z**2)**2

print("SymPy result):", lap_simplified)
print("Manual:", sp.simplify(lap_manual))
print("Difference simplifies to:", sp.simplify(lap_simplified - lap_manual))