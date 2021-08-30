/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <iostream>
#include <vector>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
 
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<int> pVec;
        vector<int> qVec;
        
        storeValues(pVec, p);
        storeValues(qVec, q);
        
        if (pVec.size() != qVec.size()) {
            return false;
        }
        
        for (int i = 0; i < pVec.size(); i++) {
            if (pVec[i] != qVec[i]) {
                return false;
            }
        }
        
        return true;
    }
    
    void storeValues(vector<int> &vec, TreeNode* root) {
        if (root == nullptr) {
            vec.push_back(-1);
            return;
        }
        
        vec.push_back(root->val);
        storeValues(vec, root->left);
        storeValues(vec, root->right);
        
        
    }
};