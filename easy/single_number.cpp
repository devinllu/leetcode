#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        int ret = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            ret = ret ^ nums[i];

        }
        
        return ret;
        
        
    }
};