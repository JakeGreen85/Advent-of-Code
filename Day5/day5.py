# Day 4 of Advent of Code

TESTINPUT = "testInput.txt"
INPUT = "input.txt"

stack1=["T", "P", "Z", "C", "S", "L", "Q", "N"]
stack2=["L", "P", "T", "V", "H", "C", "G"]
stack3=["D", "C", "Z", "F"]
stack4=["G", "W", "T", "D", "L", "M", "V", "C"]
stack5=["P", "W", "C"]
stack6=["P", "F", "J", "D", "C", "T", "S", "Z"]
stack7=["V", "W", "G", "B", "D"]
stack8=["N", "J", "S", "Q", "H", "W"]
stack9=["R", "C", "Q", "F", "S", "L", "V"]
stacks=[stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

def GetFile(input):
    # open input file given
    f = open(input)
    fLines = f.readlines()

    # format input to remove "\n"
    for i in range(len(fLines)):
        fLines[i] = fLines[i][:-1]

    return fLines

def FormatInput(fLines):
    fromIndex = []
    toIndex = []
    moveAmt = []
    str = ""
    for x in range(len(fLines)):
        print(fLines[x])
        if(fLines[x][6] != " "):
            moveAmt.append(int(fLines[x][5] + fLines[x][6]))
            fromIndex.append(int(fLines[x][13]))
            toIndex.append(int(fLines[x][len(fLines[x])-1]))
        else:
            moveAmt.append(int(fLines[x][5]))
            fromIndex.append(int(fLines[x][12]))
            toIndex.append(int(fLines[x][len(fLines[x])-1]))
    return moveAmt, fromIndex, toIndex

def Move(amtList, fromList, toList):
    return 0

def main():
    fLines = GetFile(TESTINPUT)
    amtList, fromList, toList = FormatInput(fLines)
    print(amtList, fromList, toList)
    result = Move(amtList, fromList, toList)
    print("Overlaps: " + str(result))


main()