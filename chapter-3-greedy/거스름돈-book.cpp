#include <iostream>

using namespace std;

int solution(int N){
    int count = 0;
    int coin_types[4] = {500, 100, 50, 10};
    int len = sizeof(coin_types)/sizeof(int);

    for(const auto& coin : coin_types){
        count += N / coin;
        N %= coin;
    }

    return count;
} 

int main(){
    int N = 1260;
    int result = solution(N);
    cout << "결과: " << result << endl;
    return 0;
}
