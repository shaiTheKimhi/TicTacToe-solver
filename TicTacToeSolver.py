import sys
class TicTacToeSolver(object):
    """description of class
    
    board - a tic tac toe board where:
    1 - X
    0 - O
    -1- Empty
    default board is all empty
    Side is always X (1)
    """
    def __init__(self, side, board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]):
        self.board = board
        self.side = side

    #makes next oponent move and makes and returns the next player move to be activated
    #move- 2d tuple of indexes of next move
    def next_move(self, move):
        return self.search_vic(self.side)

    def search_vic(self, side):
        lost = True
        (w, los) = (0,0) #these are our (non definitive) winning options for possible stalemates and lossing options in general (both for -1 or for 0)
        best = [0,float('inf'),(0,0)] #wins loses and location of best drawing option
        moves = empty(self.board)
        if(moves == []): 
            me = win(self.board, side)
            en = win(self.board, op(side))
            if(me):
               return 1, None, None
            elif(en):
               return -1, None
            else:
               return 0, 0, 0
        for m in moves: #iterate over every operator possible from current state
            self.board[m[0]][m[1]] = side
            if(win(self.board, side)):
                self.board[m[0]][m[1]] = -1
                return 1, m, None
            else:
                res = self.search_vic(op(side))
                if(res[0] == 1): #means the oponent has won
                    los += 1
                elif(res[0] == -1): # means the oponent has definitely lost
                     self.board[m[0]][m[1]] = -1
                     return 1, m, None
                elif(res[0] == 0):
                     lost = False
                     w += res[2]
                     los += res[1]
                     if(w > best[0]):
                         best = [w, los, m]
                     elif(w == best[0] and los <= best[1]):
                         best = [w, los, m]
                
            self.board[m[0]][m[1]] = -1
        if(lost):
            return -1, None
        else:
            return 0, w, los, best

def op(side):
    return 0 if side else 1 


# returns a list of all empty spaces in the board
def empty(board):
    lst = [i for line in board for i in line]
    l = [(int(i/3), i%3) if lst[i] == -1 else (-1,-1) for i in range(len(lst))]
    return list(filter((-1,-1).__ne__, l))

# checks whether the board is a won one (final state)
# side - the side of the cheked winner, X by default
def win(board, side = 1):
    lst = [i for line in board for i in line]
    # for each i in [0,1,2] we will check if line i or column i is full
    for i in range(3):
        if((lst[i*3:i*3+3] == [side, side, side]) or (lst[i::3] == [side, side, side])):
            return True
    if (lst[: : 4] == [side, side, side] or lst[2: -2: 2] == [side, side, side]):
        return True
    return False



if (__name__ == '__main__'):
    print(sys.version_info)

    board = [[1,1,-1],[0,0,-1],[1,-1,-1]]
    T = TicTacToeSolver(1, board)
    #print(T.search_vic(1))
    #print(T.search_vic(0))

    #board = [[1,-1,-1],[-1,0,-1],[0,-1,1]]
    #T.board = board
    #print(T.search_vic(1))

    #T.board = [[1,-1,-1],[-1,-1,-1],[0,-1,-1]]

    #print(T.search_vic(1))
    #T.board[0][1] = 1
    #print(T.search_vic(0))

    T.board = [[1,0,-1],[-1,0,-1],[0,1,1]]
    print(T.search_vic(1))


    #play a full game
    #T.board = [[-1,-1,-1] for i in range(3)]
    #side = 1
    #res = T.search_vic(1)
    #while(res[0] != 1 and res[0] != -1):
    #    print(res)
    #    T.board[res[3][2][0]][res[3][2][1]] = side
    #    side = op(side)
    #    res = T.search_vic(side)
      

    
   # print(T.search_vic(1))
   
    debug = input() #empty operation for debug