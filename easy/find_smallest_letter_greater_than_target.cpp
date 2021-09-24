#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        
        if (letters[0] == target) {
            for (char c : letters) {
                if (c != target) {
                    return c;
                }
            }
        }
        
        for (char c : letters) {
            if (target < c) {
                return c;
            }
            
        }
        
        return letters[0];
    }
};