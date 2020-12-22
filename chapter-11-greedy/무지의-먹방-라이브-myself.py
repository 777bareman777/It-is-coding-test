import time
import numpy as np

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    answer = 0
    food_times = np.array(food_times)
    
    while True:
        access_index = np.nonzero(food_times)[0] # 시간이 남은 음식을 찾는다.
        min_times = min(food_times[access_index]) # 그중 최소 시간 음식을 찾는다.
        len_access_index = len(access_index)
        
        #print(food_times, k , min_times*len_access_index)
       
        if k >= min_times * len_access_index:
            # 남은 음식들 중 최소 시간만큼 빼버린다.
            food_times[access_index] -= min_times
            # 남은 음식들 * min_times 만큼 k를 빼버린다.
            k -= (min_times) * len_access_index
        else:
            break
    
    # 나머지중 한번에 뺄 수 있는 횟수 찾기
    for itr in range(1,min_times+1):
        if k < itr * len_access_index:
            food_times[access_index] -= (itr-1)
            k -= (itr-1) * len_access_index
            break
        
    idx = 0
    for _ in range(k):
        idx += 1
        if idx == len_access_index:
            idx = 0
    answer = int(access_index[idx]) + 1
    
    return answer

food_times = [3,1,2]
k = 5

start_time = time.time()
result = solution(food_times, k)
end_time = time.time()

print('실행 결과:',result)
print('걸린 시간:',end_time-start_time)
