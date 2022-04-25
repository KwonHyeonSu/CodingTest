#include <iostream>
#include <vector>

using namespace std;

template <typename T>
void pprint(T a)
{
    for(int i=0;i<a.size();i++)
    {
        cout << a[i];
        if(i!=a.size()-1) cout << ", ";
    }
    cout << endl;
}

int main(void)
{
    //벡터의 초기 크기를 n으로 설정
    int n = 5;
    vector<int> vec_int(n, 3);
    cout << "vec_int(n, 3), n = 5 : ";
    vec_int.erase(vec_int.begin(), vec_int.begin()+2);
    pprint(vec_int);


    vector<string> vec_string;



    return 0;
}