# ""Write a function ‘select_second’ with one argument ‘L’ which is a list to return
#  the second element of the given list. If the list has no second element, it should return None.
#  """


def select_second(L):
        if len(L) < 2:
                return None
        return L[1]
print(select_second([23,45,67,89]))
print(select_second([1]))
