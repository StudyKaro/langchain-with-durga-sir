# slice operation in python
# slicing is used to extract a portion of a list, string, or any other sequence type
# syntax: sequence[start:stop:step]
list_example = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list_example[2:7])  # last index excluded, Output: [30, 40, 50, 60, 70]
print(list_example[2:7:2])  # Output: [30, 50, 70]
print(list_example[::2])  # Output: [10, 30, 50, 70, 90]
print(list_example[:8])  # Output: [10, 20, 30, 40, 50, 60, 70, 80]
print(list_example[-4:-1])  # Output: [70, 80, 90]
print(list_example[-1])  # Output: 100
print(list_example[-3:])  # Output: [80, 90, 100]

# copy list into another list using slicing
list_copy = list_example[:]
list_2 = [100,120,140,160,180,200]
# unpacking the list into variables
a, b, c, d, e, f = list_2   

list_union = [*list_example, *list_2]
print(list_union)  # Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 120, 140, 160, 180, 200]

# No arrayIndexOutOfBoundsException in python, if we try to access an index which is out of bounds, it will return an empty list instead of throwing an exception.
print(list_example[-15:])  # Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]