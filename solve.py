from collections import deque
import copy
dy,dx=[0,0,1,-1],[1,-1,0,0] #동서남북
def end(y,x,p,oil,goal):
    gy,gx=goal[0],goal[1]
    if gy==y and gx==x:
        return y,x,oil
    else:
        dq = deque()
        chk = [[False] * n for _ in range(n)]
        dq.append([y, x, p])
        chk[y][x] = True
        lst=[]
        while dq:
            y, x, p = dq.popleft()
            p += 1
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and mapp[ny][nx] != 1 and chk[ny][nx] == False:
                    if ny == gy and nx == gx:
                        chk[ny][nx] = True
                        dq.append([ny,nx,p])
                        lst.append([ny,nx,p])
                    else:
                        chk[ny][nx] = True
                        dq.append([ny,nx,p])
        if len(lst) > 0:
            y, x, p = lst[0][0], lst[0][1], lst[0][2]
            oil -= p
            if oil >= 0:
                oil = oil + (p * 2)
                return y, x, oil
            elif oil < 0:
                oil = -1
                return ny, nx, oil
        else:
            oil = -1
            return y, x, oil

def bfs(y,x,p,oil): #고객 찾기
    if mapp[y][x] != 0 and len(mapp[y][x]) > 0:
        goal=mapp[y][x]
        mapp[y][x]=0
        return y,x,oil,goal
    dq = deque()
    chk = [[False] * n for _ in range(n)]
    dq.append([y, x, p])
    chk[y][x] = True
    lst = []
    while dq:
        y, x, p = dq.popleft()
        p += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and mapp[ny][nx] != 1 and chk[ny][nx] == False:
                if mapp[ny][nx] == 0:
                    chk[ny][nx] = True
                    dq.append([ny, nx, p])
                else:
                    chk[ny][nx] = True
                    lst.append([ny, nx, p])
                    dq.append([ny, nx, p])
    # 람다 정렬 후 end 보내기
    if len(lst) > 0:
        lst.sort(key=lambda x: (x[2], x[0], x[1]))
        y, x, p = lst[0][0], lst[0][1], lst[0][2]
        oil -= p
        goal = mapp[y][x]
        mapp[y][x] = 0
        return y, x, oil,goal
    else:
        goal=[]
        oil = -1
        return y, x, oil,goal

n,m,oil=map(int,input().split())
mapp=[list(map(int, input().split())) for _ in range(n)]
taxi=list(map(int, input().split()))
y,x = taxi[0]-1, taxi[1]-1
men=[list(map(int, input().split())) for _ in range(m)]
ans=0
t=0
for k in men:
    mapp[k[0]-1][k[1]-1]=[k[2]-1, k[3]-1]
    t+=1
for _ in range(t):
    y,x,oil,goal=bfs(y,x,0,oil)
    if oil<=0:
        oil=-1
        break
    y,x,oil=end(y,x,0,oil,goal)
    if oil<=0:
        oil=-1
        break
ans=oil
print(ans)