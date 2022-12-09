input = open('input.txt', 'r')
lines = input.readlines()

countContain = 0
countOverlap = 0

for line in lines:
    stripped = line.strip()
    pairList = stripped.split(',')
    elf1 = pairList[0].split('-')
    elf2 = pairList[1].split('-')

    a = int(elf1[0])
    b = int(elf1[1])
    c = int(elf2[0])
    d = int(elf2[1])

    if a <= c and b >= d or c <= a and d >= b:
        countContain = countContain + 1
    
    if a >= c and a <= d or b >= c and b <= d or c >= a and c <= b or d >= a and d <= b:
        countOverlap = countOverlap + 1

input.close()

print("Ranges contained in the other: " + str(countContain))
print("Ranges that overlap: " + str(countOverlap))
