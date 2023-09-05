#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
#The program will prompt for a URL, read the XML data from that URL using urllib
#and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#'pip install elementpath' install in command prompt
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('Count', len(counts))
print('Sum', sum([int(i.text) for i in counts]))