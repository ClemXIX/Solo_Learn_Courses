"""
break


You’re making a calculator that should add multiple numbers taken from input and output the result.

The number of inputs is variable and should stop when the user enters "stop".

Sample Input
4
32
6
stop

Sample Output
42

Use an infinite loop to take user input and break it, if the input equals to "stop".
Remember, the input is a string by default. You need to convert it to int to be able to use it as a number.
"""

sum = 0
while True:
    x = input()
    if x != 'stop':
        sum += int(x)
    else:
        break

print(sum)
