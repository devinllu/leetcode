#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    char findTheDifference(string s, string t) {
        
        if (s.empty()) {
            return t[0];
        }
    
        
        std::map<char, std::vector<char> >mp;
        
        for (const auto& p : s) {
            mp[p].push_back(p);
        }
        
        for (const auto& p : t) {
            mp[p].push_back(p);
        }
        
        for (const auto& p : mp) {
            if (p.second.size() % 2 != 0) {
                return p.first;
            }
        }
        
        return '\0';
        
    }
};