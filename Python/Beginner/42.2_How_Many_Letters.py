"""
Letter Count


Write a function that takes a string and a letter as its arguments and returns the count of the letter in the string.

Sample Input
hello, how are you?
o

Sample Output
3

Explanation: The letter o appears 3 times in the given text.
The given code takes the string and letter from input and passes them to the letter_count() function.
Define the function, so that the given code works as expected.
"""

def letter_count(text, letter):
    return text.count(letter)

text = input()
letter = input()

print(letter_count(text, letter))
