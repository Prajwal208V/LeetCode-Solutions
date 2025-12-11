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
13function insertionSortList(head: ListNode | null): ListNode | null {
14  const dummy = new ListNode(0)
15  let cur = head
16  let prev = dummy
17  while (cur) {
18    const next = cur.next
19    if (prev.next && prev.next.val > cur.val) prev = dummy
20    while (prev.next && prev.next.val < cur.val) prev = prev.next
21    cur.next = prev.next
22    prev.next = cur
23    cur = next
24  }
25  return dummy.next
26}