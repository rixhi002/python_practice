#include <bits/stdc++.h>
using namespace std;
class Solution{
    public:
    bool search(vector <vector<int>>&matrix,int target)
    {
        int n=matrix.size();
        int m=matrix[0].size();
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(matrix[i][j]==target)
                    return true;
            }
        }
        return false;
    }
};
int main()
{
    int n,m,target;
    cin>>n>>m;
    cin>>target;
    vector <vector<int>> arr(n,vector<int>(m,0));
    for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>arr[i][j];
            }
        }
        Solution obj;
        bool ans=obj.search(arr,target);
        cout<<ans;
        return 0;
}