import os

#input = "red purple green orange purple purple orange yellow yellow yellow" 
input = "blue blue yellow orange orange green green green blue blue purple red red orange orange purple green yellow red red yellow orange orange green purple purple purple purple green orange red yellow yellow blue blue yellow yellow yellow orange purple green yellow blue purple purple blue red purple green orange red yellow yellow blue purple purple blue yellow green green yellow red purple green green blue red orange yellow blue blue red purple blue yellow yellow red red yellow green purple purple green orange orange orange orange yellow yellow green green yellow red purple blue red red red red blank"

#open("PracticeInput2a.txt").readlines()
#arr = open("input2.txt").readlines()

inputArr = input.split(' ');

dict = \
{'red': ['blank','red'], 'yellow': ['blank','yellow'],'blue': ['blank','blue'],\
 'purple':['red','blue'], 'orange':['red','yellow'], 'green':['yellow','blue']}

outputArr = []
outputArr.append(inputArr[0])
print inputArr[0] + " ",
for i in range(1, len(inputArr)-1):  
    possibleValues = dict[inputArr[i]]
    print "Checking.... "  + str(inputArr[i]) + " with possibilities of ",
    print possibleValues;
    if (outputArr[-1] == possibleValues[0]):
        print possibleValues[1] + " ",
        outputArr.append(possibleValues[1])
    else:
        print possibleValues[0] + " ",
        outputArr.append(possibleValues[0])
        
print inputArr[-1];

print '-------------------------'
with open("output2.txt", "a") as myfile:
    for color in outputArr:
        print color + " ",
        myfile.write(color + " ")

#red blue yellow red blue red yellow blank yellow