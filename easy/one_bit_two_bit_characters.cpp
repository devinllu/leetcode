#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        
        if (bits[bits.size() - 1] == 1) {
            return false;
        } 
        
        bool result = false;
        for (int i = 0; i < bits.size(); i++) {
            int current = bits[i];
            
            if (current == 0) {
                if (i == bits.size() - 1) {
                    result = true;
                }
            } else {
                if ((i + 1) == bits.size() - 1) {
                    if (bits[i + 1] == 0) {
                        result = false;
                        break;
                    }
                } 
                
                i++;
            }
        }
        
        return result;
    }
};