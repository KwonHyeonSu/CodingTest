#include <iostream>
using namespace std;
#define MAXN ((int)1e3)
int N;//연잎수
int A[MAXN+10];//연잎좌표
void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> A[i];
	}
}


void Sort(){
    for(int i=0;i<N-1;i++){
        for(int j=i;j<N;j++){
            if(A[i] > A[j]){
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        }
    }
}

int FindLower(int s, int e, int d){

    int sol = -1;
    int m;
    while(s <= e){
        m = (s+e)/2;
        if(A[m] == d){
            sol = m;
            e = m-1;
        }else if(A[m] < d){
            s = m+1;
        }else{
            e = m-1;
        }
    }
    if(sol == -1){
        return e;
    }
    return sol;
}

int FindHigh(int s, int e, int d){
    int sol = -1;
    int m;
    while(s <= e){

        m = (s+e)/2;
        if(A[m] == d){
            sol = m;
            s = m+1;
        }else if(A[m] < d){
            s = m+1;
        }else{
            e = m-1;
        }
    }
    if(sol == -1){
        return s;
    }
    return sol;
}

int Solve(){
    Sort();
    /*
    cout << "Sort Complete\n";
    for(int i=0;i<N;i++){
        cout <<A[i] << " ";
    }
    cout <<endl;
    int val = 7;
    cout <<" findlow  "<<val<<" : " << FindLower(0, N-1, val) << endl;
    cout <<" findhigh  "<<val<<" : " << FindHigh(0, N-1, val) << endl;

*/
    int ret = 0;

    for(int i=0;i<N-2;i++){
        for(int j=i+1;j<N-1;j++){
            //dist between 1, 2
            int dist = A[j] - A[i];
            int low = FindHigh(j+1, N-1, A[j]+dist);
            int high = FindLower(j+1, N-1, A[j]+dist*2);
            if(low <= high){
                ret += high - low + 1;
            }

            //cout <<"dist : "<<dist<<endl;
            //cout << "(" << A[i] << ", " << A[j] << ", " << low << "to"<<high<< ")" << endl;
        }
    }

    return ret;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;
	InputData();//입력받는 부분

	//여기서부터 작성
    ans = Solve();
	cout << ans << "\n";//출력하는 부분
	return 0;
}

/*
5
3
1
10
7
4

4

1. 개구리가 뛴 거리가 이전에 뛴 거리 이상 뛰지만 그 2배보다 멀리 뛰지는 않는다.
2. 개구리는 오른쪽으로만 뛴다.
3. 개구리는 두 번만 뛴다.
4. 위 세 가지 조건을 만족한다면 어느 곳에서든 시작할 수 있다.
(1, 3, 7), (1, 4, 7), (4, 7, 10), (1, 4, 10)
*/
