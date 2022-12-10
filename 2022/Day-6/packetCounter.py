input = open('input.txt', 'r')
line = input.readline()
input.close()

charCount = 0
packetStart = []
packetStartFound = False
packetStartIndex = 0
messageStartIndex = 0

for char in line:

    if not packetStartFound:
        if len(packetStart) < 4:
            packetStart.append(char)
            charCount += 1
        
        else:
            packetStart.pop(0)
            packetStart.append(char)
            charCount += 1

            if len(packetStart) == len(set(packetStart)):
                packetStartFound = True
                packetStartIndex = charCount

    elif packetStartFound:
        if len(packetStart) < 14:
            packetStart.append(char)
            charCount += 1

        else:
            packetStart.pop(0)
            packetStart.append(char)
            charCount += 1

            if len(packetStart) == len(set(packetStart)):
                messageStartIndex = charCount
                break

print(packetStartIndex)
print(messageStartIndex)

