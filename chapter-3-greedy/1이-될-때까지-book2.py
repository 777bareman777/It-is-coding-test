import time

def solution(N,K):
    count = 0

    while True:
        # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
        target = (N // K) * K
        count += (N - target)
        N = target
        # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        if N < K:
            break;
        # K로 나누기
        count += 1
        N //= K

    # 마지막으로 남은 수에 대하여 1씩 빼기
    count += (N-1)
    return count


# N이 K 이상이라면 K로 게속 나누기
N, K = map(int, input().split())

start_time = time.time()
result = solution(N,K)
end_time = time.time()

print('실행 결과:',result)
print('걸린 시간:',end_time - start_time)
