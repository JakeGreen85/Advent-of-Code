# Day 2 of Advent of Code

# GLOBAL VARIABLES
ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6

def GetFile(input):
    # open input file given
    f = open(input)
    fLines = f.readlines()

    # format input to remove "\n"
    for i in range(len(fLines)):
        fLines[i] = fLines[i][:-1]
    return fLines

def FormatInput(input):
    result = []
    for x in range(len(input)):
        result.append([input[x][0], input[x][-1]])
    return result

# Functions for part 1 of day 2

def FormatStrings(str):
    if(str == "X" or str == "A"):
        return "ROCK"
    elif(str == "Y" or str == "B"):
        return "PAPER"
    else:
        return "SCISSORS"


def CalculateScore(list):
    total = 0
    for x in list:
        result = CheckResult(FormatStrings(x[1]), FormatStrings(x[0]))
        total += result
    return total

def CheckResult(pInput, eInput):
    if(eInput == "ROCK"):          # ROCK
        if(pInput == "ROCK"):      # ROCK
            return DRAW + ROCK
        elif(pInput == "PAPER"):    # PAPER
            return WIN + PAPER
        else:                   # SCISSORS
            return LOSS + SCISSORS
    elif(eInput == "PAPER"):        #PAPER
        if(pInput == "ROCK"):      #ROCK
            return LOSS + 1
        elif(pInput == "PAPER"):    # PAPER
            return DRAW + PAPER
        else:                   # SCISSORS
            return WIN + SCISSORS
    else:                       # SCISSORS
        if(pInput == "ROCK"):      # ROCK
            return WIN + 1
        elif(pInput == "PAPER"):    # PAPER
            return LOSS + PAPER
        else:                   # SCISSORS
            return DRAW + SCISSORS

# Functions for part 2 of day 2

def FormatStrings2(str):
    if(str == "X"):
        return "lose"
    elif(str == "Y"):
        return "draw"
    else:
        return "win"

def CheckResult2(pInput, eInput):
    if(pInput == "win"):
        if(eInput == "ROCK"):
            return WIN + PAPER
        elif(eInput == "PAPER"):
            return WIN + SCISSORS
        else:
            return WIN + ROCK
    elif(pInput == "draw"):
        if(eInput == "ROCK"):
            return DRAW + ROCK
        elif(eInput == "PAPER"):
            return DRAW + PAPER
        else:
            return DRAW + SCISSORS
    else:
        if(eInput == "ROCK"):
            return LOSS + SCISSORS
        elif(eInput == "PAPER"):
            return LOSS + ROCK
        else:
            return LOSS + PAPER

def CalculateScore2(list):
    total = 0
    for x in list:
        input1 = FormatStrings(x[0])
        input2 = FormatStrings2(x[1])
        total += CheckResult2(input2, input1)
    return total


def main():
    # open file
    fLines = GetFile("input.txt")

    # format list
    list = FormatInput(fLines)

    # Calculate total score (Part 1)
    total = CalculateScore(list)
    print("Total Score (Part 1): " + str(total))

    # Calculate total score (Part 2)
    total2 = CalculateScore2(list)
    print("Total Score (Part 2): " + str(total2))

# call main
main()