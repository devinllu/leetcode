#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        if (nums.size() == 1) {
            return 0;
        }
        
        int index = 0;
        int max = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > max) {
                max = nums[i];
                index = i;
            }
        }
        
        int secondMax = -1;
        
        for (auto elem : nums) {
            if (elem > secondMax) {
                if (elem != max) {
                    secondMax = elem;
                }
            }
        }
        
        if (max >= (secondMax * 2)) {
            return index;
        }
        
        return -1;
        
        
        
    }
};