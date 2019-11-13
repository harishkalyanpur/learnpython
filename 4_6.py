hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try :
    h = float(hours)
    r = float(rate)
except :
    quit ()

def computepay(h,r):
    if h > 40 :
        pay = (40 * r) + ((h - 40) * 1.5 * r)
        return pay
    elif h <= 40 :
        pay = (h * r)
        return pay
computepay(h,r)        
print ("Pay",computepay(h,r))
