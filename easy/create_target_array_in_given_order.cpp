#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int findLucky(vector<int>& arr) {
        
        if (arr.empty()) {
            return -1;
        }
        
        std::map<int, std::vector<int> >mp;
        int max = -1;
        
        for (int i = 0; i < arr.size(); i++) {
            int val = arr[i];
            
            mp[val].push_back(val);
        }
        
        for (const auto &p : mp) {
            if (p.first == p.second.size()) {
                if (p.first > max) {
                    max = p.first;
                }
            }
        }
        
        return max;
        
    }
};