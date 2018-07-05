import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--piece", help="enter Knight, Queen, Rook, or Bishop")
parser.add_argument("--position", help="enter alpha a-h and index 1-8. Ex:) d4")
args = parser.parse_args()
horizontals = [(1,0),(0,1),(-1,0),(0,-1)]
diagonals = [(1,1),(-1,1),(1,-1),(-1,-1)]
knightMoves = [[1,-2], [2,-1], [2,1], [1,2], [-1,2], [-2,1], [-2,-1], [-1,-2]]
chessBoard = [[1] * 8 for i in range(8)]

map_alpha_to_index = {
   "a" : 0,
   "b" : 1,
   "c" : 2,
   "d" : 3,
   "e" : 4,
   "f" : 5,
   "g" : 6,
   "h" : 7
}

map_index_to_alpha = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h"
}

class Piece:
    def __init__(self, moveSet, position):
        self.moveSet = moveSet
        self.position = position
        self.potentialMoves = []
        c, r = list(position.strip().lower())
        self.row = int(r) - 1
        self.column = map_alpha_to_index[c]

    def enumerateMoves(self,chessBoard):
        print("Please specify a piece")

    def isInBounds(self,x,y):
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    def runRise(self, chessBoard):
        i,j = self.row, self.column
        self.potentialMoves = []
        for xInt, yInt in self.moveSet:
            run, rise = i+xInt,j+yInt
            while self.isInBounds(run, rise):
                self.potentialMoves.append((run,rise))
                run,rise = run + xInt, rise + yInt

        self.potentialMoves = ["".join([map_index_to_alpha[i[1]], str(i[0] + 1)]) for i in self.potentialMoves]
        self.potentialMoves.sort()
        return self.potentialMoves

class Knight(Piece):
    def __init__(self, position):
        Piece.__init__(self, knightMoves, position)
        
    def enumerateMoves(self,chessBoard):
        i,j = self.row, self.column
        self.potentialMoves = []
        for a in range(len(self.moveSet)):
            x = self.moveSet[a][0]
            y = self.moveSet[a][1]
            try:
                temp = chessBoard[i + x][j + y]        
                self.potentialMoves.append([i + x, j + y])
            except:
                pass
        temp = [i for i in self.potentialMoves if i[0] >=0 and i[1] >=0]
        allPossibleMoves = ["".join([map_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
        allPossibleMoves.sort()
        return allPossibleMoves

class Rook(Piece):
    def __init__(self, position):
        Piece.__init__(self, horizontals, position)

    def enumerateMoves(self, chessBoard):
        return self.runRise(chessBoard)

class Queen(Piece):
    def __init__(self, position):
        Piece.__init__(self, horizontals+diagonals, position)

    def enumerateMoves(self, chessBoard):
        return self.runRise(chessBoard)

class Bishop(Piece):
    def __init__(self, position):
        Piece.__init__(self, diagonals,position)

    def enumerateMoves(self, chessBoard):
        return self.runRise(chessBoard)

def determinePiece(name):
    if name.lower() == "knight":
        knight = Knight(args.position)
        print(knight.enumerateMoves(chessBoard))
    elif name.lower() ==  "rook":
        rook = Rook(args.position)
        print(rook.enumerateMoves(chessBoard))
    elif name.lower() == "queen":
        queen = Queen(args.position)
        print(queen.enumerateMoves(chessBoard))
    elif name.lower() == "bishop":
        bishop = Bishop(args.position)
        print(bishop.enumerateMoves(chessBoard))

determinePiece(args.piece)
