#include <iostream>
using namespace std;

#define MAXN (100)
int N, M;//문서수, 궁금한 문서 번호
int P[MAXN+10];//문서 우선순위

//queue
int que[MAXN+10];
int rp = 0;

void pprint(){
    cout << "\n\033[31m-----pprint-----\033[0m\n";
    cout << "rp : " << rp << "\t M : " << M << endl;
    for(int i=0;i<=rp;i++){
        if(i == rp) cout << "\033[34m";
        if(i == M) cout << "\033[35m";
        cout << que[i] << " ";
        cout << "\033[0m";
    }
    cout << "\n\033[31m-----pprint end-----\033[0m\n\n";
}
void push(int a){
    if(que[rp] == 0){
        que[rp] = a;
    }
    else{
        que[++rp] = a;
    }
    //pprint();
}
int pop(int a = 0){
    int ret = que[0];
    for(int i=0;i<rp;i++){
        que[i] = que[i+1];
    }
    rp--;
    if(M == 0){
        if(a) M = rp+1;
        else M = rp;
    } 
    else M--;
    //pprint();

    return ret;
}
int front(){return que[0];}
int back(){return que[rp];}

int Solve(){
    int k = 0;
    rp = 0;
    que[rp] =0;
    for(int i=0;i<N;i++){
        push(P[i]);
    }
    //cout << "--------------------\n";
    int n = 1;
    while(true){
        auto flag = false;
        for(int i=1;i<=rp;i++){
            if(que[0] < que[i]){
                push(pop(true));
                flag = true;
                break;
            }
        }
        if(!flag){
            //cout << "just popped!" << endl;
            k++;
            if(M==0) return k;
            pop(false);
        }
        n++;
    }
    return -2;
}

void InputData() {
    cin >> N >> M;
    for (int i=0; i<N; i++){
        cin >> P[i];
    }
}


int main() {
    int ans = -1;
    int T;
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    cin >> T;
    for (int t=1; t<=T; t++){
        InputData();//입력받는 부분

        //여기서부터 작성
        ans = Solve();
        cout << ans << "\n";//출력하는 부분
    }
    return 0;
}

/*
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
*/