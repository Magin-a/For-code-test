#방법2 다익스트라
# - 개선된 다익스트라 시간 복잡도O(ElogV) E는 간선의 개수 V는 노드의 개수

#특징 
# - 연결된 노드중에 가장 작은 짧은 거리 노드를 찾는걸 '힙(heap)'구조 사용
# - 힙큐에 값을 넣을 때 첫번째 원소가 기분이기에 (가치, 노드)으로 설정

import sys
import heapq 
input = sys.stdin.readline
inf =int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)]

distance = [inf]*(n+1) #다익스트라 테이블

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start)) 
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) #(가치, 노드)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf:
        print('무한')

    else:
        print(distance[i])

