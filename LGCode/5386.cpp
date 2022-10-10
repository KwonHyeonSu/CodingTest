#include <iostream>
using namespace std;

#define MAXN (100)
int N;
int sol[MAXN + 10];

//que
int que[MAXN + 10];
int fp, bp;
void Push(int a){
    if(que[bp]==0) que[bp] = a;
    else que[++bp] = a;

    //cout << "Push : " << a << endl;
}
int Pop(){
    //cout << "Pop : " << que[fp] << endl;
    int ret = que[0];
    for(int i=0;i<bp;i++){
        que[i] = que[i+1];
    }
    que[bp--] = 0;
    return ret;
    //return que[fp++];
}
int Front(){
    return que[fp];
}
int Back(){
    return que[bp];
}

void InputData(){
	cin >> N;
}

void OutputData(){
	for (int i=0; i<N; i++){
		cout << sol[i] << "\n";
	}
}

void Solve(){
    int n=0;
    fp = bp = 0;

    for(int i=1;i<=N;i++){
        Push(i);
    }

    while(n < N-1){

        int t = Back()/2;
        for(int i=1;i<=t;i++){
            Push(Front());
            Pop();
        }

        sol[n]=Front();
        Pop();
        n++;
    }
    sol[N-1] = Pop();
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력
	//여기서부터 작성
    Solve();
	OutputData();//출력
	return 0;
}
// 1 2 3 4 1 2
/*
1) 가장 아래 카드 번호를 2로 나눈 몫의 정수만큼 반복하여 제일 위에 올라와 있는
 카드부터 한 장씩 순서대로 가장 밑으로 옮긴다.
2) 옮긴 후 가장 위에 올라와 있는 카드 한 장을 상대에게 넘긴다.
위 1)~2) 행동을 N-1번 수행하고 마지막에는 남은 카드 한 장을 넘긴다.
위 규칙대로 카드를 넘겼을 때, 상대방에게 넘긴 카드 번호를 넘긴 순서대로 출력하시오. 

4

3 1 2 4 

*/