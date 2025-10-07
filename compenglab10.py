import numpy as np


###Question 4

#Calculated value of pi
picalc = 2*np.arccos(0)

print(picalc)

#Np.pi value

nppi = np.pi

print(nppi)

#Difference

diff = picalc - nppi

print("="*50)
print("Question 4")

print(diff)

###Question 5


print("="*50)
print("Question 5")
print(np.exp(1)-np.e)


###Question 6
x = 0
m = 2.00
n = 2.00
while n > 0:
    n = m ** x
    x = x -1.00

x_nu = x + 2

print("="*50)
print("Question 6")
print("Largest x",x_nu, "Smallest number", 2**x_nu)

###Question 7
x = 2
m = 2.00
try:
    while True:
        n = m ** x
        if n == float('inf'):  
            break
        x = x + 1.00
except OverflowError:
    pass  

x_nu = x - 1  

print("="*50)
print("Question 7")
print("Biggest x", x_nu, "Biggest number", 2**x_nu)

###Question 8

x = 0
m = 2.00
n = 2.00
while n > 1:
    n = 1 + m ** x
    x = x -1.00

x_nu = x + 2
print("="*50)
print("Question 8")
print("Biggest x", x_nu, "Smaller 1 + n number", 1 + 2**x_nu)


###Question 9
import scipy as sp
### Question 10
print("="*50)
print("Question 10")
print(dir(sp.constants))

### Question 11
print("="*50)
print("Question 11")
print("Scipy e",sp.constants.e)
print("Is np.e = sp.e ?", sp.constants.e == np.e)

### Question 12

print("="*50)
print("Question 12")

#Unit constant - eV
print(sp.constants.eV)

#Base units
print("Charge of an electron",sp.constants.e, "potential difference (V) of 1")
#Prefix constant - Angstrom
print("Angstrom",sp.constants.angstrom)
#Real constant - Charge of an Electron
print("Electron charge",sp.constants.e)


### Question 13
print("="*50)
print("Question 13")

v_c = 1.00 / (np.sqrt(sp.constants.epsilon_0 * sp.constants.mu_0))
print("Calculated Speed of Light", v_c)