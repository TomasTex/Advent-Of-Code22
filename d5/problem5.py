def parseInput():
    with open("input.txt") as inputText:
        lineCountrer = 0
        commandInput = []
        matrix = [['F', 'C', 'J', 'P', 'H', 'T', 'W'], ['G', 'R', 'V', 'F', 'Z', 'J', 'B', 'H'], ['H', 'P', 'T', 'R'], ['Z', 'S', 'N', 'P', 'H', 'T'], [
            'N', 'V', 'F', 'Z', 'H', 'J', 'C', 'D'], ['P', 'M', 'G', 'F', 'W', 'D', 'Z'], ['M', 'V', 'Z', 'W', 'S', 'J', 'D', 'P'], ['N', 'D', 'S'], ['D', 'Z', 'S', 'F', 'M']]
        for line in inputText:
            if lineCountrer >= 10:
                commandInput.append([int(line.split()[1]), int(
                    line.split()[3]) - 1, int(line.split()[5]) - 1])
            lineCountrer += 1

        for quantity, fromWhere, toWhere in commandInput:
            what = matrix[fromWhere][-quantity:]
            matrix[toWhere] += reversed(what)
            matrix[fromWhere] = matrix[fromWhere][:-quantity]


print(parseInput())
