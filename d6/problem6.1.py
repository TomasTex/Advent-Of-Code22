def parseInput():
    # Read the input file
    f = open("input.txt", "r")
    inpt = f.readline()
    f.close()
    return inpt

def anyEqual(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return True
    return False

def findFirstMarker(inputText: str) -> int:
    index = 0
    for ch in range(len(inputText)):
        index += 1
        if ch < 12:
            continue
        if not anyEqual([inputText[ch], inputText[ch -1], inputText[ch -2], inputText[ch -3], inputText[ch -4], inputText[ch -5], inputText[ch -6], inputText[ch-7], inputText[ch -8], inputText[ch -9], inputText[ch -10], inputText[ch -11], inputText[ch -12], inputText[ch -13]]):
            return index


        

print(findFirstMarker(parseInput()))