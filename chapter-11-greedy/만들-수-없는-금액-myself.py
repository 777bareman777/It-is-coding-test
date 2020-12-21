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

def solution(N, data):
    data.sort()
    result = 0
    flag = [0 for i in range(sum(data))]

    for i in range(1,N+1):
        tmp = combination(data,i)
        sum_tmp = []
        for j in tmp:
            sum_tmp.append(sum(j))
        
        for j in sum_tmp:
            flag[j-1] += 1


    for i in range(len(flag)):
        if flag[i] == 0:
            result = i+1
            break
             
    return result


N = int(input())
data = list(map(int, input().split()))
start_time = time.time()
result = solution(N,data)
end_time = time.time()

print('실행 결과:', result)
print('걸린 시간:', end_time - start_time)
