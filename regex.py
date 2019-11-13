fname = input ("Enter the filename:")
if len(fname) < 1 : fname = 'regex_sum_101005.txt'
fh = open(fname)
import re
val = 0
for lin in fh:
  lst = re.findall('([0-9]+)', lin)  
  for i in lst :
    val = val + int(i)
print(val)
