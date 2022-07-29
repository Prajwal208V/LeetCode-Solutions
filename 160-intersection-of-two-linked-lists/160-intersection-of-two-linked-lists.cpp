/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int length(ListNode *head){
        ListNode *temp=head;
        int len=0;
        while(temp!=NULL){
          len++;
          temp=temp->next;
        }
      return len;
    }
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int len1=length(headA);
        int len2=length(headB);
        ListNode *longList;
        ListNode *shortList;
        int dif=(len1>len2)?(len1-len2):(len2-len1);
        if(len1>len2){
          longList=headA;
          shortList=headB;
        }
        else{
          longList=headB;
          shortList=headA;
        }
        while(dif--){
          longList=longList->next;
          if(longList==NULL){
            return NULL;
          }
        }
     while(longList!=NULL && shortList!=NULL){
       if(longList==shortList){
         return longList;
       }
       longList=longList->next;
       shortList=shortList->next;
     }
      return NULL;
    }
};