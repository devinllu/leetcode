#include <iostream>
#include <vector>

using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if (head == NULL) {
            return NULL;
        }
        
        ListNode* nextNode = head->next;
        if (head->val == val) {
            head = NULL;
        }
        
        return recurseRemove(head, nextNode, head, val);
    }
    
    ListNode* recurseRemove(ListNode* first, ListNode* head, ListNode* prev, int val) {
        if (head == NULL) {
            return first;
        }
        
        ListNode* nextNode = head->next;
        if (head->val == val) {
            head = NULL;
            if (prev != NULL) {
                prev->next = nextNode;
            }
        } else {
            prev = head;
            if (first == NULL) {
                first = head;
            }
        }
        
        return recurseRemove(first, nextNode, prev, val);
    }
};