#include <iostream>
#include <cstring>
using namespace std;

#define MAXN (100)
int W, H;//����, ���� ũ��
int sw, sh, ew, eh;//��� ���μ���, ���� ���μ��� ��ǥ
char map[MAXN+10][MAXN+10];//��������

void InputData(){
	cin >> W >> H;
	cin >> sw >> sh >> ew >> eh;
	for (int i=1; i<=H; i++){
		cin >> &map[i][1];
	}
}

int visited[MAXN+10][MAXN+10];

struct QUE{
    int h, w, t;
};

struct QUE que[MAXN * MAXN + 10];
int rp, wp;

void push(int h, int w, int t){
    if(map[h][w] != '0') return;
    if(visited[h][w] == 1) return;
    visited[h][w] = 1;
    que[wp].h = h;
    que[wp].w = w;
    que[wp].t = t;
    wp++;
}

void pop(){
    rp++;
}

int empty(){
    return wp==rp;
}

struct QUE front(){
    return que[rp];
}

int BFS()
{
    int dh[] = {1,-1, 0, 0};
    int dw[] = {0, 0, -1, 1};

    //memset(visited, 0, sizeof(visited));
    rp = wp = 0;

    push(sh, sw, 0);



    while(!empty()){
        struct QUE cur = front();
        pop();

        if((cur.h == eh) && (cur.w == ew)) return cur.t;
        for(int i=0;i<4;i++)
        {
            int nh = cur.h + dh[i];
            int nw = cur.w + dw[i];

            push(nh, nw, cur.t+1);

        }

    }
    return -2;

}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans = -1;
	InputData();//�Է�

	//���⼭���� �ۼ�
    ans = BFS();
	cout << ans << "\n";//���
	return 0;
}
