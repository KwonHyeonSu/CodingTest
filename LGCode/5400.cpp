#include <iostream>
using namespace std;

#define MAXN ((int)5e3)
int N;
int A[MAXN + 10];

void InputData(){
	cin >> N;
	for (int i=0; i<N; i++){
		cin >> A[i];
	}
}

void swap(int* a, int* b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void Toleft()
{

    for(int i=1;i<N;i++)
    {
        A[i] = A[i+1];
    }
    N-=1;
}

void pprint()
{
    cout << "\n-----pprint------" << N <<endl;
    for(int i=0;i<N;i++){
        cout << i << ": " << A[i] << " ";
    }
    cout << endl;
}

int Solve()
{
    int ret= 0;
    while(true){
        //2 small to left
        for(int i=0;i<2;i++){
            for(int j=i+1;j<N;j++)
            {
                if(A[i] > A[j]){
                    swap(&A[i], &A[j]);
                }
            }
        }
        //cout << "sort complete\n";
        //pprint();
        int addret = A[0] + A[1];
        A[0] = addret;
        ret += addret;

        //cout <<"\nadd complete\n";
        //pprint();

        if(N > 2){

            Toleft();
            //cout <<"Tolefted\n";
            //pprint();
        }

        if(N == 2){
            ret += A[1];
            ret += A[0];
            break;
        }


        else if(N == 1){
            break;
        }

    }
    //pprint();

    return ret;

}


int main(){
	int ans = -1;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	InputData();//입력

	//여기서부터 작성
    ans = Solve();
	cout << ans << "\n";
	return 0;
}
/*
8
18 1 3 31 71 77 44 35

13
*/
