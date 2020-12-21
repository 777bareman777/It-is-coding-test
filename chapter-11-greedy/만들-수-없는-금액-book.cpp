#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int N, vector<int> arr){
    sort(arr.begin(), arr.end());

    int target = 1;
    for (int i = 0; i < N; ++i) {
        // 만들 수 없는 금액을 찾았을 때 반복 종료
        if (target < arr[i]) break;
        target += arr[i];
    }

    return target;
} 

int main(){
    int N;
    cin >> N;

    vector<int> arr;
    for (int i = 0; i < N; ++i) {
        int x;
        cin >> x;
        arr.push_back(x);
    }

    int result = solution(N, arr);
    cout << "실행 결과: " << result << endl;
    return 0;
}
