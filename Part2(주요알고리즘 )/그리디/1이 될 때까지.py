#예제3-4(1이 될 때까지)
#나의 코드
#N 과 K를 입력 받고 N이 1이 될떄까지 1. N에서 1을 뺀다  2. N을 K로 나눈다. 반복
import sys

k, n = map(int, sys.stdin.readline().split())
count = 0

while k != 1:
    if k%n == 0:
        k //= n 
        count += 1
    else:
        k -= 1
        count += 1
print(count)

#***
k, n = map(int, input().split())
result =0

while k >= k:
    while n% k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

