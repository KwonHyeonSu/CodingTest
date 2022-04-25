#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>

using namespace std;

template <typename T>
void pprint(T v)
{
    for(int i=0;i<v.size();i++)
    {
        cout << v[i] << ", ";
    }
}

vector<string> split(string str, char delimetor)
{
    istringstream ss(str);
    string stringBuffer;
    vector<string> ret;

    while(getline(ss, stringBuffer, delimetor)) ret.push_back(stringBuffer);

    return ret;
}

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer;
    map<string, vector<string>> reportMap;
    map<string, int> reportedMap;
    vector<string>::iterator iter;
    map<string, vector<string>>::iterator iter2;
    map<string, int>::iterator iter3;

    stable_sort(report.begin(), report.end());
    report.erase(unique(report.begin(), report.end()), report.end());

    for(iter = report.begin();iter != report.end(); iter++)
    {
        auto splited = split(*iter, ' ');
        reportMap[splited[0]].push_back(splited[1]);
        reportedMap[splited[1]] += 1;
    }

    for(iter3 = reportedMap.begin(); iter3 != reportedMap.end(); iter3++)
    {
        if(iter3->second < k)
        {
            iter3->second = -1;
        }
    }

    for(int i=0;i<id_list.size();i++)
    {
        if(reportMap.count(id_list[i]) > 0)
        {
            vector<string> tmp = reportMap[id_list[i]];
            int cnt = 0;
            for(int j=0;j<tmp.size();j++)
            {
                map<string, int>::iterator iter5;
                
                for(iter5 = reportedMap.begin(); iter5 != reportedMap.end(); iter5++)
                {
                    if(tmp[j] == iter5->first && iter5->second != -1)
                    {
                        cnt++;
                    }
                }
            }
            answer.push_back(cnt);
        }

        else{
            answer.push_back(0);
        }
    }

    //pprint(answer);

    return answer;
}

int main(void)
{
    string _id_list []= {"muzi", "frodo", "apeach", "neo"};
    string _report []= {"ryan con", "ryan con", "ryan con", "ryan con"};
    int k = 2;

    vector<string> id_list;
    vector<string> report;

    for(int i=0; i<sizeof(_id_list)/sizeof(_id_list[0]); i++)
        id_list.push_back(_id_list[i]);
    for(int i=0;i<sizeof(_report) / sizeof(_report[0]); i++)
        report.push_back(_report[i]);
/*
    pprint(id_list);
    cout << endl << endl;
    pprint(report);*/

    solution(id_list, report, k);

    return 0;
}