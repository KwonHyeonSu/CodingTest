#include <iostream>
using namespace std;
#define MAXN ((int)1e4)
int N, M;
int A[MAXN+10];
void InputData(){
	cin >> N;
	for (int i=0 ; i<N ; i++){
		cin >> A[i];
	}
	cin >> M;
}

int isPossible(int m){
    int sum = M;
    for(int i=0;i<N;i++){
        if(A[i] > m) sum -= m;
        else sum -= A[i];
        if(sum < 0) return -1;
    }
    return 1;
}

int Solve()
{
    int s = 0, e = 0, sol = 0;
    for(int i=0;i<N;i++){
        if(e < A[i]) e = A[i];
    }
    while(s<= e){
        int m = (s+e)/2;
        if(isPossible(m) == 1){
            sol = m;
            s = m+1;
        }else{
            e = m-1;
        }
    }

    return sol;

}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;

	InputData();// 입력받는 부분

	// 여기서부터 작성
    ans = Solve();
	cout << ans << "\n";// 출력하는 부분
	return 0;
}
/*
4
120 110 140 150
485

127
*/
