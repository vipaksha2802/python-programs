import numpy as np
import pandas as pd

# Create NumPy array of student marks
marks = np.array([85, 72, 90, 65, 88, 95, 76, 81, 69, 92])

# Calculate mean, median, maximum and minimum
print("Mean Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))

# Create Pandas DataFrame
students = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Marks": marks
})

print("\nStudent Data:")
print(students)

# Display students scoring more than 80 marks
print("\nStudents scoring more than 80 marks:")
print(students[students["Marks"] > 80])
