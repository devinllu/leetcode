#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool rotateString(string A, string B) {
        
        int size = A.size();
        bool result = false;
        
        if (A.empty() && B.empty()) {
            return true;
        }
        
        while (size > 0) {
            
            if (A == B) {
                result = true;
                break;
            }
            
            char firstChar = A[0];
            A.erase(0, 1);
            A += firstChar;
            
            size--;
        }
        
        return result;
    }
};