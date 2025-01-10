# 6.5 
# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

# Find the position of the colon
pos = text.find(':')

# Extract the number from the position of the colon onwards and strip extra spaces
num_str = text[pos+1:].strip()

# Convert the extracted string to a floating point number
num = float(num_str)

# Print the result
print(num)