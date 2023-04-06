#Write a program "count_digits.py" to print the number of digits in the given number.
num = input("enter a num:")
c = 0
for i in num:
    if i.isdigit():
        c += 1
print(f"the number of digits in the given number is",c)