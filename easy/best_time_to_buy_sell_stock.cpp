#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        if (prices.size() < 1) {
            return 0;
        }
        
        int min = prices[0];
        int minIndex = 0;
        
        int max = prices[0];
        int maxIndex = 0;
        int profit = 0;
        for (int i = 0; i < prices.size(); i++) {
            
            if (prices[i] < min) {
                min = prices[i];
                max = prices[i];
                maxIndex = i;
                minIndex = i;
            }
            
            if (prices[i] > max && maxIndex >= minIndex) {
                max = prices[i];
                maxIndex = i;
            }
            
            int newProfit = max - min;
            
            if (newProfit > profit) {
                profit = newProfit;
            }
            
        }
        
        return profit;
        
        
    }
};