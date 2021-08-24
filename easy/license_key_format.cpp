#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
        if (K <= 0) {
            return "";
        }
        
        string result = "";
        
        for (char c : S) {
            if (c != '-') {
                
                result += toupper(c);
            }
        }
        
        int groups = result.size() % K;
        if (groups == 0) {
            groups = K;
        }
        string newResult = "";
        
        for (char c : result) {
            if (groups != 0) {
                groups--;
                newResult += c;
            } else {
                newResult += '-';
                newResult += c;
                groups = K - 1;
            }
        }
        
        return newResult;
    }
};