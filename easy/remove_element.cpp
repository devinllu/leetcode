#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        if (nums.size() == 0) {
            return 0;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            if (val == nums[i]) {
                nums.erase(nums.begin() + i);
                i--;
            }
        }
        
        return nums.size();
        
    }
};