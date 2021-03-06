"""
Ranges


A group of buildings have restrooms on every 5th floor.
For example, a building with 12 floors has restrooms on the 5th and 10th floors.

Create a program that takes the total number of floors as input and outputs the floors that have restrooms.

Sample Input
23

Sample Output
5
10
15
20
You can define a range with the corresponding rules and output the numbers in that range.
Remember, that range(a, b) includes a, but does not include b.
"""

n = int(input())

for floors in range(0, n, 5):
    if floors != 0:
        print(floors)