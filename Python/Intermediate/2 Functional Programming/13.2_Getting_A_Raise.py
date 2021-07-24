"""
map


You work on a payroll program.
Given a list of salaries, you need to take the bonus everybody is getting as input and increase all the salaries by that amount.
Output the resulting list.
You can use the map() function to increase all the values of the list.
"""

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())

# creating a lambda function then printing it

raising = lambda salaires, up: [i + bonus for i in salaires]

print(raising(salaries, bonus))

# the map function
print(list(map(lambda x: x + bonus, salaries)))
