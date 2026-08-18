# File Handling
with open("input.txt", "r") as f:
    lines = f.readlines()

# Step 2: Count number of lines
line_count = len(lines)

# Step 3: Extract first two lines
first_two = lines[:2]

# Step 4: Write extracted lines to a new file
with open("output.txt", "w") as f:
    f.writelines(first_two)

# Display results
print("Total number of lines in input file:", line_count)
print("First two lines have been written to output.txt")