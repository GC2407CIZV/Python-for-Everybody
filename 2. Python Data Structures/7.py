#10.2 
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Initialize an empty dictionary to store the hour counts
hour_counts = dict()

# Read through the file line by line
for line in handle:
    # Check if the line starts with "From " to get email sender information
    if line.startswith("From "):
        # Split the line into words
        words = line.split()
        # The time is the sixth word in the line (index 5)
        time = words[5]
        # Extract the hour by splitting the time at the colon
        hour = time.split(":")[0]
        # Increment the count for the hour in the dictionary
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Sort the hours and print the counts
for hour in sorted(hour_counts):
    print(hour, hour_counts[hour])