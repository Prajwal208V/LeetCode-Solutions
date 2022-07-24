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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
      if(list1==NULL){
        return list2;
      }
      if(list2==NULL){
        return list1;
      }
      ListNode *resultNode=NULL;
      resultNode=new ListNode;
      ListNode *last=resultNode;
      ListNode *newNode=NULL;
      while(list1!=NULL && list2!=NULL){
        newNode=new ListNode;
        if(list1->val < list2->val){
          newNode->val=list1->val;
          newNode->next=NULL;
          // cout<<newNode->val<<" ";
          last->next=newNode;
          last=newNode;
          list1=list1->next;
        }
        else if (list1->val == list2->val){
         newNode->val=list1->val;
          newNode->next=NULL;
          // cout<<newNode->val<<" ";
          last->next=newNode;
          last=newNode;
          list1=list1->next;
          newNode=new ListNode;
          newNode->val=list2->val;
          newNode->next=NULL;
          cout<<newNode->val<<" ";
          last->next=newNode;
          last=newNode;
          list2=list2->next;
        }
        else{
          newNode->val=list2->val;
          newNode->next=NULL;
          cout<<newNode->val<<" ";
          last->next=newNode;
          last=newNode;
          list2=list2->next;
        }
      }
      while(list1!=NULL){
          newNode=new ListNode;
          newNode->val=list1->val;
          newNode->next=NULL;
          // cout<<newNode->val<<" ";
          last->next=newNode;
          last=newNode;
          list1=list1->next;
      }
      while(list2!=NULL){
         newNode=new ListNode;
          newNode->val=list2->val;
          newNode->next=NULL;
          cout<<newNode->val<<" ";
          last->next=newNode;
          last=newNode;
          list2=list2->next;
      }
      return resultNode->next; 
    }
};