import numpy as np

# Create a one-dimensional array containing numbers from 1 to 10
arr = np.arange(1, 11)

print("Original Array:", arr)

# Slicing operations
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Even-indexed elements:", arr[::2])
print("Reversed Array:", arr[::-1])

# Statistical measures
print("\nStatistical Measures:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting
# Add 5 to every element
arr = arr + 5

print("\nArray after broadcasting (adding 5):", arr)

# Multiply every element by 2 using broadcasting
arr = arr * 2

print("Array after broadcasting (multiplying by 2):", arr)