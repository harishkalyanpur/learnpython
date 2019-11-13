score = input("Enter Score: ")
try:
	s = float(score)
except:
    quit ()
if (s <= 1.0) & (s >= 0.9) :
	print ("A")
elif (s < 0.9) & (s >= 0.8) :
	print ("B")
elif (s < 0.8) & (s >= 0.7) :
	print ("C")
elif (s < 0.7) & (s >= 0.6) :
	print ("D")
elif s < 0.6 :
	print ("F")
elif s > 1.0 :
	print ("Out of range")
