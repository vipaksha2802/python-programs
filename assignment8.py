# Experiment 8: File Handling and I/O

# Open the input file in read mode
with open("input.txt", "r") as file:
    lines = file.readlines()

# Count total number of lines
line_count = len(lines)

# Extract the first two lines
first_two_lines = lines[:2]

# Write the first two lines into output.txt
with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

# Display results
print("Total number of lines:", line_count)
print("\nFirst two lines are:")

for line in first_two_lines:
    print(line, end="")

print("\n\nExtracted lines have been written to output.txt")