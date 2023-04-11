# """ Define a function “sign” which takes a numerical argument and returns -1 if it's negative, 
# 1 if it's positive, and 0 if it's 0."""

def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    return 0
print(sign(23))
print(sign(-10))
print(sign(0))