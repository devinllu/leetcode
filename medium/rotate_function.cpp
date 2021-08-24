#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        int max = 0;
        int n = A.size();
        int prev = 0;
        int lastIndex = A.size();
        long total = 0;
        
        for (int i = 0; i < A.size(); i++) {
            total += A[i];
        }
            
        while (n > 0) {
            if (n == A.size()) {
                
                for (int i = 0; i < A.size(); i++) {
                    prev += A[i] * i;
                }
                max = prev;
                
            } else {
                
                int lastVal = A[lastIndex - 1];
                prev = prev + total - (lastVal * A.size());
                
                if (prev > max) {
                    max = prev;
                }
                lastIndex--;
            }
            
            n--;

            
        }
        
    
        return max;
        
        
    }
};