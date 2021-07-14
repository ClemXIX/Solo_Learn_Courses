"""
Search Engine


You’re working on a search engine. Watch your back Google!

The given code takes a text and a word as input and passes them to a function called search().

The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

Sample Input
"This is awesome"
"awesome"

Sample Output
Word found
Define the search() function, so that the given code works as expected.
"""

# using return print("word") will outup a None in sololearn cause the sample is using print(search())

def search(text, word):
    if word in text:
        return "Word found"
    else:
        return "Word "


text = input()
word = input()

print(search(text, word))