# Day 3 of Advent of Code

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.swapcase()

def GetFile(input):
    # open input file given
    f = open(input)
    fLines = f.readlines()

    # format input to remove "\n"
    for i in range(len(fLines)):
        fLines[i] = fLines[i][:-1]
    return fLines

def SplitCompartments(input):
    newList = []
    for x in input:
        newList.append([x[:int(len(x)/2)], x[int(len(x)/2):]])
    return newList

def SplitGroups(input):
    newList = []
    tempList = []
    for x in range(len(input)):
        tempList.append(input[x])
        if(len(tempList) == 3):
            newList.append(tempList)
            tempList = []
    return newList

def CheckDuplicates(list):
    total = 0
    for x in list:
        for y in range(len(x[0])):
            if x[0][y] in x[1]:
                total += ConvertToPriority(x[0][y])
                break
    return total

def ConvertToPriority(str):
    priority = 0
    for a in range(len(lowercase)):
        if(str == lowercase[a]):
            priority = a + 1
    for b in range(len(uppercase)):
        if(str == uppercase[b]):
            priority = b + 27
    return priority

def CheckGroupBadge(list):
    total = 0
    for x in list:
        for y in range(len(x[0])):
            if x[0][y] in x[1] and x[0][y] in x[2]:
                total += ConvertToPriority(x[0][y])
                break
    return total

def main():
    file = GetFile("input.txt")
    list = SplitCompartments(file)
    result = CheckDuplicates(file)
    print("Total Priority of Duplicates: " + str(result))
    list2 = SplitGroups(file)
    result2 = CheckGroupBadge(list2)
    print("Total Priority of Groups: " + str(result2))

main()