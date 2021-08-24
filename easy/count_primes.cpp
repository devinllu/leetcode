#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isPrime(int n) {
        if (n == 2) {
            return true;
        }
        
        if (n % 2 == 0) {
            return false;
        }
        
        for (int i = 3; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        
        return true;
    }
    int countPrimes(int n) {
        int counter = 0;
        
        if (n < 3) {
            return counter;
        }
        
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                counter++;
            }
        }
        
        return counter;
    }
};