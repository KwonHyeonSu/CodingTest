// set : 균형잡힌 이진트리, 원소 삽입과 삭제, 탐색 등의 연산은 O(log n)을 보장
// map : 딕셔너리 자료구조, 원소 삽입과 삭제, 탐색 등의 연산은 O(log n)을 보장

#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main(void)
{
    map<string, int> m;

    m.insert(make_pair("a", 1));
    m.insert(make_pair("a", 2));
    m.insert(make_pair("b", 2));
    m.insert(make_pair("c", 3));

    cout << m.count("a")<<endl;
    cout << m.count("b")<<endl;



    return 0;
}