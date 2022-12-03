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

#ASCII
#A -> Z = 65 -> 90
#a -> z = 97 -> 122

def commonTypeAndItsPriority(line: str) -> int:
    halfLength = len(line) // 2
    firstHalf, secondHalf = line[:halfLength], line[halfLength:]
    for letter in firstHalf:
        if letter in secondHalf:
            return letterPriority(letter)

def sumPriorities(lines:list) ->int:
    sum = 0
    for line in lines:
        sum += commonTypeAndItsPriority(line)
    return sum

def letterPriority(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96 
    return ord(letter) - 38

print(sumPriorities(parseInput()))