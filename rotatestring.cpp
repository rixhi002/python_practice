#include <bits/stdc++.h>
using namespace std;
class Solution{
    public:
    bool rotate(string s,string goal)
    {
        if(s.length()!=goal.length())
            return false;
        string shifted=s+s;
        return shifted.find(goal)!=std:;string::npos;
    }
};
int main()
{
    string s,goal;
    getline(cin,s);
    getline(cin,goal);
    Solution obj;
    cout<<obj.rotate(s,goal);
    return 0;

}