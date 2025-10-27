import numpy as np
import matplotlib.pyplot as plt

# Question 3
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Question 4
print(y[1])
print(y[4])
print(y[0])
print(y[-1])
print(y[-3])

# Question 5
print(y[0:4])
print(y[2:])
print(y[-3])

# Question 6
time1 = [0.0, 0.9, 1.3, 1.7, 2.3, 3.0, 3.8, 4.8, 6.0]
speed1 = [0.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

print(time1)
print(speed1)

# Question 7
time1_array = np.array(time1)
speed1_array = np.array(speed1)

print(time1_array)
print(speed1_array)

# Question 7E
g_array = np.array([1, 2, 3, 4])
gsquared = g_array**2
print(gsquared)

# Question 7F
conversion_factor = 0.44704
speed1_ms = speed1_array * conversion_factor

print(speed1_ms)

# Question 10
plt.figure(figsize=(10, 5))

plt.plot(time1_array, speed1_array, 'r-', label='Speed vs Time 1')

# Question 11
time2 = [0.0, 1.3, 1.7, 2.3, 3.0, 3.8, 4.7, 5.6, 6.8]
speed2 = [0.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

time2_array = np.array(time2)
speed2_array = np.array(speed2)

# Question 12
plt.plot(time2_array, speed2_array, 'bs', label='Speed vs Time 2')

# Question 14
plt.xlabel('Time (seconds)')
plt.ylabel('Speed (miles per hour)')
plt.title('Speed vs Time')
plt.xlim(0, 7)
plt.legend()
plt.show()

# Question 18
x_vals = np.linspace(-2.5, 2.5, 11)
sin_vals = np.sin(x_vals)
cos_vals = np.cos(x_vals)

# Question 19
plt.figure(figsize=(10, 5))

# Question 20
plt.plot(x_vals, sin_vals, 'o-', label='sin(x)')
plt.plot(x_vals, cos_vals, 's-', label='cos(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
