#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int solution(int N, vector<int> K){
    int result = 0; // 총 그룹의 수
    int count = 0; // 현재 그룹에 포함된 모험가의 수
    sort(K.begin(), K.end()); // 공포도 낮은 순서대로 정렬

    for (int i = 0; i < N ; ++i) { // 공포도를 낮은 것부터 하나씩 확인하며
        count += 1; // 현재 그룹에 해당 모험가를 포함시키기
        if (count >= K[i]) { // 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 생성
            result += 1; // 총 그룹의 수 증가시키기
            count = 0; // 현재 그룹에 포함된 모험가의 수 초기화
        }
    }

    return result;
} 

int main(){
    int N;
    cin >> N;

    vector<int> K;
    for (int i = 0; i<N; ++i) {
        int tmp;
        cin >> tmp;
        K.push_back(tmp);
    }

    int result = solution(N,K);
    cout << "실행 결과: " << result << endl;
    return 0;
}
