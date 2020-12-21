import time

def solution(N,M,matrix):
    result = 0
    for i in range(N):
        tmp = min(matrix[i])
        result = max(tmp, result)
    return result


# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())
# matrix을 공백으로 구분하여 입력 받기
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

start_time = time.time()
result = solution(N,M,matrix)
end_time = time.time()

print('실행 결과:',result)
print('걸린 시간:',end_time-start_time)
