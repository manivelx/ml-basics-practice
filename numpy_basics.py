import numpy as np

arr = np.arange(1, 13)

print("Array:", arr)

print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

matrix = arr.reshape(3,4)
print("Reshaped Matrix:\n", matrix)
