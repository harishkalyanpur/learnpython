fname = input("Enter file name: ")
fh = open(fname)
lst = list()
glst = list()
for line in fh:
 line = line.rstrip()
 lst = line.split()
 for i in range(len(lst)):
  if len(glst) is 0:
   glst.append(lst[0])
   continue 
  if lst[i] in glst:
   continue
  glst.append(lst[i])
glst.sort()
print(glst)
