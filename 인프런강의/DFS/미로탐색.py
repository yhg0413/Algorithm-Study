
def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0 <= x <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0:
                board[xx][yy] = 1
                DFS(xx,yy)
                board[xx][yy] = 0

if __name__ == '__main__':
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    cnt = 0
    board = [[0]]

