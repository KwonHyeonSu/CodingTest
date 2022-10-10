#include <iostream>
#include <cstring>

using namespace std;
int N, M;//장기판 행의 수, 열의 수
int R, C, S, K;//말 행과 열, 졸 행과 열

void InputData(){
	cin >> N >> M;
	cin >> R >> C >> S >> K;
}

int visited[100][100];

struct QUE{
    int h, w, t;
};

struct QUE que[10000];
int rp, wp;
void push(int h, int w, int t)
{
    if(visited[h][w] == 1) return;
    if(h <= 0 || h > N || w <= 0 || w > M) return;
    visited[h][w] = 1;
    que[wp].h = h;
    que[wp].w = w;
    que[wp].t = t;

    wp++;
}

void pop(){rp++;}

int empty(){return wp==rp;}

struct QUE front(){return que[rp];}

int Solve()
{
    memset(visited, 0, sizeof(visited));
    wp = rp = 0;

    push(R, C, 0);

    int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
    int dy[] = {1, -1, 2, -2, 2, -2, 1, -1};

    while(!empty())
    {
        struct QUE cur = front();
        pop();
        if(cur.h == S && cur.w == K) return cur.t;
        for(int i=0;i<8;i++)
        {
            int dn = cur.h + dx[i];
            int dw = cur.w + dy[i];

            push(dn, dw, cur.t+1);
        }

    }
    return -2;

}


int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;
	InputData();//입력

	//여기서부터 작성
    ans = Solve();
	cout << ans << "\n";//출력
	return 0;
}

/*
9 9
3 5 2 8

2
*/
