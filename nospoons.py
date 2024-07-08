# code for no more spoons episode 2
import sys
import math

cells =[]

# init values

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

# get the details of the grid
for r in range(height):
    line = input()  # width characters, each either a number or a '.'
    for c in range(width):
        if line[c] != ".":
            cells.append([r,c])
        
print("Debug messages...", file=sys.stderr, flush=True)
print(cells, file=sys.stderr, flush=True) 

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Two coordinates and one integer: a node, one of its neighbors, the number of links connecting them.
print("0 0 2 0 1")
