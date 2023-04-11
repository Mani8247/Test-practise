# Write a program "list_grouping.py" that takes a list and splits into smaller lists of given size. For example,
# if lst = [1, 2, 3, 4, 5, 6], size = 2, it should return [[1, 2], [3,4], [5,6]] and
# if lst = [1,2,3,4,5,6,7,8,9], size = 4 then it should return [[1,2,3,4],[5,6,7,8],[9]]. 

m = []
n = int(input("enter list: "))
for i in range(n):
    v = int(input("enter num :"))
    m.append(v)
print(m)
size = int(input("enter size: "))
n = []
for i in range(0,len(m),size):
    n.append(m[i:i+size])
print(n)