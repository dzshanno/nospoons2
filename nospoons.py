# code for no more spoons episode 2
import sys
import math



class Game:
    '''Holds info on speciofic game'''
    pass

class grid:
    ''' holds info on specific game grid'''
    pass

class conn:
    ''' holds info on all connections'''
    # first cell
    # second cell
    # number of connections used - default = 0
    
    def __init__(self,cell1,cell2,used = 0):
        self.cell1 = cell1
        self.cell2 = cell2
        self.used = used

    def hor(self):
        '''checks to see if connection is horizontal'''
        if self.cell1.y == self.cell2.y:
            return True
        else :
            return False


class cell:
    ''' holds info on all cells'''
    # x pos
    # y pos
    # possible connections default = 2
    # required connections
    # enabled connections default = 0
    # list of connection objects
    def __init__(self,x,y,poss=2,req=0,enabled=0,conns=[]):
        self.x=x
        self.y=y
        self.poss=poss
        self.req=req
        self.enabled = enabled
        self.conns = conns

    def add_conn(self,conn):
        self.conns.append(conn)
        self.poss -= 1
        self.req -= 1
        self.enabled += 1

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
    for i in range(4,7):
        if cell[i][2]==0:

            cell[i][2] += 1
            cell[1] -= 1
            cell[2] -= 1
            cell[3] += 1

            
            add_target(cell[i])
            added_conn = True
            return added_conn
    for i in range(4,7):
        if cell[i][2]==1:

            cell[i][2] += 1
            cell[1] -= 1
            cell[2] -= 1
            cell[3] += 1
            add_target(cell[i][0])
            added_conn = True
            return added_conn


def find_certain(cells):
    another_loop = True
    while another_loop == True:
        for c in cells:
            another_loop = False
            if c[1] == c[2]:
                another_loop = True
                add_next_conn(c)



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
        if c.y ==  cell.y and c.x>cell.x:
            return c
    return ""

#find cell below
def cell_down(cells,cell):
    for c in cells:
        if c.x ==  cell.x and c.y>cell.y:
            return c
    return ""

def cell_up(cells,cell):
    for c in reversed(cells):
        if c.x ==  cell.x and c.y<cell.y:
            return c
    return ""

def cell_left(cells,cell):
    for c in reversed(cells):
        if c.y ==  cell.y and c.x<cell.x:
            return c
    return ""


# START OF GAME LOOP
# init values
    
cells = []
conns = []

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

# get the details of the grid
for r in range(height):
    line = input()  # width characters, each either a number or a '.'
    for c in range(width):
        if line[c] != ".":
            cells.append(cell([c,r],0,int(line[c]),0,[]))

# find neighbour cells - add to cell description and add to list of possible connectoins
for c in cells:
    cr = cell_right(cells,c)
    if cr:
        c.conns.append(conn(c,cr))
        c.poss += 2
    
    cd = cell_down(cells,c)
    if cd:
        c.conns.append(conn(c,cd))
        c.poss += 2

    cu = cell_up(cells,c)
    if cu:
        c.conns.append(conn(c,cu))
        c[1] += 2

    cl = cell_left(cells,c)
    if cl:
        c.conns.append(conn(c,cl))
        c[1] += 2

      
print("Debug messages...", file=sys.stderr, flush=True)
for c in cells:
    print(c, file=sys.stderr, flush=True)
for c in conns:
    print(c, file=sys.stderr, flush=True)
for t in target:
    print(t)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

