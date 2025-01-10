# Exploring the HyperText Transport Protocol

# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

# http://data.pr4e.org/intro-short.txt
# There are three ways that you might retrieve this web page and look at the response headers:

# Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
# Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.

# First, we need to bring in the necessary tools to talk to other computers over the internet.
import socket

# We're making a "connection" to another computer. 
# Think of this as opening a line to a website (like opening a phone line to talk to someone).
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now, we're dialing the phone number (connecting to the server) using the website's address ('data.pr4e.org')
# and we're using port 80, which is the common port for websites.
mysock.connect(('data.pr4e.org', 80))

# We need to ask the website for something. 
# We're asking it for a file (called 'intro-short.txt') using a specific request (like asking for a document).
# We format our request in a special way, just like you would when you send a letter.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

# We send our request to the website through the connection (like talking over the phone)
mysock.send(cmd)

# Now, we're waiting to hear back from the website.
# We will receive the data in pieces, one chunk at a time (like listening to someone speak in parts).
while True:
    
    # We try to receive up to 512 characters (bytes) of the response at once.
    data = mysock.recv(512)

    # If the response is empty (no more data), we stop listening.
    if (len(data) < 1):
        break

    # We then "translate" the data from computer code (bytes) into something we can read (a string).
    # Then we print it out to see the website's response.
    print(data.decode())

# When we're done, we hang up the phone (close the connection).
mysock.close()