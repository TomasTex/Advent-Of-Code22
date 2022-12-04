def parseInput()-> list:
    file = open('input.txt', 'r')
    data = []
    temp = []
    for line in file:
        data.append(line.split())
    for line in data:
        temp.append(line[0].split(','))
    data = temp.copy()
    temp.clear()
    for line in data:
        for elf in line:
            temp.append(elf.split('-'))
    data = temp.copy()
    return data

def isOneInsideOther(elf1: list, elf2: list) -> bool:
    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        return True
    elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
        return True
    else:
        return False

def answer(data: list) -> int:
    sum = 0
    for i in range(len(data)-1):
        if i % 2 == 0:
            sum += 1 if isOneInsideOther(data[i], data[i+1]) else 0
    return sum
        
print(answer(parseInput()))
