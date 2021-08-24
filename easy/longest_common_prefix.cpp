#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string result = "";
        
        if (strs.size() == 0) {
            return result;
        }
        
        if (strs.size() == 1) {
            return strs[0];
        }
        
        string first = strs[0];
        bool failed = false;
        
        for (int i = 0; i < first.size(); i++) {
            for (int j = 1; j < strs.size(); j++) {
                string current = strs[j];
                
                if (first[i] != current[i]) {
                    failed = true;
                }
            }
            if (failed) {
                break;
            }
            result += first[i];
        }
        
        return result;
        
    }
};