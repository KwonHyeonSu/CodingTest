#include <iostream>
using namespace std;
#define MAXN ((int)1e3)
int N;//���ټ�
int A[MAXN+10];//������ǥ
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
	InputData();//�Է¹޴� �κ�

	//���⼭���� �ۼ�
    ans = Solve();
	cout << ans << "\n";//����ϴ� �κ�
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

1. �������� �� �Ÿ��� ������ �� �Ÿ� �̻� ������ �� 2�躸�� �ָ� ������ �ʴ´�.
2. �������� ���������θ� �ڴ�.
3. �������� �� ���� �ڴ�.
4. �� �� ���� ������ �����Ѵٸ� ��� �������� ������ �� �ִ�.
(1, 3, 7), (1, 4, 7), (4, 7, 10), (1, 4, 10)
*/
