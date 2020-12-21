import time


def solution(N):
    count = 0
    coin_types = [500,100,50,10]

    for coin in coin_types:
        count += N // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
        N %= coin

    return count


N = 1260
start_time = time.time()
result = solution(N)
end_time = time.time()

print('결과:',result)
print(f'실행시간: {end_time-start_time}')
