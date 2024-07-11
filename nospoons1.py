import sys
import math
cells = []
output = ""
line = ""
rightoutput=""
belowoutput=""
# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()# width characters, each either 0 or .
    cells.append(list(line))


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#scan each cell#
for rows in range(height):
    for cols in range(width):
        if cells[rows][cols]=="0":
            print("found node "+ str(cols)+" "+str(rows), file=sys.stderr, flush=True)
            output=str(cols) + " " + str(rows)
            
        # find node to the right
            rightoutput="-1 -1"
            for right in range(cols+1,width):
                if cells[rows][right]=="0":
                    print("found right neighbour"+ str(right)+" "+str(rows), file=sys.stderr, flush=True)
                    rightoutput=str(right) + " "+ str(rows)
                    break
                    
            output=output +" "+rightoutput

        #find row below
            belowoutput="-1 -1"
            for below in range(rows+1,height):
                if cells[below][cols]=="0":
                    print("found below neighbour"+ str(cols)+" "+str(below), file=sys.stderr, flush=True)
                    belowoutput=str(cols) + " "+ str(below)
                    break
                
            output = output + " " + belowoutput

            print(output)
    
# Three coordinates: a node, its right neighbor, its bottom neighbor

