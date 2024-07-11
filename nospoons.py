# code for no more spoons episode 2
import sys
import math

# cells holds [grid position,
#              conns possible, 
#              conns needed,
#              conns applied,
#              north conn,
#              east conn,
#              south conn,
#              west conn]
cells =[]

# conns holds   [[x1,y1],
#                [x2,y2],
#                used -1 for not available] order so x1,y1 is left and/or up from x2,y2
conns = []

target =[]
def add_target(conn):
    target.append(str(conn[0][0])+" "+
                                str(conn[0][1])+" "+
                                str(conn[1][0])+" "+
                                str(conn[1][1])+ " "+
                                "1")
    return True


def add_next_conn(cell):
    added_conn = False
    if cell[1] == 0:
        return added_conn
    for i in range(4,reversed):
        if cell[i][2]==0:

            cell[i][2] += 1
            cell[1] -= 1
            cell[2] -= 1
            cell[3] += 1
            add_target(cell[i])
            added_conn = True
            return added_conn
    for i in range(4,reversed):
        if cell[i][2]==1:

            cell[i][2] += 1
            cell[1] -= 1
            cell[2] -= 1
            cell[3] += 1
            add_target(cell[i][0])
            added_conn = True
            return added_conn



# if there is one possible and one needed enable that connection
def case1 (cells,conns):
    changed = False
    for c in cells:
        if c[1]== c[2]:
            for con in conns:
                if con[0] == c[0] and con [2] == False:
                    con[2] = True
                    c[1] -= 1
                    c[3] += 1
                    target.append(str(con[0][0])+" "+
                                str(con[0][1])+" "+
                                str(con[1][0])+" "+
                                str(con[1][1])+ " "+
                                "1")
                    changed = True
                    break
                if con[1] == c[0] and con [2] == False:
                    con[2] = True
                    for d in cells:
                        if d[0] == con [1]:
                            d[1] -= 1
                            d[3] += 1
                            target.append(str(con[0][0])+" "+
                                str(con[0][1])+" "+
                                str(con[1][0])+" "+
                                str(con[1][1])+ " "+
                                "1")
                            changed = True
                            break
    return changed



# find a cell to the right
def cell_right(cells,cell):
    for c in cells:
        if c[0][1] ==  cell[0][1] and c[0][0]>cell[0][0]:
            return c[0]
    return ""

#find cell below
def cell_down(cells,cell):
    for c in cells:
        if c[0][0] ==  cell[0][0] and c[0][1]>cell[0][1]:
            return c[0]
    return ""

def cell_up(cells,cell):
    for c in reversed(cells):
        if c[0][0] ==  cell[0][0] and c[0][1]<cell[0][1]:
            return c[0]
    return ""

def cell_left(cells,cell):
    for c in reversed(cells):
        if c[0][1] ==  cell[0][1] and c[0][0]<cell[0][0]:
            return c[0]
    return ""


def no_choice(cell):
    print

# init values

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

# get the details of the grid
for r in range(height):
    line = input()  # width characters, each either a number or a '.'
    for c in range(width):
        if line[c] != ".":
            cells.append([[c,r],0,int(line[c]),0,"","","",""])

# find neighbour cells - add to cell description and add to list of possible connectoins
for c in cells:
    cr = cell_right(cells,c)
    if cr:
        c[4] = cr
        c[1] += 2
        conns.append([c[0],cr,False])
    
    cd = cell_down(cells,c)
    if cd:
        c[5] = cd
        c[1] += 2
        conns.append([c[0],cd,False])

    cu = cell_up(cells,c)
    if cu:
        c[6] = cu
        c[1] += 2
        conns.append([cu,c[0],False])

    cl = cell_left(cells,c)
    if cl:
        c[7] = cl
        c[1] += 2
        conns.append([cl,c[0],False])

case1(cells,conns)       
print("Debug messages...", file=sys.stderr, flush=True)
for c in cells:
    print(c, file=sys.stderr, flush=True)
for c in conns:
    print(c, file=sys.stderr, flush=True)
for t in target:
    print(t)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

