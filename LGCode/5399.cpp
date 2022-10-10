#include <iostream>
using namespace std;
#define MAXN ((int)3e4)
int N;//자료 개수
struct ST{
	int id, score;//아이디, 점수
};
ST A[MAXN + 10];//자료

void InputData(){
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i].score;
		A[i].id = i+1;
	}
}

void OutputData() {
	for (int i = 0; i < 3; i++) {
		cout << A[i].id << " ";
	}
	cout << "\n";
}

void swap(ST *a, ST *b)
{
    ST tmp = *a;
    *a = *b;
    *b = tmp;
}

void Solve()
{
    for(int i=0;i<3;i++)
    {

        for(int j=i+1;j<N;j++){
            if(A[i].score < A[j].score){
                swap(&A[i], &A[j]);
            }
            if(A[i].score == A[j].score && A[i].id > A[j].id){
                swap(&A[i], &A[j]);
            }
        }
    }

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력
	//작성
	Solve();
	OutputData();
	return 0;
}
