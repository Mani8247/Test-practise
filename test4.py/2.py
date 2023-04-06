# Write a program "num_identifier.py" that will print whether the number is a single digit number or double digit number or big number.
#If given number is one digit number, print "Single digit number"
#If given number is two digit number, print "Double digit number"
#If number is three digit number or bigger, print "Big number"
num = int(input("enter a num:"))
if num<10:
    print("single digit number")
elif num<100 and num>=10:
    print("double digit number")
else:
    print("big number")
    