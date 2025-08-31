import numpy as np

# Problem 1
# Defining base vectors with arbitrary components:
# Having the components be randomly assigned as integers to avoid floating point precision errors.

a_1 = np.random.randint(0, 100) # Components for vector a
a_2 = np.random.randint(0, 100)
a_3 = np.random.randint(0, 100)

b_1 = np.random.randint(0, 100) # Components for vector b
b_2 = np.random.randint(0, 100)
b_3 = np.random.randint(0, 100)

c_1 = np.random.randint(0, 100) # Components for vector c
c_2 = np.random.randint(0, 100)
c_3 = np.random.randint(0, 100)

a = np.array([a_1, a_2, a_3])
b = np.array([b_1, b_2, b_3])
c = np.array([c_1, c_2, c_3])

# goal is to evaluate if the expressions on each side of the equations are equal 
# Eqn A: c dot ( a cross b ) = ( b cross a ) dot c

eqna_lhs = np.dot(c, np.cross(a, b))
eqna_rhs = np.dot(np.cross(b, a), c)

print("vec_a:", a)
print("vec_b:", b)
print("vec_c:", c)

print("Does Eqn A hold?",eqna_lhs,"==",eqna_rhs," ",eqna_lhs == eqna_rhs)

# Eqn b: a cross (b cross c) = (a cross b) dot c
eqnb_lhs = np.cross(a, np.cross(b, c))
eqnb_rhs = np.dot(np.cross(a, b), c)

print("Does Eqn B hold?",eqnb_lhs,"==",eqnb_rhs," ",eqnb_lhs == eqnb_rhs)

#Eqn c: a cross (b cross c) = (a dot c)b - (a dot b)c
eqnc_lhs = np.cross(a, np.cross(b, c))
eqnc_rhs = (np.dot(a, c) * b) - (np.dot(a, b) * c)

print("Does Eqn C hold?",eqnc_lhs,"==",eqnc_rhs," ",eqnc_lhs == eqnc_rhs)

# Eqn d: If d = lambda*a + mu*b then (a cross b) dot d = 0
# Since the expression is being dotted by d, the value of lambda and mu do not matter
# since they will become scalar multiples, thus, we can simplify this expression 
# to just the equation (a cross b ) dot (a + b) = 0
eqnd_lhs = np.dot(np.cross(a, b), (a + b))
eqnd_rhs = 0

print("Does Eqn D hold?",eqnd_lhs,"==",eqnd_rhs," ",eqnd_lhs == eqnd_rhs)

# Eqn e: (a cross b) cross (c cross b) = b*(b dot (c cross a))
eqne_lhs = np.cross(np.cross(a, b), np.cross(c, b))
eqne_rhs = np.dot(b, np.cross(c, a)) * b

print("Does Eqn E hold?",eqne_lhs,"==",eqne_rhs," ",eqne_lhs == eqne_rhs)

# Eqn f: (a cross b) dot (c cross d) = (a dot c)(b dot d) - (a dot d)(b dot c)
# Here well define an arbitrary d vector

d_1 = np.random.randint(0, 100) # Components for vector d
d_2 = np.random.randint(0, 100)
d_3 = np.random.randint(0, 100)

d = np.array([d_1, d_2, d_3])

eqnf_lhs = np.dot(np.cross(a, b), np.cross(c, d))
eqnf_rhs = (np.dot(a, c) * np.dot(b, d)) - (np.dot(a, d) * np.dot(b, c))

print("Does Eqn F hold?",eqnf_lhs,"==",eqnf_rhs," ",eqnf_lhs == eqnf_rhs)
