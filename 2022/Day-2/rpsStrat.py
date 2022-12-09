input = open('input.txt', 'r')
lines = input.readlines()
input.close()

strategy1 = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
strategy2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

score1 = 0
score2 = 0

for line in lines:
    stripped = line.strip()

    score1 = score1 + strategy1[stripped]
    score2 = score2 + strategy2[stripped]

print("Score using Strategy One: " + str(score1))
print("Score using Strategy Two: " + str(score2))