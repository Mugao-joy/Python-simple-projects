#we are simulating what happens in a web browser, HTTP request in python
import socket #import requests is best though
#below is just a file handle without any data
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#reach out and connect to a destination with a domain name
mysock.connect(('data.pr4e.org', 80)) #function call,talk to port 80
#get the http command(there are strings in python that are in unicode hence use encode)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n' .encode()
mysock.send(cmd)

#this while loop will ask for upto 512 characters from the text on the website
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())#decode converts into the internal format-unicode
mysock.close()