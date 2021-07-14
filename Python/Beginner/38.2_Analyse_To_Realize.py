"""


You’re analyzing a data set and need to remove the outliers (the smallest and largest values.
The data is stored in a list).

Complete the code to remove the smallest and largest elements from the list and output the sum of the remaining numbers.
Remember the functions a list supports: min and max can be used to get the smallest and largest numbers.
"""

data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]

def working_on(x):
    # take a list as arg, remove max and min then return the sum of the list
    x.remove(max(x))
    x.remove(min(x))
    total = 0
    for i in x:
        total += i

    return total

print(working_on(data))