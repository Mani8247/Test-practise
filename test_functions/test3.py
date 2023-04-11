# Write a function to find the sum of the cube of elements in a list. The list is received as an argument to the function and it should return the sum.
def sum_cub(*args):
    sum = 0
    for x in args:
        sum += (x**3)
    return sum
print(sum_cub(2,3,4,5))
