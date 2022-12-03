import sys
from itertools import zip_longest
from functools import reduce

def getBadgeFromGroup(rucksacks):
    uniqueRucksacks = map(getUniqueItems,rucksacks)
    intersection = lambda x,y : x.intersection(y)
    badge = reduce(intersection,uniqueRucksacks)
    return badge

def getPrioritySum(setOfItems):
    return sum([getPriority(item) for item in setOfItems])

def getPriority(item):
    if item.islower():
        return ord(item)-ord('a')+1
    elif item.isupper():
        return ord(item)-ord('A')+27
    else:
        return 0

def getUniqueItems(rucksackItems):
    return set(rucksackItems)

def getDuplicateItems(rucksackItems):
    noItems = len(rucksackItems)
    compartment1 = getUniqueItems(rucksackItems[:noItems//2])
    compartment2 = getUniqueItems(rucksackItems[noItems//2:])
    duplicates = compartment1.intersection(compartment2)
    return duplicates


def getRucksackItems(filename):
    rucksacks = []
    with open(filename) as f:
        for line in f.readlines():
            rucksacks.append(line.strip())
    return rucksacks

def problem1(rucksacks):
    duplicates = map(getDuplicateItems,rucksacks)
    prioritySum = map(getPrioritySum,duplicates)
    totalPriority = sum(prioritySum)
    print(f'Problem 1: {totalPriority}')

def problem2(rucksacks):
    groups = zip_longest(*(iter(rucksacks),) * 3)
    badges = map(getBadgeFromGroup,groups)
    prioritySum = map(getPrioritySum,badges)
    totalPriority = sum(prioritySum)
    print(f'Problem 2: {totalPriority}')

def main():
    filename = sys.argv[1]
    rucksacks = getRucksackItems(filename)
    problem1(rucksacks)
    problem2(rucksacks)

if __name__ == "__main__":
    main()