import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.xml'
serviceurl = input('Enter location: ')
#while True:
#    address = input('Enter location: ')
#    if len(address) < 1: break

#    url = serviceurl + urllib.parse.urlencode({'address': address})
url = serviceurl
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
results = tree.findall('.//count')
val = 0
print('Count:', len(results))
for item in range(len(results)) :
  val = val + int(results[item].text)
print(val)
