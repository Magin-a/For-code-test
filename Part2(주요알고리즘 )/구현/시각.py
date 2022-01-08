#시각
import sys
n = int(sys.stdin.readline())
result = 0
for a in range(n+1):
    for b in range(60):
        for c in range(60):
            if '3' in str(a) +str(b) + str(c):
                print(a, b ,c)
                result += 1

print(result)


#1시간의 모든 경우의 수 => 3600개
#1~59중에 3이 포함되는 수 갯수 => 15개 
