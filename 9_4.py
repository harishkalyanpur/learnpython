fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lst = list()
counts = dict()
for line in fh :
    if line.startswith('From:'):
        words = line.split()
        lst.append(words[1])
for word in lst:
   counts[word] = counts.get(word,0) + 1
bigword =  None
bigcount = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)
