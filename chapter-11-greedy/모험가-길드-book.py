import time

def solution(N,K):
    result = 0  # 총 그룹의 수
    count = 0 # 현재 그룹에 포함된 모험가의 수
    K.sort() # 공포도가 높은 순서대로 정렬

    for i in K: # 공포도를 낮은 것부터 하나씩 확인하기
        count += 1 # 현재 그룹에 해당 모험가를 포함시키기
        if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
            result += 1 # 총 그룹의 수 증가시키기
            count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

    return result

# N, 모험가의 수
N = int(input())
# K, 모험가별 공포도
K = list(map(int, input().split()))

start_time = time.time()
result = solution(N,K)
end_time = time.time()

print('실행 결과:',result)
print('걸린 시간:',end_time-start_time)
