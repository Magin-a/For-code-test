#게임개발
import sys
N, M = map(int, sys.stdin.readline().split())
c_x, c_y, way = map(int, sys.stdin.readline().split())

field =[sys.stdin.readline().split() for _ in range(N)]
clear_site = [] 
move= [[0, -1], [1, 0],[0, 1], [-1, 0]]

c_site = field[c_x][c_y]

while True:
    for x, y in move:
        test_x, test_y = c_x+x, c_y+y
        if (0 <= test_x <N and 0 <= test_y <M) and field[test_x][test_y] != '1' and [test_x, test_y] not in clear_site:
            c_site = [test_x, test_y]
            clear_site.append(c_site)
        else:
            continue


#1단계) 바라보는 방향 기준 왼쪽으로 갈 수 있는 곳 탐색
#2단계) 갈 수있는 곳이 나오면 그 방향으로 전진
#3단계) 만약 4방향 모두 가본 칸이거나 바다("1")라면 완전 방향으로 후진 
#   3-1단계) 후진 후 1단계 반복 But 후진이 바다일 경우 Break 