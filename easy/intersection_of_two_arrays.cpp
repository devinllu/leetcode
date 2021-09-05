#include <iostream>
#include <vector>
#include <set>

using namespace std;


class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s;
        vector<int> results;
        
        for (int i = 0; i < nums1.size(); i++) {
            for (int j = 0; j < nums2.size(); j++) {
                if (nums1[i] == nums2[j]) {
                    s.insert(nums1[i]);
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