input = open('input.txt', 'r')
lines = input.readlines()
input.close()

sum = 0
badgeSum = 0
elfNum = 0
badgeSet1 = set()
badgeSet2 = set()
badgeSet3 = set()

for line in lines:
    rucksack = line.strip()

    compartment1 = rucksack[0:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]

    for item in compartment1:
        if item in compartment2:
            asciiNum = ord(item)

            if asciiNum < 97:
                sum = sum + asciiNum - 38

            else:
                sum = sum + asciiNum - 96

            break

    if elfNum % 3 == 0:
        badgeSet1 = set()
        badgeSet2 = set()
        badgeSet3 = set()
        for item in rucksack:
            badgeSet1.add(item)

    if elfNum % 3 == 1:
        for item in rucksack:
            badgeSet2.add(item)

    if elfNum % 3 == 2:
        for item in rucksack:
            badgeSet3.add(item)

        badgeSet = badgeSet1.intersection(badgeSet2, badgeSet3)
        badge = ord(badgeSet.pop())

        if badge < 97:
            badgeSum = badgeSum + badge - 38

        else:
            badgeSum = badgeSum + badge - 96
            
    elfNum = elfNum + 1

print("Duplicate Item Sum: " + str(sum))
print("Badges Sum: " + str(badgeSum))
