1/**
2 * Definition for singly-linked list.
3 * class ListNode {
4 *     val: number
5 *     next: ListNode | null
6 *     constructor(val?: number, next?: ListNode | null) {
7 *         this.val = (val===undefined ? 0 : val)
8 *         this.next = (next===undefined ? null : next)
9 *     }
10 * }
11 */
12
13function sortList(head: ListNode | null): ListNode | null {
14    if (!head || !head.next) return head;
15    
16    let slow: ListNode | null = head;
17    let fast: ListNode | null = head.next;
18    
19    while (fast && fast.next) {
20        slow = slow!.next;
21        fast = fast.next.next;
22    }
23    
24    const mid = slow!.next;
25    slow!.next = null;
26    
27    const left = sortList(head);
28    const right = sortList(mid);
29    
30    return merge(left, right);
31}
32
33function merge(l1: ListNode | null, l2: ListNode | null): ListNode | null {
34    const dummy = new ListNode(0);
35    let cur = dummy;
36    
37    while (l1 && l2) {
38        if (l1.val < l2.val) {
39            cur.next = l1;
40            l1 = l1.next;
41        } else {
42            cur.next = l2;
43            l2 = l2.next;
44        }
45        cur = cur.next;
46    }
47    
48    cur.next = l1 ? l1 : l2;
49    return dummy.next;
50}
51