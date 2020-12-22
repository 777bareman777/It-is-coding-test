#include <iostream>

using namespace std;

int solution(int N, int M, int* arr){
    int result = 0;
    // 1부터 m까지의 각 무게에 대하여 처리
    for (int i = 1; i <= M; ++i) {
        N -= arr[i] ; // 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
        result += arr[i] * N; // B가 선택하는 경우의 수와 곱해주기
    }

    return result;
} 

int main(){
    int N, M;
    cin >> N >> M;
    
    int* arr = new int[M+1];
    for (int i = 0; i < N; ++i){
        int x;
        cin >> x;
        arr[x] += 1;
    }

    int result = solution(N,M,arr);
    cout << "실행 결과: " << result << endl;

    delete[] arr;
    return 0;
}
