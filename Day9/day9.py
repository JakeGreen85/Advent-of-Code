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
        print(x)
        print(x[0])
        print(x[1])
        print(x[2])
        print(x[3])
        if x[0] <= x[2]:
            if x[1] >= x[3]:
                overlaps += 1
                continue
        if(x[0] >= x[2]):
            if x[1] <= x[3]:
                overlaps += 1
                continue

    return overlaps

def main():
    fLines = GetFile(TESTINPUT)
    list = FormatInput(fLines)
    print(list[0])
    result = CompareList(list)
    print("Overlaps: " + str(result))


main()