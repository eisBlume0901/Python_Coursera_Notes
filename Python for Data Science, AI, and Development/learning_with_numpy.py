import numpy as np
import matplotlib.pyplot as plt

even = np.array([2, 4, 6, 9, 11, 13])
print(even)
print(type(even))
print(even.size) # 6
print(even.ndim) # 1
print(even.shape) # (6,)
print(even.dtype) # int64
even[3] = 8
print(even)
even[4:6] = np.array([10, 12])
print(even)

# Vector Addition using numpy
u = np.array([[1], [9]]) # x = 1, y = 8
v = np.array([[19], [1]]) # x = 19, y = 1
print(u + v)

# Vector Addition without using numpy
u = [1, 0]
v = [0, 1]
z = []
for n, m in zip(u, v):
    z.append(n+m)
print(z)

# Vector Subtraction using numpy
u = np.array([[10, 1], [9, 4]])
v = np.array([[5, 3], [0, 4]])
print(u - v)

# Scalar Multiplication with numpy
y = np.array([[1], [2]])
print(2*y) # each component is multiplied to 2, it is expected to have 2 and 4

# Scalar Multiplication without using numpy
y = [1, 2]
z = []

for n in y:
    z.append(2*n)
print(z)

# Scalar Addition with numpy (broadcasting)
u = np.array([2, 4, 5, 7, 9])
print(u + 1)

# Hadamard Product with numpy
u = np.array([[1, 4], [2, 7]])
v = np.array([[3, 1], [8, 0]])
w = u * v
print(w)

# Dot Product with numpy
u = np.array([[1, 4], [2, 7]])
v = np.array([[3, 1], [8, 0]])
print(np.dot(u, v))

# Universal functions of numpy
grades = np.array([75, 80, 82, 90, 76, 85, 93])
# mean()
print(grades.mean())
# max()
print(grades.max())
# min()
print(grades.min())
# pi
print(np.pi)
# sin()
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)
print(x)
# linspace() - line space for creating an evenly space number line
print(np.linspace(-2, 2, num=9)) # Starts from -2 then ends to -2 with 9 elements within the range

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()