#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

bool cmp(const int a, const int b)
{
    return a>b;
}

int main(void)
{
    int arr1[10000];
    vector<int> arr2[10000];
    int n = 10000;

    //sort
    //첫 원소의 주소, 마지막 원소 주소 인자로 넘겨줌
    sort(arr1, arr1+n);
    sort(arr2->begin(), arr2->end());
    //비교 함수 만들어서 같이 넘겨줄 수 있음.

    //stable_sort
    //사용법은 같음.
    stable_sort(arr1, arr1+n);

    //lower_bound 해당 값 이상인 원소가 몇번째에서 등장하는지
    //첫 원소 주소와 마지막 원소의 다음 주소와 비교할 원소를 넘겨준다.
    //구간 내의 원소들은 정렬되어있어야함
    //리턴 값은 해당 원소의 주소값이다. 없다면 arr1+n을 리턴
    //또는 arr2.end()리턴
    int index = lower_bound(arr1, arr1+n, 42) - arr1;
    cout << index << endl;

    //upper_bound
    //사용법은 같다.
    vector<int>::iterator iter = upper_bound(arr2->begin(), arr2->end(), 54);
    if(iter != arr2->end()) cout << *iter << " ";

    //max_element
    //구간내의 최대값을 가지는 원소의 주소 리턴
    cout << *max_element(arr1, arr1+n) << endl;

    //unique
    //구간내의 중복된 원소를 구간의 끝부분으로 밀어주고 마지막 원소의 다음 주소를 리턴한다.
    //구간내의 원소들은 정렬되어 있어야한다.
    //보통 erase와 함께 중복된 원소를 제거하는 방법으로 사용한다.
    //arr2.erase(unique(arr2->begin(), arr2->end()), arr2->end());

    //next_permutation
    //구간 내의 원소들의 다음 순열을 생성하고 true 리턴
    //다음 순열이 없다면 false리턴
    //구간 내의 원소들은 정렬되어 있어야한다.
    for(int i=0;i<10;i++) arr1[i] = i;

    do{
        for(int i=0;i<10;i++)
            cout << arr1[i];
        cout << endl;
    }while(next_permutation(arr1, arr1+10));

    return 0;
}