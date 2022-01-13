# #게임개발

#1단계) 바라보는 방향 기준 왼쪽으로 갈 수 있는 곳 탐색
#2단계) 갈 수있는 곳이 나오면 그 방향으로 전진
#3단계) 만약 4방향 모두 가본 칸이거나 바다("1")라면 완전 방향으로 후진 
#   3-1단계) 후진 후 1단계 반복 But 후진이 바다일 경우 Break 


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
c_x, c_y, see = map(int, input().split())
dirt = [[0, -1], [-1, 0], [0, 1], [1, 0]]
memory = []
field = [input().split() for _ in range(m)]

def direction():
    global see
    see -= 1
    if see == -1:
        see = 3

count = 0
turn_cnt = 0
while True:
    direction()
    test_x , test_y =c_x + dirt[see][0], c_y + dirt[see][1] 

    if field[test_x][test_y] == "0" and [test_x, test_y] not in memory:
        memory.append([test_x, test_y])
        c_x, c_y =  test_x , test_y
        count += 1
        turn_cnt =0

    else:
        turn_cnt += 1
    
    
    
    if turn_cnt == 4:
        test_x , test_y =c_x - dirt[see][0], c_y - dirt[see][1]

        if field[test_x][test_y] == "0":
            c_x, c_y =  test_x , test_y

        else:

            break
        turn_cnt =0

print(count)
