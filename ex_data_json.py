import urllib.request, urllib.parse, urllib.error
import json

#serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.json'
serviceurl = input('Enter location: ')
url = serviceurl
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = json.loads(data)
info = tree['comments']
print(len(info))
tot = 0
for val in info:
  tot = tot + int(val['count'])
print(tot)
