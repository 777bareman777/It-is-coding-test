#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int solution(int N, int M, int K, vector<int>& data){
    sort(data.begin(), data.end()); // 입력 받은 수들 정렬하기
    int first = data[N-1]; // 가장 큰수
    int second = data[N-2]; // 두 번째로 큰 수

    // 가장 큰 수가 더해지는 횟수 계산
    int count = (M / (K+1)) * K + M % (K+1);

    int result = 0;
    result += count * first; // 가장 큰 수 더하기
    result += (M-count) * second; // 두 번째로 큰 수 더하기

    return result;
}


int main(){
    int N, M, K;
    vector<int> V;
    // N, M, K를 공백을 기준으로 구분하여 입력 받기
    cin >> N >> M >> K;

    // N개의 수를 공백을 기준으로 구분하여 입력받기
    for(int i=0;i<N;++i){
        int x;
        cin >> x;
        V.push_back(x);
    }

    int result = solution(N,M,K,V);
    cout << "실행 결과: " << result << endl;
    return 0;
}


