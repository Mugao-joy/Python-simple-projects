#following links with python
#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
#scan for a tag that is in a particular position relative to the first name in the list,
#follow that link and repeat the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#crawl pages  of the url
url = input('Enter URL - ') #'http://py4e-data.dr-chuck.net/known_by_Alister.html'
repeat = int(input('Enter number of repetations: '))
position = int(input('Enter the link position: '))

#to repeat desired times
for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count +1

        #break at desired position
        if count>position:
            break
        url = tag.get('href', None)
        name = tag.contents[0]

print(name)