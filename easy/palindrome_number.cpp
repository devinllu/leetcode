#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string orig = std::to_string(x);
        string result = "";
        
        for(int i = orig.length() - 1; i >= 0; i--){
            result += orig[i];
        }
        
        if(orig == result){
            return true;
        }
        
        return false;
    }
};