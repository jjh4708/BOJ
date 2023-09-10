import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().strip().split())
graph = []
INF = 10e9
visited = [[[0] * 2 for _ in range(W)] for _ in range(H)]
moves = [[-1,0], [1,0], [0,-1], [0,1]]

for _ in range(H):
    l = list(input().strip())
    graph.append(l)

def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 0

    while q : 
        v = q.popleft()

        if v[0] == H-1 and v[1] == W-1 :
            return visited[v[0]][v[1]][v[2]]
        
        for i in moves : 
            ny = v[0] + i[0]
            nx = v[1] + i[1]
        
            if 0 <= ny < H and 0 <= nx < W :
                if graph[ny][nx] == '1' and v[2] == 0 :
                    visited[ny][nx][1] = visited[v[0]][v[1]][0] + 1
                    q.append([ny,nx,1])

                if graph[ny][nx] == '0' and visited[ny][nx][v[2]] == 0: 
                    visited[ny][nx][v[2]] = visited[v[0]][v[1]][v[2]] + 1
                    q.append([ny,nx,v[2]])
    return -1

answer = bfs()
if answer == -1 :
    print(-1)
else :
    print(answer+1)
                


