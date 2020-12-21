import time

def solution(S):
    result = 0
    for number in S:
        number = int(number)
        if number <= 1 or result <=1 :
            result += number
        else:
            result *= number
    return result 


S = input()
start_time = time.time()
result = solution(S)
end_time = time.time()

print('실행 결과:', result)
print('걸린 시간:', end_time - start_time)
