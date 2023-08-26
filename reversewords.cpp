#include <bits/stdc++.H>
#include <sstream>
using namespace std;
class Solution{
    public:
    string reverseWords(string s)
    {
        stringstream ss(s);
        string word;
        vector <string> words;
        while(ss >> word)
        {
            words.push_back(word);
        }
        reverse(words.begin(),words.end());
    stringstream reversed;
    for(const string &w: words)
    {
        if(!reversed.str().empty())
            reversed << " ";
    reversed << w;
    }
    return reversed.str();
    }
};
int main()
{
    string s;
    getline(cin,s);
    Solution obj;
    string ans=obj.reverseWords(s);
    cout<<ans<<endl;
    return 0;

}