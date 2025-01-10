# 9.4 
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


# Prompt for the file name, defaulting to "mbox-short.txt" if no input is given
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Create a dictionary to store the sender's email and the count of messages
email_counts = {}

# Read through the file line by line
for line in handle:
    # Only process lines that start with 'From '
    if line.startswith('From '):
        # Split the line into words
        words = line.split()
        # Extract the email address (second word)
        email = words[1]
        # Update the count for the email in the dictionary
        email_counts[email] = email_counts.get(email, 0) + 1

# Initialize variables to track the most prolific sender
max_count = None
max_email = None

# Loop through the dictionary to find the sender with the highest count
for email, count in email_counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

# Print the most prolific sender and the number of messages
print(max_email, max_count)
