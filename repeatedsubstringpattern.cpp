#include <bits/stdc++.h>
using namespace std;
class Solution{
    public:
    bool repeated(string s)
    {
        int n=s.length();
        for(int i=1;i<=n/2;i++)
        {
            if(n%i==0)
            {
                string substring =s.substr(0,i);
                string repeated;
                for(int j=0;j<n/i;j++)
                {
                    repeated+=substring;
                }
                if (repeated==s)
                    return true;
            }
            }
            return false;
        }
    };
int main()
{
    string s;
    getline(cin,s);
    Solution obj;
    bool ans=obj.repeated(s);
    cout<<ans;
    return 0;
}
