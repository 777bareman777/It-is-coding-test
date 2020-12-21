import time

def solution(N):
    count = 0
    case = 0

    while(N>0):
        tmp = N

        # case를 올리면서, 가장 큰 화폐 단위부터 돈을 거슬러줌
        if case == 0:
            tmp -= 500
        elif case == 1:
            tmp -= 100
        elif case == 2:
            tmp -= 50
        elif case == 3:
            tmp -= 10

        # 거슬러 줘야 할 돈이 초과되 었을 때, case를 올려서, 화폐 단위를 바꿈. 
        if tmp < 0:
            case += 1
        # 초과되지 않았다면, 개수를 카운트함.
        else:
            N = tmp
            count += 1

    return count


N = 1260
start_time = time.time()
result = solution(N)
end_time = time.time()

print('결과:',result)
print(f'실행시간: {end_time-start_time}')
