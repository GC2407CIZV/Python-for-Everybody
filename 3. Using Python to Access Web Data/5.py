# Import necessary libraries for web scraping
import urllib.request
import xml.etree.ElementTree as ET

# Prompt the user to input a URL if None -> go to default url
url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

# Print retrieved url
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()

# Print total of characters retrieved
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

# Find all 'count' elements in the XML data (ignoring the structure)
# The './/count' syntax means "find all 'count' elements anywhere in the XML structure"
counts = tree.findall('.//count')

# Initialize a variable 
total = 0

# Loop through each 'comment' in the list of 'counts'
for result in counts:
    # Debug print the data :)
    total = total + int(result.text)
    print(result.text) # Print the value of each count

# Print the total number of 'comment' elements and the sum of the 'count' values
print('Count:', len(counts))
print('Sum:', total)