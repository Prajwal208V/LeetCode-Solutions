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
  int counter(ListNode *head){
    int n=0;
    while(head!=NULL){
      n++;
      head=head->next;
    }
    return n;
  }
public:
    ListNode* middleNode(ListNode* head) {
        int middle=(counter(head)/2);
        while(middle--){
          head=head->next;
        }
        return head;
    }
};