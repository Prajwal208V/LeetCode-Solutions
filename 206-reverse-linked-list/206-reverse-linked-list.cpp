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
    ListNode* reverseList(ListNode* head) {
        auto reverseNode=new ListNode;
        auto itr=reverseNode;
        ListNode *newNode=NULL;
        stack<int>s;
        while(head){
          s.push(head->val);
          head=head->next;
        }
       while(!s.empty()){
         int i=s.top();
         s.pop();
         newNode=new ListNode;
         newNode->val=i;
         newNode->next=NULL;
         itr->next=newNode;
         itr=newNode;
       }
      return reverseNode->next;
    }
};