import os

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
            