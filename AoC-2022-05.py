import sys

def parseInstruction(string):
    contents = string.replace(" ",",").split(",")
    return (int(contents[1]),int(contents[3]),int(contents[5]))

def parseCrateString(string,size):
    if len(string) != 4*size-1:
        string += " "*(4*size-1-len(string))
    contents = []
    for char in string[1:-1:4]:
        if char == " ":
            contents.append(None)
        else:
            contents.append(char)
    return contents

def parseStackString(string):
    return [int(x) for x in string.split() ]

def getSetupString(file):
    strings = []
    while True:
        line = file.readline()
        if line == "\n" or not line:
            break
        else:
            strings.insert(0,line)
    return strings

def parseInput(filename):
    with open(filename) as file:
        setup = getSetupString(file)
        stacks = { i : [] for i in parseStackString(setup[0])}
        size = len(stacks)
        for line in setup[1:]:
            crates = parseCrateString(line,size)
            for stack,crate in zip(stacks,crates):
                if crate:
                    stacks[stack].append(crate)
        
        instructions = []
        for line in file.readlines():
            instructions.append(parseInstruction(line))
        
        return stacks, instructions
        

def problem1(stacks, instructions):
    for command in instructions:
        n = command[0]
        source = command[1]
        target = command[2]
        for _ in range(n):
            crate = stacks[source].pop()
            stacks[target].append(crate)
    
    message = ""
    for stack in stacks.values():
        message += stack[-1]
    
    print(f"Problem 1: {message}")

def problem2(stacks, instructions):
    for command in instructions:
        source = command[1]
        target = command[2]
        n = len(stacks[source])-command[0]
        for _ in range(command[0]):
            stacks[target].append(stacks[source][n])
            stacks[source].pop(n)
    
    message = ""
    for stack in stacks.values():
        if stack:
            message += stack[-1]
    
    print(f"Problem 2: {message}")

def main():
    filename = sys.argv[1]
    stacks, instructions = parseInput(filename)
    problem1(stacks, instructions)
    stacks, instructions = parseInput(filename)
    problem2(stacks, instructions)

if __name__ == "__main__":
    main()