#include <bits/stdc++.h>
using namespace std;
class Solution{
    public:
    int stairs(int n)
    {
        if(n==0||n==1)
            return 1;
        int prev=1,curr=1;
        for(int i=2;i<=n;i++)
        {
            int temp=curr;
            curr=curr+prev;
            prev=temp;
        }
        return curr;
    }
};
int main()
{
    int n;
    cin>>n;
    Solution obj;
    cout<<"The stairs can  be climbed in: "<<obj.stairs(n);
    return 0;
}