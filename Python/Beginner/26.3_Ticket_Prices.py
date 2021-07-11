"""
continue


You are making a ticketing system.
The price of a single ticket is $100.
For children under 3 years old, the ticket is free.

Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.

Sample Input
18
24
2
5
42

Sample Output
400
There is one child under 3 among the passengers, so the total price of 5 tickets will be $400.
"""

total = 0
passengers = 0

while passengers <= 4:
    x = int(input())
    if x > 3:
        total += 100
        passengers += 1
    else:
        passengers += 1
        continue


print(total)