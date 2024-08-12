import numpy as np
import matplotlib.pyplot as plt

my_array = np.array([[1, 2], [4, 5], [6, 7]])

print(my_array)
print(my_array.shape)
print(my_array.dtype)
result = my_array + 2
print(result)

mean = np.mean(my_array)
print(mean)

median = np.median(my_array)
print(median)
plt.show()