#미로탈출
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int ,input().rstrip())) for _ in range(n)]
move_x = [1, 0, -1, 0]
move_y = [0, 1, 0, -1]
result = 0

def bfs(x, y):

    q = deque()
    q.append([x, y])
        

    while q:
        test_x, test_y = q.popleft()

        for i in range(4):
            t_x = test_x + move_x[i] 
            t_y = test_y + move_y[i]

            if t_x < 0 or t_x >= n or t_y < 0 or t_y >= m:
                continue
                
            if graph[t_x][t_y] == 0:
                continue

            if graph[t_x][t_y] == 1:
                graph[t_x][t_y] = graph[test_x][test_y] +1
                q.append([t_x,t_y])
    
    return graph[n-1][m-1]

print(bfs(0, 0))
