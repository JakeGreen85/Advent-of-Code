# Day 4 of Advent of Code

TESTINPUT = "testInput.txt"
INPUT = "input.txt"

def GetFile(input):
    # open input file given
    f = open(input)
    fLines = f.readlines()

    # format input to remove "\n"
    for i in range(len(fLines)):
        fLines[i] = fLines[i][:-1]

    return fLines

def FormatInput(fLines):
    list = []
    tempList = []
    str = ""
    for x in range(len(fLines)):
        for y in range(len(fLines[x])):
            if(fLines[x][y] != "," and fLines[x][y] != "-"):
                str += fLines[x][y]
            else:
                tempList.append(str)
                str = ""
        tempList.append(str)
        list.append(tempList)
        tempList = []
        str = ""
    return list

def CompareList(list):
    overlaps = 0

    for x in list:
        if (int(x[0]) <= int(x[2])) and (int(x[1]) >= int(x[3])):
            overlaps += 1
        elif (int(x[0]) >= int(x[2])) and (int(x[1]) <= int(x[3])):
            overlaps += 1

    return overlaps

def RangeOverlap(list):
    overlaps = 0
    for x in list:
        if(int(x[0]) >= int(x[2]) and int(x[0]) <= int(x[3])):
            overlaps += 1
        elif(int(x[1]) >= int(x[2]) and int(x[1]) <= int(x[3])):
            overlaps += 1
        elif(int(x[2]) >= int(x[0]) and int(x[2]) <= int(x[1])):
            overlaps += 1
        elif(int(x[3]) >= int(x[0]) and int(x[3]) <= int(x[1])):
            overlaps += 1
    return overlaps


def main():
    fLines = GetFile(INPUT)
    list = FormatInput(fLines)
    result = CompareList(list)
    print("Part 1: Overlaps: " + str(result))
    result2 = RangeOverlap(list)
    print("Part 2: Range Overlaps: " + str(result2))


main()