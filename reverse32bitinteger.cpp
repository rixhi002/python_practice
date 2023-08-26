#include <bits/stdc++.h>
using namespace std;
class Solution{
    public:
    int reverse(int n)
    {
        int res=0;
        while(n!=0)
        {
            if(res>INT_MAX/10||res<INT_MIN/10)//to check overflow before updating res
                return 0;
            
            int digit=n%10;
            n=n/10;
            res=res*10+digit;
        }
        return res;
    }
};
int main()
{
    int n;
    cin>>n;
    Solution obj;
    cout<<"The reverse is :"<<obj.reverse(n);
    return 0;
}