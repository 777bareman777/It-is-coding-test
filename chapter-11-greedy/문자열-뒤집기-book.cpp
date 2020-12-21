#include <iostream>

using namespace std;

int solution(string S){
    int count0 = 0; // 전부 0으로 바꾸는 경우
    int count1 = 0; // 전부 1로 바꾸는 경우

    // 첫 번째 원소에 대해서 처리
    if (S[0] == '1') {
        count0 += 1;
    }
    else {
        count1 += 1;
    }

    // 두 번째 원소부터 모든 원소를 확인하며
    for (int i=0; i<S.size()-1; ++i) {
        if (S[i] != S[i+1]) {
            // 다음 수에서 1로 바뀌는 경우
            if (S[i+1] == '1') count0 += 1;
            // 다음 수에서 0으로 바뀌는 경우
            else count1 += 1;
        }
    }
    return min(count0,count1);
} 

int main(){
    string S;
    cin >> S;

    int result = solution(S);
    cout << "실행 결과: " << result << endl;
    return 0;
}
