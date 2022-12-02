# A = Rock    X = Rock
# B = Paper   Y = Paper
# C = Scisors Z = Scisors

def parseInput() -> list:
    input = open("input.txt", "r")
    linesGoodInput = []
    lineStr = '_'
    while lineStr != '':
        lineStr = input.readline()
        lineList = lineStr.split()
        if '\n' in lineList:
            lineList.remove('\n')
        linesGoodInput.append(lineList)
    input = linesGoodInput
    return input


def scoreCalculatorEachPlay(enemy: str, player: str) -> int:
    # A = 1 'Rock'
    # B = 2 'Paper'
    # C = 3 'Scisors'
    # X = lose
    # Y = draw
    # Z = win
    if enemy == 'A':
        enemy = 1
    if enemy == 'B':
        enemy = 2
    if enemy == 'C':
        enemy = 3
    if player == 'X':
        player = 0
    if player == 'Y':
        player = 3
    if player == 'Z':
        player = 6

    draw = 3
    win = 6
    lost = 0
    if player == draw:
        return enemy + draw
    # enemy wins
    if player == lost and enemy == 1:
        return 3 + lost
    if player == lost and enemy == 2:
        return 1 + lost
    if player == lost and enemy == 3:
        return 2 + lost
    # player wins
    if player == win and enemy == 1:
        return 2 + win
    if player == win and enemy == 2:
        return 3 + win
    if player == win and enemy == 3:
        return 1 + win


def scoreCalculator(input: list) -> int:
    score = 0
    for i in range(0, len(input)-1):
        score += scoreCalculatorEachPlay(input[i][0], input[i][1])
    return score


input = parseInput()
print(scoreCalculator(input))
