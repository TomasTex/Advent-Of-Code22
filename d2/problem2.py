# A = Rock    X = Rock
# B = Paper   Y = Paper
# C = Scisors Z = Scisors

def parseInput() -> list:
    input = open("input.txt", "r")
    linesGoodInput = []
    lineStr = 'obrigadoJoseSocrates'
    while lineStr != '':
        lineStr = input.readline()
        lineList = lineStr.split()
        if '\n' in lineList:
            lineList.remove('\n')
        linesGoodInput.append(lineList)
    input = linesGoodInput
    return input


def scoreCalculatorEachPlay(enemy: str, player: str) -> int:
    # A = X = 1 'Rock'
    # B = Y = 2 'Paper'
    # C = Z = 3 'Scisors'
    if enemy == 'A':
        enemy = 1
    if enemy == 'B':
        enemy = 2
    if enemy == 'C':
        enemy = 3
    if player == 'X':
        player = 1
    if player == 'Y':
        player = 2
    if player == 'Z':
        player = 3

    draw = 3
    win = 6
    lost = 0
    if enemy == player:
        return player + draw
    # enemy wins
    if ((enemy - player) == 1) or ((enemy - player) == -2):
        return player + lost
    # player wins
    if ((enemy - player) == 2) or ((enemy - player) == -1):
        return player + win


def scoreCalculator(input: list) -> int:
    score = 0
    for i in range(0, len(input)-1):
        score += scoreCalculatorEachPlay(input[i][0], input[i][1])
    return score


input = parseInput()
print(scoreCalculator(input))
