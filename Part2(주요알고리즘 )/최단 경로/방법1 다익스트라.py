#방법1 다익스트라
# - 시간 복잡도O(v^2) 연결된 모든 노드를 확인하기 때문

import sys
input = sys.stdin.readline
inf = int(1e9)

# 노드 개수, 간선의 개수
n,m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)]

visited = [False]*(n+1)

distance = [inf]*(n+1)

#간선 입력부
for _ in range(m):
    a, b, c = map(int, input().split())
    #a노드에서 b로 가는 비용c
    graph[a].append((b,c)) 

def find_min_node():
    min_val = inf
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i

    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = find_min_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now]+ j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf:
        print('무한')

    else:
        print(distance[i])
