#include <iostream>

using namespace std;

int solution(int N, int K){
    int count = 0;

    while(true) {
        // N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
        int target = (N / K) * K;
        count += (N - target);
        N = target;
        // N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        if (N < K) break;
        // K로 나누기
        count += 1;
        N /= K;
    }

    // 마지막으로 남은 수에 다하여 1씩 빼기
    count += (N - 1);
    return count;
} 

int main(){
    int N, K;
    // N, K를 공백을 기준으로 구분하여 입력 받기
    cin >> N >> K;

    int result = solution(N,K);
    cout << "실행 결과: " << result << endl;
    return 0;
}
