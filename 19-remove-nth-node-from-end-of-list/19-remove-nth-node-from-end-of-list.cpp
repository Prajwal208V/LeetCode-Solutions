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
  int lengthFun(ListNode * head){
    int n=0;
    while(head!=NULL){
      head=head->next;
      n++;
    }
    return n;
  }
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
      int len=lengthFun(head);
      if(n==1 && len==1){
        return head->next;
      }
      int leftSize=len-n-1;
      ListNode *lastNode=head;
      while(leftSize-- && lastNode!=NULL){
        lastNode=lastNode->next;
      }
      if(len==n){
        return head->next;
      }
      lastNode->next=lastNode->next->next;
      
      return head;
    }
};