import time

def solution(S):
    # 첫 번째 문자를 숫자로 변경하여 대입
    result = int(S[0])

    for i in range(1, len(S)):
        # 두 수중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하긱 수행
        num = int(S[i])
        if num <= 1 or result <= 1:
            result += num
        else :
            result *= num

    return result 


S = input()
start_time = time.time()
result = solution(S)
end_time = time.time()

print('실행 결과:', result)
print('걸린 시간:', end_time - start_time)
