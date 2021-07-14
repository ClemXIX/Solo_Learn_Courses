"""
List Operations


You’re making a voice recognition system.
The supported commands are stored in a list.

Complete the program to take a command as input, check if it’s supported and output "OK", if it is, and "Not supported", if not.

Sample Input
Lights Off

Sample Output
OK
The given code declares the list of supported commands.
"""

commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]

x = input()

if x in commands:
    print("OK")
else:
    print("Not supported")