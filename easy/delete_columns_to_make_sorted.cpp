#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> result;
        
        for (int i = 0; i < nums.size(); i++) {
            int indices = index[i];
            auto it = result.begin() + indices;
            result.insert(it, nums[i]);
        }
        
        return result;
    }
};