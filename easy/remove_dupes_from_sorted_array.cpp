#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }
        
        int curr = nums[0];
        int size = nums.size();
        
        for(int i = 1; i < size; i++){
            if(curr != nums[i]){
                curr = nums[i];
            } else {
                nums.erase(nums.begin() + i);
                i--;
                size--;
            }
        }
        
        return nums.size();
    }
};