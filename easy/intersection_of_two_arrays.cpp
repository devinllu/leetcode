#include <iostream>
#include <vector>
#include <set>

using namespace std;


class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s;
        vector<int> results;
        
        for (auto i : nums1) {
            for (auto j : nums2) {
                if (i == j) {
                    s.insert(i);
                    break;
                }
            }
        }
        
        for (auto a : s) {
            results.push_back(a);
        }
        
        return results;
    }
};