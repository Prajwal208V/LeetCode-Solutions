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
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *newNode;
        ListNode *result=new ListNode(-100);
        ListNode *lastNode=result;
        while(head!=NULL){
          if(head->val != val){
            newNode=new ListNode;
            newNode->val=head->val;
            lastNode->next=newNode;
            lastNode=newNode;     
          }
          head=head->next;
        }
        return result->next;
    }
};