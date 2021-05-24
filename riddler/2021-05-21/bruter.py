import math

n = int(input('What is N? '))

class Searcher:
    def __init__(self, n):
        self.n = n
        self.board = []
        self.ans = 0
        self.argmax = None

    def check(self, r, c):
        for i in range(len(self.board)-1):
            for j in range(i):
                dists = [
                    math.dist(self.board[i], self.board[j]),
                    math.dist(self.board[j], (r,c)),
                    math.dist((r,c), self.board[i])
                ]
                for x in range(len(dists)):
                    if abs(dists[x] - dists[x-1]) < 0.000000001:
                        return False
        return True

    def backtrack(self, i, j):
        nxt = self.get_next(i,j)
        if nxt is None:
            # if len(self.board) >= self.ans:
            #     print(self.ans)
            #     print(pretty(self.board))
            if len(self.board) > self.ans:
                self.ans = len(self.board)
                self.argmax = self.board[:]
                print(self.ans, self.argmax)
            return
        else:
            nxti, nxtj = nxt
        self.backtrack(nxti, nxtj)
        self.board.append((i,j))
        if self.check(i, j):
            self.backtrack(nxti, nxtj)
        self.board.pop()

    def get_next(self,i,j):
        if j+1 < n:
            return (i,j+1)
        elif i+1 < n:
            return (i+1, 0)
        else:
            return None
    
    def go(self):
        self.backtrack(0,0)

def pretty(points: list):
    board = [[0 for i in range(n)] for j in range(n)]
    for r,c in points:
        board[r][c] = 1
    ans = []
    for r in board:
        ans.append(''.join('X' if x else '.' for x in r))
    return '\n'.join(ans)

searcher = Searcher(n)
searcher.go()
print(searcher.ans)
print(searcher.argmax)
print(pretty(searcher.argmax))
