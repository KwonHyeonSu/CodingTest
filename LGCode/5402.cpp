#include <iostream>
using namespace std;

#define MAX ((int)2e5)

int N;
int A[MAX+10];
int M;
int B[MAX+10];

void InputData(){
	cin >> N;
	for(int i=0 ; i<N ; i++) {
		cin >> A[i];
	}
	cin >> M;
	for(int i=0 ; i<M ; i++) {
		cin >> B[i];
	}
}

void OutputData(){
	for(int i=0 ; i<M ; i++) {
		cout << B[i] << " ";
	}
	cout << "\n";
}

int Lowerbound(int s, int e, int d){
    int sol = -1;
    while(s <= e){
        int m = (s+e)/2;
        if(A[m] == d){
            sol = m;
            e = m-1;
        }
        else if(A[m] < d){
            s = m+1;
        }
        else e = m-1;
    }
    return sol;
}
int Upperbound(int s, int e, int d){
    int sol = -1;
    while(s <= e){
        int m = (s+e)/2;
        if(A[m] == d){
            sol = m;
            s = m+1;
        }
        else if(A[m] < d){
            s = m+1;
        }
        else e = m-1;
    }
    return sol;
}


void Solve(){
    for(int i=0;i<M;i++){
        int upper;
        int lower = Lowerbound(0, N-1, B[i]);
        if(lower != -1){

            upper = Upperbound(0, N-1, B[i]);
            B[i] = upper-lower+1;
        }else{
            B[i] = 0;
        }
        //cout << "lower, upper : " << lower << ", " << upper <<endl;

    }
}

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	// 입력받는 부분
	InputData();

	// 여기서부터 작성
    Solve();

	// 출력하는 부분
	OutputData();
	return 0;
}


/*
10
1 1 1 6 9 11 13 17 19 20
2
2 9

3 1
*/
