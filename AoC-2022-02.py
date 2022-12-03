import sys
from functools import reduce

payoffs = {
    ('A','X') : 4,
    ('A','Y') : 8,
    ('A','Z') : 3,
    ('B','X') : 1,
    ('B','Y') : 5,
    ('B','Z') : 9,
    ('C','X') : 7,
    ('C','Y') : 2,
    ('C','Z') : 6
}

strategy = {
    ('A','X') : ('A','Z'),
    ('A','Y') : ('A','X'),
    ('A','Z') : ('A','Y'),
    ('B','X') : ('B','X'),
    ('B','Y') : ('B','Y'),
    ('B','Z') : ('B','Z'),
    ('C','X') : ('C','Y'),
    ('C','Y') : ('C','Z'),
    ('C','Z') : ('C','X')
}

def getPlays(filename):
    plays = []
    with open(filename) as f:
        for line in f.readlines():
            plays.append(tuple(line.split()))
    return plays

def getNewPlay(play):
    return strategy[play]

def getScore(play):
    return payoffs[play]

def problem1(plays):
    totalScore = sum([ getScore(play) for play in plays])
    print(f'Problem 1: {totalScore}')

def problem2(plays):
    totalScore = sum([ getScore(getNewPlay(play)) for play in plays])
    print(f'Problem 2: {totalScore}')

def main():
    filename = sys.argv[1]
    plays = getPlays(filename)
    problem1(plays)
    problem2(plays)

if __name__ == "__main__":
    main()