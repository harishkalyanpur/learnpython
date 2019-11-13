fname = input("Enter file name:")
try:
  fh = open(fname)
except:
  print("Error: Check filename",fname)
count = 0
value = 0
tot = 0
for line in fh:
 line = line.strip()
# print(line)
 if 'X-DSPAM-Confidence:' in line:
#  length = len(line)
  count = count + 1
  pos = line.find(':')
  value = line[pos+1:]
  val = float(value)
  tot = tot + val
print("Average spam confidence:",tot/count)
