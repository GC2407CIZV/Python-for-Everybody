# Following Links in Python
# The program will use urllib to read the HTML from the data files below, 
# extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, 
# follow that link and repeat the process a number of times and report the last name you find.

# Import necessary libraries for web scraping
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certicate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt the user to enter information for web scraping
url = input('Enter URL - ')
pos = int(input("Enter position - ")) -1
count = int(input("Enter count - "))

# Initialize a counter to track the number of times we have scraped
count1 = 0

# Loop to repeat the scraping process the number of times specified by the user
while (count1 < count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags (<a>) from the parsed HTML
    tags = soup('a')
    url = tags[pos].get('href')
    name = tags[pos].contents[0]
    count1 = count1 + 1

# After completing the loop, print the name of the last link that was followed
print(name)