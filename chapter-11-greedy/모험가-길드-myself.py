import time

def solution(N,K):
    count = 0
    # 공포도가 높은 순서대로 정렬
    K.sort()

    print(K)
    while True:
        # 공포도가 높은 모험가 찾기
        if K: 
            max_fear = max(K)

        # 공포도가 높은 모험가 보다 모험가의 수가 많다면, 모험가 그룹 생성
        if len(K) >= max_fear:
            for i in range(max_fear):
                K.pop()
            count += 1
        # 공포도가 높은 모험가 보다 모험ㅎ가의 수가 많다면, 모험가 그룹 생성 종료
        else:
            break

    return count

# N, 모험가의 수
N = int(input())
# K, 모험가별 공포도
K = list(map(int, input().split()))

start_time = time.time()
result = solution(N,K)
end_time = time.time()

print('실행 결과:',result)
print('걸린 시간:',end_time-start_time)
