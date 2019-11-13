fname = input ("Enter the filename:")
if len(fname) < 1 : fname = 'mbox-short.txt'
fh = open(fname)
lst = list()
tm = list()
a = list()
di = dict()
for lin in fh :
    lin = lin.rstrip()
    if lin.startswith('From ') :
      wds = lin.split()
      lst.append(wds[5])
      for w in lst :
        tm = w.split(':')
      a.append(tm[0])
#print(a)
for word in a:
   di[word] = di.get(word,0) + 1
for k,v in sorted(di.items()):
  print(k,v)
