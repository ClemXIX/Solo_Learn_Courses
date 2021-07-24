"""
Multiple Variables


You can use multiple variables to take multiple inputs for your program.
For example, the following code takes two inputs and stores them in the variables x and y:
x = input()

y = input()
PY
Task:
Given the code above, output the input x repeated y times.

Sample Input:
awesome
3

Sample Output:
awesomeawesomeawesome
Remember, the input() function results in a string. You need to convert the result into the corresponding type, if you need to use it as a number.
"""

x = input()
y = int(input())

print(x * y)