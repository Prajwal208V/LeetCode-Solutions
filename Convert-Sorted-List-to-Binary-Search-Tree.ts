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
13/**
14 * Definition for a binary tree node.
15 * class TreeNode {
16 *     val: number
17 *     left: TreeNode | null
18 *     right: TreeNode | null
19 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
20 *         this.val = (val===undefined ? 0 : val)
21 *         this.left = (left===undefined ? null : left)
22 *         this.right = (right===undefined ? null : right)
23 *     }
24 * }
25 */
26
27function sortedListToBST(head: ListNode | null): TreeNode | null {
28    if (!head) return null;
29    if (!head.next) return new TreeNode(head.val);
30
31    let prev: ListNode | null = null;
32    let slow: ListNode | null = head;
33    let fast: ListNode | null = head;
34
35    while (fast && fast.next) {
36        prev = slow;
37        slow = slow!.next;
38        fast = fast.next.next;
39    }
40
41    if (prev) prev.next = null;
42
43    const root = new TreeNode(slow!.val);
44    root.left = sortedListToBST(head === slow ? null : head);
45    root.right = sortedListToBST(slow!.next);
46
47    return root;
48}
49
50