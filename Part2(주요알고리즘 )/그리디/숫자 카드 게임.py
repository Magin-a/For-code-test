#예제3-3(숫자 카드 게임)
#나의코드
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

#교재 코드(1) min()함수
m, n  = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)

#교재코드(2) 2중반본문
m, n  = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
        result = max(result, min_value)

print(result)
