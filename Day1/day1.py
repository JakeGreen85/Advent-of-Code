# Day 1 of Advent of Code

def GetFile():
    # open input file given
    f = open("input.txt")
    fLines = f.readlines()

    # format input to remove "\n"
    for i in range(len(fLines)):
        if(fLines[i] != "\n"):
            fLines[i] = fLines[i][:-1]
    return fLines

def FormatList(list):
    # initialize lists
    values = []
    tempList = []

    # go through all the lines to separate each elf's backpack
    for i in range(len(list)):
        # if the current line is not an empty line, then add the line to a temporary list
        if(list[i] != "\n"):
            tempList.append(list[i])

        # if the current line is an empty line, then add the temporary list to the complete list of values
        else:
            values.append(tempList)
            tempList = [] # Reset the temporary list
    return values

def findHigh(values):
    # Go through each of the backpacks and add up all the values, to find the largest
    temp = 0
    high = 0
    index = 0
    for i in values:
        for j in i:
            temp += int(j)
        if(temp >= high):
            high = temp
            index = i
        temp = 0
    return high, index

def findTopThree(values):
    top3 = []
    # Use the previous function to find the highest values, remove it from 
    # the list, then find the highest from the new list, etc.
    for i in range(3):
        x, y = findHigh(values)
        top3.append(x)
        values.remove(y)
    return top3

def main():
    # Open the input file
    file = GetFile()
    # Save the formatted list
    list = FormatList(file)
    # Find the highest value and print to console
    print("High: " + str(findHigh(list)))
    # Find the top 3 values and print values and sum to console
    top3 = findTopThree(list)
    print("Top 3: " + str(top3))
    print("Sum of top 3: " + str(top3[0] + top3[1] + top3[2]))
    return

# call main
main()