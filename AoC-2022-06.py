import sys

def findMarker(inputData,n):
    datalength = len(inputData)
    if datalength < n:
        return -2
    
    index = n
    characters = list(inputData[0:index])
    distinct = areDistinct(characters)
    while not distinct and index < datalength:
        characters[index % n] = inputData[index]
        distinct = areDistinct(characters)
        index += 1

    if not distinct:
        return -1
    else:
        return index


def areDistinct(container):
    return len(container) == len(set(container))

def parseInput(filename):
    with open(filename) as file:
        return file.readline()

def problem1(inputData,n):
    index = findMarker(inputData,n)
    if index == -1:
        print("Problem 1: Could not find start marker.")
    elif index == -2:
        print("Problem 1: Data stream too short for marker.")
    else:
        print(f"Problem 1: {index}")

def problem2(inputData,n):
    index = findMarker(inputData,n)
    if index == -1:
        print("Problem 2: Could not find start marker.")
    elif index == -2:
        print("Problem 2: Data stream too short for marker.")
    else:
        print(f"Problem 2: {index}")

def main():
    filename = sys.argv[1]
    n1 = 4
    n2 = 14
    inputData = parseInput(filename)
    problem1(inputData,n1)
    problem2(inputData,n2)

if __name__ == "__main__":
    main()