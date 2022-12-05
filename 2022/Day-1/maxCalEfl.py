input = open('input.txt', 'r')

lines = input.readlines()

currentElf = 0
elves = dict()

for line in lines:
    if line == '\n':
        currentElf = currentElf + 1

    elif currentElf in elves:
        elves[currentElf] = elves[currentElf] + int(line.strip())

    else:
        elves[currentElf] = int(line.strip())

input.close()

calList = list(elves.values())
calList.sort(reverse = True)

firstElf = calList[0]

print("Max calories by one Elf: " + str(firstElf))

secondElf = calList[1]
thirdElf = calList[2]

topThreeElves = firstElf + secondElf + thirdElf

print("Total calories of top three Elves: " + str(topThreeElves))