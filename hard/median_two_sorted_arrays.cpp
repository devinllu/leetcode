#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len = nums1.size() + nums2.size();
        
        int m = nums1.size();
        int n = nums2.size();
        int index = len / 2;
        if(len % 2 == 1) {
            return (double) kthSmallest(nums1, nums2, index, 0, m, 0, n);
        } else {
            return ((double) kthSmallest(nums1, nums2, index, 0, m, 0, n) +
                    (double) kthSmallest(nums1, nums2, index-1, 0, m, 0, n)) / 2;
        }
        
    }
    
    int kthSmallest(vector<int> A, vector<int> B, int k, int aL, int aR, int bL, int bR) {
        if(aL == aR) return B[bL+k];
        if(bL == bR) return A[aL+k];
        else{
            int midA = (aL+aR)/2;
            int midB = (bL+bR)/2;
            int lenA = midA - aL;
            int lenB = midB - bL;

            if(A[midA] <= B[midB]){
                if(k <= lenA + lenB)
                    return kthSmallest(A, B, k, aL, aR, bL, midB);
                else
                    return kthSmallest(A, B, k-lenA-1, midA+1, aR, bL, bR);
            }
            else{
                if(k <= lenA + lenB)
                    return kthSmallest(A, B, k, aL, midA, bL, bR);
                else
                    return kthSmallest(A, B, k-lenB-1, aL, aR, midB+1, bR);
            }
        }
    }
};