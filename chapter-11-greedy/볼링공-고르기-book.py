import time

'''
N=5, M=3
data = [1 3 2 3 2 ]
array = [0 1 2 2]

for i in range(1,4):
    i = 1
    n -= array[i] -> 5 - 1 = 4
    result += array[i] * N -> 1 * 4 = 4

    i = 2
    n -= array[i] -> 4 - 2 = 2
    result += array[i] * N -> 2 * 2 = 4

    i = 3
    n -= arrray[i] -> 2 - 2 = 0
    result += array[i] * N -> 2 * 0 = 0

result = 8
'''

def solution(N, M, data):
    # 1 부터 M까지의 무게를 담을 수 있는 리스트
    array = [0] * (M+1)

    for x in data:
        # 각 무게에 해당하는 볼링공의 개수 카운트
        array[x] += 1

    result = 0
    # 1부터 m까지의 각 무게에 대하여 처리
    for i in range(1, M + 1):
        N -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
        result += array[i] * N # B가 선택하는 경우의 수와 곱해주기
    return result


N, M = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()
result = solution(N,M,data)
end_time = time.time()

print('실행 결과:', result)
print('걸린 시간:', end_time - start_time)
