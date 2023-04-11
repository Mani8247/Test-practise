# Write a function to display the elements of list thrice if it is a number and display the element terminated with ‘#’ if it is not a number.
# For example, if the content of list is [‘41’,‘DHRUVA’,‘GURU’, ‘13’,‘ZARA’]
# The output should be
# 	414141
# 	DHRUVA#
# 	GURU#
# 	131313
# 	ZARA#
def elem(list):
    for i in list:
        if i.isdigit():
            print(i * 3)
        else:
            print(i + "#")
    return
print(elem(["22","mani",'45','harish']))