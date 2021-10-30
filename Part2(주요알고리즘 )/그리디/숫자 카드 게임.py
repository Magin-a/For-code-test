#예제3-3(숫자 카드 게임)
m, n  = map(int, input().split())
board = []
result = 0
for _ in range(m):
    num = list(map(int, input().split()))
    pre = result
    result = min(num)
    if pre >= result:
        result = pre

print(result)
