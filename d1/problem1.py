def read_input(filename: str) -> list:
    with open(filename) as f:
        lines = f.readlines()
        lineStripped = [i.replace('\n', '') for i in lines]
        listOfElfs = []
        listElfFood = []

        for i in lineStripped:
            if i != '':
                listElfFood.append(int(i))
            if i == '':
                listOfElfs.append(listElfFood)
                listElfFood = []

        listOfElfs.sort(key=sum)
    return sum(listOfElfs[-1])

print(read_input('input1.txt'))