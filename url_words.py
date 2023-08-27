#this code computes the words
import urllib.request, urllib.parse, urllib.error

#open file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#create a dictionary
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)