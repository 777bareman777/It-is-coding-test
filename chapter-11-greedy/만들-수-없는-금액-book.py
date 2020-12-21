import time

'''
1 1 2 3 9 

target = 1
x = 1
1 < 1
target += x

target = 2
x = 1
2 < 1
target += x

target = 3
x = 2
3 < 2
taarget += x

target = 5
x = 3
5 < 3
target += x

target = 8
x = 9
8 < 9

target = 8
'''

def solution(N, data):
    data.sort()

    result = 1
    for x in data:
        # 만들 수 없는 금액을 찾았을 때 반복 종료
        if result < x:
            break
        result += x

    return result


N = int(input())
data = list(map(int, input().split()))
start_time = time.time()
result = solution(N,data)
end_time = time.time()

print('실행 결과:', result)
print('걸린 시간:', end_time - start_time)
