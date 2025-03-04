# Scraping Numbers from HTML using BeautifulSoup 
# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
# The program will use urllib to read the HTML from the data files below, and parse the data, 
# extracting numbers and compute the sum of the numbers in the file.

# Import necessary libraries for web scraping
from urllib import request
from bs4 import BeautifulSoup

html=request.urlopen('http://py4e-data.dr-chuck.net/comments_2153296.html').read()
soup = BeautifulSoup(html)

total = 0

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
   total = total + int(tag.contents[0])

print(total)