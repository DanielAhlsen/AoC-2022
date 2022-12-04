import sys

def checkOverlap(intervals):
    if intervals[0][1] < intervals[1][0] or intervals[1][1] < intervals[0][0]:
        return False
    else:
        return True

def checkContainment(intervals):
    if intervals[0][0] <= intervals[1][0] and \
            intervals[1][1] <= intervals[0][1]:
        return True
    elif intervals[1][0] <= intervals[0][0] and \
            intervals[0][1] <= intervals[1][1]:
        return True
    else:
        return False

def getInterval(pair):
    return (int(pair.split('-')[0]),int(pair.split('-')[1]))

def parseInput():
    filename = sys.argv[1]
    ranges = []
    with open(filename) as file:
        for line in file.readlines():
            stringIntervals = line.split(',')
            intervals = [getInterval(pair) for pair in stringIntervals]
            ranges.append(intervals)

    return ranges

def problem1(inputData):
    containment = map(checkContainment,inputData)
    numberOfTrues = sum(containment)
    print(f"Problem 1: {numberOfTrues}")

def problem2(inputData):
    overlaps = map(checkOverlap,inputData)
    numberOfTrues = sum(overlaps)
    print(f"Problem 2: {numberOfTrues}")

def main():
    inputData = parseInput()
    problem1(inputData)
    problem2(inputData)

if __name__ == "__main__":
    main()