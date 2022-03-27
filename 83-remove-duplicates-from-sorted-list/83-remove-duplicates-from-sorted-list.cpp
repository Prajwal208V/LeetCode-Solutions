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
    ListNode* deleteDuplicates(ListNode* head) {
      
      if(head==NULL) 
        return head;
      
      else{
        ListNode *node1=head->next,*node2=head,*node3=head;
        while(node1!=NULL){
          if(node2->val != node1->val){
            node3->next=node1;
            node3=node3->next;

            node2=node1;
            node1=node1->next;
          }

          else
            node1=node1->next;
        }

        if(node3->next!=NULL)
            node3->next=NULL;

        return head;
      }
    }
};