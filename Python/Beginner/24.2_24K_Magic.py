"""
Boolean Logic


Now that we know how to combine multiple conditions, let’s improve our gold purity checker program and output the corresponding purity level in Karats!

Here is the purity chart we’ll be using:
24K – 99.9%
22K – 91.7%
20K – 83.3%
18K – 75.0%

If the percentage is between 75 and 83.3, the gold is considered to be 18K.
If it's between 83.3 and 91.7 - then it’s 20K, and so on.

Given the percentage as input, output the corresponding Karat value, including the letter K.

Sample Input:
92.4

Sample Output:
22K
Do not output anything, if the percentage is lower than 75%.
"""

purity = float(input())

if 75 <= purity < 83.3:
    print("18K")
elif purity >= 83.3 and purity < 91.7:
    print("20K")
elif purity >= 91.7 and purity < 99.9:
    print("22K")
elif purity >= 99.9:
    print("24K")