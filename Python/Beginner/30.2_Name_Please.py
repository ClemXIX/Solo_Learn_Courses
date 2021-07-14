"""
Strings as Lists


You need to take the first and last name of a person as input and output the initials (first letters of the first and last name).

Sample Input
James
Smith

Sample Output
J.S.
In order to match the output, you need to place dots after each initial.
"""

fname = input()
lname = input()

outup = print(f"{fname[0]}.{lname[0]}.")