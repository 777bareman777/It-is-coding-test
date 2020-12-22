import time

def combination(arr, n):
    result = []
    if n > len(arr): return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)-n+1):
            for temp in combination(arr[i+1:],n-1):
                result.append([arr[i]]+temp)
    return result

def solution(N, M, data):
    result = 0
    array = [i for i in range(1,(N+1))]
    comb = combination(array,2)
    for case in comb:
        a,b = data[case[0]-1], data[case[1]-1]
        if a != b:
            result += 1

    return result

N, M = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()
result = solution(N,M,data)
end_time = time.time()

print('실행 결과:', result)
print('걸린 시간:', end_time - start_time)
