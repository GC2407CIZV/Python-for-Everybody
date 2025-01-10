# 7.2 
# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

# Initialize variables
count = 0
total = 0.0

# Loop through each line in the file
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    colon_pos = line.find(":")
    num_str = line[colon_pos + 1:].strip()
    
    try:
        value = float(num_str)
        total += value
        count += 1
    except ValueError:
        continue
    
    avg = total / count

print(f"Average spam confidence: {avg}")