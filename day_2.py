# Two rows of data
# First is opponent's play: A,B,C (Rock, Paper, Scissors);
# Second is your response: is X,Y,Z (Rock, Paper, Scissors)
# Score is shape + outcome
# Rock = 1, Paper = 2, Scissors = 3; 0 for loss, 3 for draw, 6 for win

f = open("input_day_2.txt", "r")
in_data = f.read()
f.close()

# Determine the winner of each round
# Determine the scores after

# X draws A, loses to B, beats C
# Y beats A, draws B, loses to C
# Z loses to A, beats B, draws C

# Wins: X-C, Y-A, Z-B
# Draws: X-A, Y-B, Z-C
# Loses: X-B, Y-C, Z-A

#

shapes = {
    "A":"Rock",
    "X":"Rock",
    "B":"Paper",
    "Y":"Paper",
    "C":"Scissors",
    "Z":"Scissors"
}

def result(pair):
    if pair[0]==pair[1]:
        return "Draw"
    elif pair[0]=="Rock":
        if pair[1]=="Paper":
            return "Win"
        elif pair[1]=="Scissors":
            return "Loss"
    elif pair[0]=="Paper":
        if pair[1]=="Rock":
            return "Loss"
        elif pair[1]=="Scissors":
            return "Win"
    elif pair[0]=="Scissors":
        if pair[1]=="Rock":
            return "Win"
        elif pair[1]=="Paper":
            return "Loss"


guide = [g.split() for g in in_data.split("\n")]

#shapes[g[0]], shapes[g[1]]

score = 0

for g in guide:
    round_score = 0

    if shapes[g[1]]=="Rock":
        round_score+=1
    elif shapes[g[1]]=="Paper":
        round_score+=2
    elif shapes[g[1]]=="Scissors":
        round_score+=3

    results = result([shapes[g[0]], shapes[g[1]]])

    if results=="Draw":
        round_score+=3
    elif results=="Loss":
        round_score+=0
    elif results=="Win":
        round_score+=6

    score += round_score

    #print(g, shapes[g[0]], shapes[g[1]], results, round_score, score)

#print(score)

# Part 2: X means you need to lose, Y means you need to draw, Z means you need to win
score = 0
for g in guide:
    round_score = 0
    if g[1]=="X":
        # Lose
        if shapes[g[0]]=="Rock":
            # Must choose Scissors
            round_score+=3
        elif shapes[g[0]]=="Paper":
            # Must choose Rock
            round_score+=1
        elif shapes[g[0]]=="Scissors":
            # Must choose Paper
            round_score+=2
    elif g[1]=="Y":
        # Draw
        round_score+=3
        if shapes[g[0]]=="Rock":
            round_score+=1
        elif shapes[g[0]]=="Paper":
            round_score+=2
        elif shapes[g[0]]=="Scissors":
            round_score+=3
    elif g[1]=="Z":
        # Win
        round_score+=6
        if shapes[g[0]] == "Rock":
            # Must choose Paper
            round_score += 2
        elif shapes[g[0]] == "Paper":
            # Must choose Scissors
            round_score += 3
        elif shapes[g[0]] == "Scissors":
            # Must choose Rock
            round_score += 1

    score+=round_score

    print(g, shapes[g[0]], round_score, score)

print(score)