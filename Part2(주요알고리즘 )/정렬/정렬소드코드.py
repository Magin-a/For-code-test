import sys
input = sys.stdin.readline

data1 = [2, 1 ,6, 7, 8, 9, 0, 4, 3, 5]


#1. 선택정렬
for a in range(len(data1)):
    min_index = a
    for b in range(a+1, len(data1)):
        if data1[min_index] > data1[b]:
            min_index = b

    data1[a], data1[min_index] = data1[min_index],  data1[a] #스와이프
print(data1)


data2 = [2, 1 ,6, 7, 8, 9, 0, 4, 3  ,5]
#삽입정렬
for a in range(1, len(data2)):
    for b in range(a, 0, -1):
        if data2[b] < data2[b-1]:
            data2[b], data2[b-1] = data2[b-1], data2[b]
        
        else:
            break
print(data2)

data3 = [5, 1, 6, 7, 8, 9, 0, 4, 2, 3]
#퀵정렬
def quick(data, start, end):
    if start >= end: #원소가 1개인 경우
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1

        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]

    quick(data3, start, right -1)
    quick(data3, right+1, end)

quick(data3, 0, len(data3)-1)
print(data3)
