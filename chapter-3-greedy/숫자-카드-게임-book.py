import time

def solution(N,M,matrix):
    result = 0
    for i in range(N):
        # 현재 줄에서 '가장 작은 수' 찾기
        tmp = 10001
        for tmp2 in matrix[i]:
            tmp = min(tmp, tmp2)
        # '가장 작은 수'들 주에서 가장 큰 수 찾기
        result = max(result, tmp)
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
