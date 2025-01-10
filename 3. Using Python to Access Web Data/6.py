# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
# The program will prompt for a URL, 
# read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter the sum below.

# Import necessary libraries for web scraping
import urllib.request, urllib.parse, urllib.error
import json

# Prompt the user to input a URL if None -> go to default url
url = input("Enter location: ")
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
print("Retrieving ", url)

data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

sum = 0

for comment in info["comments"]:
    sum = sum + int(comment['count'])

print(len(info["comments"]))
print(sum)
