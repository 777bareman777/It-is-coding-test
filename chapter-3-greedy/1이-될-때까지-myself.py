import time

def solution(N,K):
    count = 0
    while(N>1):
        if N % K == 0:
            N//=K
        else:
            N-=1
        count +=1
    return count


N, K = map(int, input().split())

start_time = time.time()
result = solution(N,K)
end_time = time.time()

print('실행 결과:',result)
print('걸린 시간:',end_time - start_time)
