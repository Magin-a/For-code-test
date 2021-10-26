#예제3-2(큰 수의 법칙)
#입력 
#첫번째 줄) N(2<= N <=1000 ), M(1<= M <= 10000), K( 1<= k <= 10000) 모두 자연수 공백으로 구분
#두번째 줄) N개의 자연수가 주어진다. 각 자연수는 공백으로 구분 (각 자연수는 1부터 10000이하의 수로 주어진다.)
#입력으로 주언진 K는 항상 M보다 작거나 같다.
#출력) 설명에 있는 큰수의 법칙에 따라 더해진 값 출력

#반복문을 통한 코드드
N, M, K = map(int, input().split())  
num = list(map(int, input().split())) # N개의 자연수 리스트

num.sort()

num1 = num[N-1]
num2 = num[N-2]
result = 0
count = 0

while True:
    for _ in range(K):
        if count == M:
            break
        else:   
           result += num1
           count += 1
    if count == M:
        break
    result += num2
    count+= 1


print(result)


#반복되는 수열 파악
N, M, K = map(int, input().split())  # (2<=N<=1000), (1 <= M <= 10,000), (1 <= K <= 10,000)
num = list(map(int, input().split())) # N개의 자연수 리스트

num.sort()

num1 = num[N-1]
num2 = num[N-2]
result = 0

count = (M/(K+1))*K
count += M%(K+1)

result += count*num1
result += (M-count)*num2
print(result)

