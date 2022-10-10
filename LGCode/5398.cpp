#include <iostream>
using namespace std;
#define MAXN ((int)3e4)
int N;
int A[MAXN + 10];

void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> A[i];
	}
}

void OutputData(){
	for (int i=0; i<4; i++){
		cout << A[i] << " ";
	}
	cout << "\n";
}

void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
void Solve()
{
    for(int i=0;i<4;i++)
    {
        for(int j=i+1;j<N;j++)
        {
            if(A[i] > A[j]){
                swap(&A[i], &A[j]);
            }
        }
    }



}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력 받는 부분

	//여기서부터 작성
	Solve();

	OutputData();//출력 하는 부분
	return 0;
}
