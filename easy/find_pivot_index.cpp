#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int pivot = -1;
        
        if (nums.size() < 1) {
            return pivot;
        }
        
        if (nums.size() == 1) {
            return 0;
        }
        
        vector<int> memo;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            memo.push_back(sum);
        }
        
        for (int i = 0; i < memo.size(); i++) {
            int leftSum = 0;
            int rightSum = 0;
            int leftIndex = i - 1;
            int rightIndex = i + 1;
            int lastValue = memo[memo.size() - 1];
            
            if (leftIndex < 0) {
                rightSum = lastValue - memo[i];
            } else if (rightIndex >= memo.size()) {
                leftSum = memo[i - 1];
            } else {
                leftSum = memo[i - 1];
                rightSum = lastValue - memo[i];
            }
            
            if (leftSum == rightSum) {
                pivot = i;
                break;
            }
        }
        
        return pivot;
        
    }
};