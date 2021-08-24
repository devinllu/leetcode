#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        if (n == 0) {
            return false;
        }
        
        if (n == 1) {
            return true;
        }
        
        int sum = 0;
        while (n != 0) {
            int lastDigit = n % 10;
            sum += lastDigit * lastDigit;
            
            n /= 10;
        }
        
        return happyRecur(sum, 1);
    }
    
    bool happyRecur(int n, int counter) {
        if (n == 0 || counter == 50) {
            return false;
        }
        
        if (n == 1) {
            return true;
        }
        
        int sum = 0;
        while (n != 0) {
            int lastDigit = n % 10;
            sum += lastDigit * lastDigit;
            
            n /= 10;
        }
        
        return happyRecur(sum, counter + 1);
    }
};