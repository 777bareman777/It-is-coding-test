import time

'''
데이터중 가장 큰 값을 찾는다.
그 다음으로 가장 큰 값을 찾는다.

가장 큰 값을 K번째 까지 더한다.
그 다음으로 가장 큰 값을 더한다.
위의 과정을 M번 반복할 때 까지 한다.
위의 과정은 M번 반뽁할 때 까지 반복한다.
'''

def solution(N,M,K,data):
    first = max(data)
    data.remove(first)
    second = max(data)

    result = 0
    itr = 0
    for i in range(M):
       if itr == K:
           itr = 0
           result += second
           continue

       result += first
       itr += 1

    return result



# N, M, K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

start = time.time()
result = solution(N,M,K,data)
end = time.time()

print('실행 결과:',result)
print('걸린 시간: ', end - start)
