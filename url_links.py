#scraping numbers from html data with beautiful soup
#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
#'pip3 install beautifulsoup4' on windows to install

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') #http://py4e-data.dr-chuck.net/comments_1876938.html(data is here)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags
list = []
count = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    numbers = int(str(tag.contents[0]))
    #print(numbes)
    list.append(numbers)
    count = count+1
print('Count', count)
print('Sum', sum(list))