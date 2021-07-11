"""
while Loop


You are making a game! The player tries to shoot an object and can hit or miss it.
The player starts with 100 points, with a hit adding 10 points to the player’s score, and a miss deducting 20 points.

Your program needs to take 4 action results as input ("hit" or "miss"), calculate and output the player’s remaining points.

Sample Input
hit
hit
miss
hit

Sample Output
110

Explanation: 3 hits add 30 points, one miss deducts 20, making the total points equal to 110.
Use a while loop to take input during each iteration and calculate the points.
"""

hits = 1
points = 100

while hits <= 4:
    test = input()
    if test == "hit":
        points += 10
    elif test == 'miss':
        points -= 20
    hits += 1

print(points)