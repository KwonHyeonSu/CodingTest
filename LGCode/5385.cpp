#include <iostream>
#include <stack>

using namespace std;
#define MAXN ((int)1e5)
int N;//빌딩수
int H[MAXN+10];//빌딩높이
int sol[MAXN+10];//각 빌딩에서 보이는 빌딩 번호

//stack
int stk[MAXN+10];
int sp;
void push(int h){ stk[++sp] = h;}
void pop(){sp--;}
int top(){return stk[sp];}
int empty(){return sp==0;}


void InputData() {
	cin >> N;
	for (int i=1; i<=N; i++){
		cin >> H[i];
	}
}
void OutputData() {
	for (int i=1; i<=N; i++){
		cout << sol[i] << "\n";
	}
}

void SolveStack()
{
    sp = 0; //스택 초기화
    for(int i=1;i<=N;i++){
        while(!empty() && (H[top()] < H[i])){
            sol[top()] = i;
            pop();
        }
        push(i);
    }
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	InputData();//입력받는 부분

	//여기서부터 작성
    SolveStack();
	OutputData();//출력하는 부분
	return 0;
}

/*

0
10
1 2 4 3 5 6 9 8 7 10
2 3 5 5 6 7 10 10 10 0

*/