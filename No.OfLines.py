#!/usr/local/bin/python3
fh = open("/var/tmp/test", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines in this document")
