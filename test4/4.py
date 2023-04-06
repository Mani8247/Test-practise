#Write a program "dups.py" to print a list with all duplicates in the given list. For example, if lst=[1, 3, 2, 1, 2, 5, 6] it should return [1, 2].
l = [1, 3, 2, 1, 2, 5, 6]
res = []
for i in l:
    if l.count(i)>1:
        res.append(i)
res = set(res)
print(list(res)) 
