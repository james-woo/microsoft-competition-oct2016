import os

"""
In this problem, we were given a file with numbers. The first number in the file represents the number of lines that follow (e.g. could be used to instantiate array size). The following rows are a bunch of numbers. In each row there's a bunch of numbers. First find the largest and the smallest numbers from these rows. The goal of this program is to find the missing numbers between that largest and smallest. For example, if a row contains: 
6 5 2 1
the output should have 3 4 (the missing numbers between 1 and 6)
If a row contains
4 2 1 3
the output should be a blank line as there are no missing numbers between 1 and 4. 
"""

arr = open("PracticeInput2a.txt").readlines()
#arr = open("input2.txt").readlines()

with open("output2.txt", "a") as myfile:
    for x in range(1, len(arr)):
        line = arr[x];
        numbers = line.replace('\n','').split(" ");
        firstNum = int(numbers[0]); 
        lastNum = int(numbers[-1]); 
        if ((lastNum-firstNum) == (len(numbers)-1)):
            #print " nothing for " + str(firstNum) + " to " + str(lastNum)
            myfile.write(" \n")
        else: #A number is missing 
            sortedLine = sorted(map(int, numbers));
            print sortedLine
            for y in range(1, len(sortedLine)):
                if not ((sortedLine[y]) == sortedLine[y-1]+1):
                    for i in (range(sortedLine[y-1]+1, sortedLine[y])):
                        myfile.write(str(i) + " ")
                        #print str(sortedLine[y]-1) + " ",
        #print "\n",
            myfile.seek(-1, os.SEEK_END)
            myfile.truncate()
            myfile.write("\n")
            