def parseInput() -> list:
    f = open("input.txt", "r")
    lines = f.readlines()
    temp = []
    for line in lines:
        line = line.strip("\n")
        temp.append(line)     
    f.close()
    lines = temp
    return lines

def giveListWithGroups(lines:list) ->list:
    listWithGroups = []
    groupSize = 3
    for i in range(0, len(lines), groupSize):
        group = lines[i:i+groupSize]
        listWithGroups.append(group)
    return listWithGroups
    
def commonTypeAndItsPriority(lines: list) -> int:
    listWithGroups = giveListWithGroups(lines)
    listWithGroupPriorities = []
    
    for group in listWithGroups:
        for letter in group[0]:
            if letter in group[1] and letter in group[2]:    
                listWithGroupPriorities.append(letterPriority(letter))
                break #only one letter per group
                    
    return sum(listWithGroupPriorities)
    
def sumPriorities(lines:list) ->int:
    sum = 0
    for line in lines:
        sum += commonTypeAndItsPriority(line)
    return sum

def letterPriority(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96 
    return ord(letter) - 38

print(commonTypeAndItsPriority(parseInput()))