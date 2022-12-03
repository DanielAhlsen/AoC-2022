import sys

def getToplist(values, toplistLength):
    length = min(toplistLength,len(values))
    toplist = { index : values[index] for index in range(length)}

    for index, value in enumerate(values[length:]):
        if any([entry < value for entry in toplist.values()]):
            smallest_entry = min(toplist, key=toplist.get)
            del toplist[smallest_entry]
            toplist[index+length-1] = value
                    
    return toplist

def getListOfValues(filename):
    values = []
    current_value = 0
    with open(filename) as file:
        for line in file.readlines():
            if line != "\n":
                current_value += int(line)
            else:
                values.append(current_value)
                current_value = 0

    values.append(current_value)
    return values

def problem1(values):
    print(f'Problem 1: {max(values)}')

def problem2(values,toplistLength):
    toplist = getToplist(values,toplistLength)
    print(f'Problem 2: {sum(toplist.values())}')

def main():
    filename = sys.argv[1]
    length = int(sys.argv[2])
    values = getListOfValues(filename)
    problem1(values)
    problem2(values,length)

if __name__ == "__main__":
    main()