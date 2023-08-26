#include <bits/stdc++.h>
#include <cctype>
using namespace std;
class Solution{
    public:
    bool ispalindrome(string s)
    {
        int left=0;
        int right=s.length()-1;
        while(left<right)
        {
            while(left<right && !isalnum(s[left]))
            {
                left++;
            }
            while(left<right && !isalnum(s[right]))
            {
                right--;
            }
            if(tolower(s[left])!=tolower(s[right]))
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
        }
    };

int main()
{
    string s;
    getline(cin,s);
    Solution obj;
    bool ans=obj.ispalindrome(s);
    cout<<ans;
    return 0;
}