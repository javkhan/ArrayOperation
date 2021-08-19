import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print("Output of adding x and y with a '+' operator:",x + y)
print("Output of adding x and y using 'numpy.add':",np.add(x, y))

print("Output of subtracting x and y with a '-' operator:",x - y)
print("Output of subtracting x and y using 'numpy.subtract':",np.subtract(x, y))

print("Output of elementwise product of x and y with a '*' operator:",x * y)
print("Output of element wise product of x and y using 'numpy.multiply':",np.multiply(x, y))

print("Output of elementwise division x and y with a '/' operator:",x / y)
print("Output of elementwise division x and y using 'numpy.divide':",np.divide(x, y))

print("Output of elementwise square root x using 'numpy.sqrt':",np.sqrt(x))