import time

'''
예시) 0001100

연속된 문자열을 찾는다.

0~2번째까지 0이 연속한다는 것을 찾아냈다.
이거을 하나의 리스트로 분리시킨다.

3~4번째까지 1이 연속한다는 것을 찾아냈다.
이것을 하나의 리스트로 분리시킨다.

5~6번째까지 0이 연속한다는 것을 찾아냈다.
이것을 하나의 리스트로 분리시킨다.

그와 동시에 0과 1이 연속적으로 발생하는 횟수를 기록한다.
그중 작은 횟수를 가진 리스트를 뒤집고
순서대로 리스트를 합치면 최소 횟수로 문자열을 뒤집을 수 있다.
'''

def solution(S):
    result = 0

    sub_S = []
    prev = S[0]
    count = 1 
    count_0, count_1 = 0, 0
    for i in range(1, len(S)):
        if prev == S[i] :
            count += 1
        else:
            if prev == '0' :
                count_0 += 1
            else:
                count_1 += 1

            tmp = [prev for i in range(count)]
            sub_S.append(tmp)
            prev = S[i]
            count = 1

    if prev == '0':
        count_0 += 1
    else:
        count_1 += 1
    tmp = [prev for i in range(count)]
    sub_S.append(tmp)

    print(count_0, count_1)

    if count_0 >= count_1 :
        result = count_1
        for i in range(len(sub_S)):
            if sub_S[i][0] == '1':
                for j in range(len(sub_S[i])):
                    sub_S[i][j]='0'
    else:
        result = count_0
        for i in range(len(sub_S)):
            if sub_S[i][0] == '0':
                for j in range(len(sub_S[i])):
                    sub_S[i][j]='1'
    
    sub_S = sum(sub_S, [])
    S = ''.join(sub_S)
    print(S)
    
    return result 


S = input()
start_time = time.time()
result = solution(S)
end_time = time.time()

print('실행 결과:', result)
print('걸린 시간:', end_time - start_time)
