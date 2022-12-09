# [N] [G]                     [Q]    
# [H] [B]         [B] [R]     [H]    
# [S] [N]     [Q] [M] [T]     [Z]    
# [J] [T]     [R] [V] [H]     [R] [S]
# [F] [Q]     [W] [T] [V] [J] [V] [M]
# [W] [P] [V] [S] [F] [B] [Q] [J] [H]
# [T] [R] [Q] [B] [D] [D] [B] [N] [N]
# [D] [H] [L] [N] [N] [M] [D] [D] [B]
#  1   2   3   4   5   6   7   8   9 

stack1 = ['D','T','W','F','J','S','H','N']
stack2 = ['H','R','P','Q','T','N','B','G']
stack3 = ['L','Q','V']
stack4 = ['N','B','S','W','R','Q']
stack5 = ['N','D','F','T','V','M','B']
stack6 = ['M','D','B','V','H','T','R']
stack7 = ['D','B','Q','J']
stack8 = ['D','N','J','V','R','Z','H','Q']
stack9 = ['B','N','H','M','S']

stackList = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

output = ""

input = open('input.txt', 'r')
lines = input.readlines()

for line in lines:
    cleaned = line.strip().split(' ')

    numToMove = int(cleaned[1])
    stackSource = int(cleaned[3]) - 1
    stackTarget = int(cleaned[5]) - 1

    helperStack = []

    for x in range(numToMove):
        helperStack.append(stackList[stackSource].pop())
    
    for x in range(numToMove):
        stackList[stackTarget].append(helperStack.pop())

input.close()

for stack in stackList:
    output = output + (stack[-1])

print(output)