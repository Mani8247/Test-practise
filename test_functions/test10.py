"""Given a string, return a list containing the characters of the string. If a character in the string is a space
 or a digit greater than 5, remove them and do not include them in the array. Note: the initial code in 
 the editor uses tabs for indentation. Don't mix it with spaces. 
Examples: 
	Input: "my string" 
	Output: ["m","y","s","t","r","i","n","g"] 
	Input: "5 dollar" 
	Output: ["5","d","o","l","l","a","r"] 
	Input: "6 cents" 
	Output: ["c","e","n","t","s"]  """


def list_ch(s):
    r = []
    for x in s:
        if x != " " and (not x.isdigit() or int(x) <= 5):
            r.append(x)
    return r

print(list_ch("my string"))
print(list_ch("6 cents"))
