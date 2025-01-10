# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.

import re

# Prompt user for file
name = input("Enter file: ")

# If no input, open default file
if len(name) < 1:
    name = "regex_sum_2153294.txt"
file = open(name)

text = file.read()

# Find all numbers in the text
numb = re.findall('[0-9]+', text)

total = 0

for i in numb:
    i = int(i)
    total = total + i

print(total) 

file.close()