#왕실의 나이트
import sys
knight_x, knight_y = sys.stdin.readline().rstrip()
knight_site = [int(ord(knight_x))-64, int(knight_y)] #x,y 좌표
count = 0 # 체스판 안에 있을 경우 카운트

f_move = [-2, 2]
s_move = [-1, 1]
#수평이동 먼저할 때
for a in f_move:
    test_x = knight_site[0] + a
    for b in s_move:
        test_y = knight_site[1] + b
        if 1 <= test_x <= 8 and 1 <= test_y <= 8:
            print(chr(test_x+64), test_y)
            count += 1
#수직이동 먼저 할때
for a in f_move:
    test_y = knight_site[1] + a
    for b in s_move:
        test_x = knight_site[0] + b
        if 1 <= test_x <= 8 and 1 <= test_y <= 8:
            count += 1
            print(chr(test_x+64), test_y)

print(count) #이동가능한 경우의 수
