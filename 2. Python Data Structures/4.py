# 8.4 
# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    words = line.split() # Split line to words
    for word in words:  # Iterate over each word
        if word not in lst:  # Check if the word is already in the list
            lst.append(word) # Add word to the list

lst.sort()

print(lst)