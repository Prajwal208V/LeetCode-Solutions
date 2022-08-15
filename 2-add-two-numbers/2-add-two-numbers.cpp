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
  vector <int> reversFun(ListNode *head1,ListNode *head2){
    vector<int> arr1;
    vector<int> arr2;
    while(head1!=NULL){
      arr1.push_back(head1->val);
      head1=head1->next;
    }
    while(head2!=NULL){
      arr2.push_back(head2->val);
      head2=head2->next;
    }
    
    vector<int> result;
    int carry=0;
    int n1=arr1.size();
    int n2=arr2.size();
    int i=0;
    int j=0;
    while(i<n1 && j<n2){
      int a=arr1[i++];
      int b=arr2[j++];
      int added=a+b+carry;
      carry=added/10;
      added%=10;
      result.push_back(added);
    }
   while(i<n1){
      int a=arr1[i++]+carry;
      carry=a/10;
      a%=10;
      result.push_back(a);
   }
   while(j<n2){
      int a=arr2[j++]+carry;
      carry=a/10;
      a%=10;
      result.push_back(a);
   }
   if(carry){
      result.push_back(carry);
   }
   return result;
  }
  
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      vector<int> resultList=reversFun(l1,l2);
      ListNode *head=new ListNode(resultList.size());
      ListNode *crr=head;
      for(auto i=resultList.begin();i!=resultList.end();i++){
        ListNode *Node=new ListNode;
        Node->val=*i;
        crr->next=Node;
        crr=Node;
      }
      return head->next;
    }
  
};