# code for no more spoons episode 2
import sys
import math


class game:
    '''Holds info on specific game'''

    # find a the first cell to the right
    def cell_right(self,allcells,startcell):
        for c in allcells:
            if c.y ==  startcell.y and c.x>startcell.x:
                return c
        return ""

    #find the first cell below
    def cell_down(self,allcells,startcell):
        for c in allcells:
            if c.x ==  startcell.x and c.y>startcell.y:
                return c
        return ""

    #find the first cell above
    def cell_up(self,allcells,startcell):
        for c in reversed(allcells):
            if c.x ==  startcell.x and c.y<startcell.y:
                return c
        return ""
    #find the first cell left
    def cell_left(self,allcells,startcell):
        for c in reversed(allcells):
            if c.y ==  startcell.y and c.x<startcell.x:
                return c
        return ""

    
    # creates the initial game state
    def __init__(self):
        
        self.w = int(input())  # the number of cells on the X axis
        self.h = int(input())  # the number of cells on the Y axis
        self.states = []


        # get the details of the initial grid
        initial_state = state(0,[])
        self.states.append(initial_state)
        for row in range(self.h):
            line = input()  # width characters, each either a number or a '.'
            for col in range(self.w):
                if line[col] != ".":
                    new_cell = cell()
                    new_cell.x = col
                    new_cell.y = row
                    new_cell.poss = 0
                    new_cell.req = int(line[col])
                    new_cell.enabled = 0
                    new_cell.conns = []
                    initial_state.cells.append(new_cell)

        
        # find neighbour cells - add to cell description and add to list of possible connectoins
        for c in initial_state.cells:
            cr = self.cell_right(initial_state.cells,c)
            if cr:
                c.conns.append(conn(c,cr,initial_state.cells))
            
            cd = self.cell_down(initial_state.cells,c)
            if cd:
                c.conns.append(conn(c,cd,initial_state.cells))

            cu = self.cell_up(initial_state.cells,c)
            if cu:
                c.conns.append(conn(c,cu,initial_state.cells))

            cl = self.cell_left(initial_state.cells,c)
            if cl:
                c.conns.append(conn(c,cl,initial_state.cells))

        

    def final_output(self):
        output = []
        for c in self.states[-1].cells:
            for con in c.conns:
                if con.used != 0:
                    # add conn in output format to the output list
                    output.append(con.output(con.used))
        # dedupe the output list
        output = list(dict.fromkeys(output))
        for o in output:
            print(str(o))

                    
                

class state:
    ''' holds info on specific game state'''
    def __init__(self,move=0,added = []):
        self.move = move
        self.cells = []
        self.added = added

    def __str__ (self):
        return "test5"

    def remaining(self):
        still_required = 0
        for c in self.cells:
            still_required += c.req
        return still_required
    
    def format_target(conn,weight = 1):
        target = str(conn.cell1.x)+" "+str(conn.cell1.y)+" "+str(conn.cell2.x)+" "+str(conn.cell2.y)+ " "+str(weight)
        return target


    # given that a connection is certain return the conn object for the next best connection or False if none are possible
    def find_next_conn(self,cell):
    
        if cell.poss == 0:
            return False
        
        for con in cell.conns:
            print("checking con "+str(con), file = sys.stderr, flush=True)
            print("used = "+str(con.used),file = sys.stderr, flush = True)
            if con.used == 0:
                con.used += 1
                
                con.cell1.poss -= 1
                con.cell1.req -= 1
                con.cell1.enabled += 1

                con.cell2.poss -= 1
                con.cell2.req -= 1
                con.cell2.enabled += 1
    
                return con
            
        for con in cell.conns:
            if con.used == 1:
                con.used += 1
                
                con.cell1.poss -= 1
                con.cell1.req -= 1
                con.cell1.enabled += 1

                con.cell2.poss -= 1
                con.cell2.req -= 1
                con.cell2.enabled += 1
                
                return con
    
        return False
    # return the next best conn for the next cell with a certain conn or if none are certain return false
    def find_certain_conn(self):
        for c in self.cells:
            unique = 0
            for con in c.conns:
                if con.used<2:
                    unique +=1

            print(c, file=sys.stderr, flush=True)
            print(unique, file = sys.stderr, flush=True)
            if c.req == c.poss and c.req != 0: 
                print("req=poss", file = sys.stderr, flush=True)
                return self.find_next_conn(c)
            if c.req == 1 and unique == 1:
                print("1 and 1", file = sys.stderr, flush=True)
                return self.find_next_conn(c)
            if c.req == 2 and unique == 1:
                print("2 and 1", file = sys.stderr, flush=True)
                return self.find_next_conn(c)
            if c.req == 3 and unique == 2:
                return self.find_next_conn(c)
            if c.req == 5 and unique == 3:
                return self.find_next_conn(c)
            if c.req == 6 and unique == 4:
                return self.find_next_conn(c)
            if c.req == 7 and unique == 4:
                return self.find_next_conn(c)
        
        return False
    
    def find_certain_conns(self):
        while self.find_certain_conn():
            print (self.find_certain_conn().output(1))
        print("no more certainties)", file=sys.stderr,flush = True)


class conn:
    ''' holds info on all connections'''
    # first cell
    # second cell
    # number of connections used - default = 0
    
    def __init__(self,cell1,cell2,cells,used = 0):
        self.cell1 = cell1
        self.cell2 = cell2
        self.used = used
        for c in cells:
            if c.x == cell1.x and c.y==cell1.y:
                c.poss += 1
            if c.x == cell2.x and c.y==cell2.y:
                c.poss += 1
    
    def __str__(self):
        output = str(self.cell1.x)+" "+str(self.cell1.y)+" "+str(self.cell2.x)+" "+str(self.cell2.y)
        return output
    
    def __repr__(str):
        return "test2"

    def hor(self):
        '''checks to see if connection is horizontal'''
        if self.cell1.y == self.cell2.y:
            return True
        else :
            return False
        
    def output(self, weight):
        return str(self)+" "+str(weight)



class cell:
    ''' holds info on all cells'''
    # x pos
    # y pos
    # possible connections default = 0
    # required connections default = 0
    # enabled connections default = 0
    # list of connection objects
    def __init__(self,x = -1,y = -1,poss=0,req=0,enabled=0,conns=[]):
        self.x=x
        self.y=y
        self.poss=poss
        self.req=req
        self.enabled = enabled
        self.conns = conns

    def __str__(self):
        output = str(self.x) + "," + str(self.y) + " Poss: "+str(self.poss)
        for con in self.conns:
            if con.cell1 == self:
                output += "-> " + str(con.cell2.x) + "," + str(con.cell2.y)
            else:
                output += " " + str(con.cell1.x) + "," + str(con.cell1.y)
        output += " Req:" + str(self.req)
        return output
    
    def __repr__(str):
        return "test4"

    def enable_conn(self,conn):
        self.conns.append(conn)
        self.poss -= 1
        self.req -= 1
        self.enabled += 1


# START OF GAME LOOP
# init values
new_game = game()
cc = new_game.states[0].find_certain_conns()
new_game.final_output()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

