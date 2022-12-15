import sys
from itertools import product

def parseInput(filename):
    with open(filename) as file:
        return [ [ int(ch) for ch in line.strip()] 
                        for line in file.readlines() ]

def problem1(trees):
    height = len(trees)
    width = len(trees[0])
    count = 0

    for y,x in product(range(1,height-1),range(1,width-1)):
        treeHeight = trees[y][x]
        visible = [True,True,True,True]
        for z in range(y):
            if trees[z][x] >= treeHeight:
                visible[0] = False
                break
        
        if visible[0]:
            count += 1
            continue

        for z in range(height-y-1):
            if trees[height-z-1][x] >= treeHeight:
                visible[1] = False
                break

        if visible[1]:
            count += 1
            continue

        for z in range(x):
            if trees[y][z] >= treeHeight:
                visible[2] = False
                break

        if visible[2]:
            count += 1
            continue

        for z in range(width-x-1):
            if trees[y][width-z-1] >= treeHeight:
                visible[3] = False
                break

        if visible[3]:
            count += 1
    
    count += 2*(width+height)-4
    print(f"Problem 1: {count}")

def problem2(trees):
    height = len(trees)
    width = len(trees[0])
    maximum = 1
    
    for y,x in product(range(height)[1:-1],range(width)[1:-1]):
        score = 1
        treeHeight = trees[y][x]
        
        #go north
        i = y-1
        factor = 1
        while i >= 0:
            if treeHeight <= trees[i][x] or i == 0:
                break
            i -= 1
            factor += 1

        score *= factor

        #go south
        i = y+1
        factor = 1
        while i <= height-1:
            if treeHeight <= trees[i][x] or i == height-1:
                break
            i += 1
            factor += 1

        score *= factor

        #go west
        i = x-1
        factor = 1
        while i >= 0:
            if treeHeight <= trees[y][i] or i == 0:
                break
            i -= 1
            factor += 1

        score *= factor

        #go east
        i = x+1
        factor = 1
        while i <= width-1:
            if treeHeight <= trees[y][i] or i == width-1:
                break
            i += 1
            factor += 1

        score *= factor

        if score > maximum:
            maximum = score
        
        score = 1
    
    print(f"Problem 2: {maximum}")

def main():
    filename = "/home/voodoo/Documents/AoC/Advent of code solutions/inputs/input-08.txt"
    trees = parseInput(filename)
    problem1(trees)
    problem2(trees)

if __name__ == "__main__":
    main()