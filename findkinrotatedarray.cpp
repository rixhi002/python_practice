#include <bits/stdc++.h>
using namespace std;
class Solution{
    public:
    int search(vector <int>&nums,int target)
    {
        int left=0;
        int right=nums.size()-s;
        while(left<=right)
        {
            int mid=left+(right-left)/2;
            if(nums[mid==target])
                return mid;
        }
        if(nums[left]<=nums[mid])
        {
            if(nums[left]<=target&&target<=nums[mid])
            {
                    right=mid-1;
            }
            else left=mid+1;
        }
        else
        {
            if(nums[mid]<=target&&target<=nums[right])
                left=mid+1;
            else right=mid-1;
        }
        return -1;
    }

};
int main()
{
    int n,t,a;
    vector <int> arr;
    cin>>n>>t;
    for(int i=;i<n;i++)
    {
        cin>>a;
        arr.push_back(a);
    }
    Solution obj;
    int ans=obj.search(arr,t);
    cout<<ans;
    return 0;
}