""" Write a function half_and_half that takes in a list and change the list 
such that the elements of the second half are now in the first half. For example,
 if the list is [10,20,30,40,50,60], then it should return [40,50,60,10,20,30] 
 and if the list is [10,20,30,40,50,60,70], then it should return [50,60,70,40,10,20,30]."""

def half_and_half(m):
    list = []
    l1 = m[-3:] + m[0:3]
    list.extend(l1)
    return list 

print(half_and_half([10,20,30,40,50,60]))

def half_and_half(n):
    l = []
    l1 = n[-3:] +n[3:4] +n[0:3]
    l.extend(l1)
    return l
print(half_and_half([10,20,30,40,50,60,70]))



# def half(l):
#     m = []
#     list1 = l[-3::1]
#     list2 = l[-1:-5:-1]
#     m.extend(list1)
#     m.extend(list2)
#     return m
# print(half([10,20,30,40,50,60,70]))
# print(half([10,20,30,40,50,60]))
