1function copyRandomList(head: Node | null): Node | null {
2  if (!head) return null
3  let cur: Node | null = head
4  while (cur) {
5    const copy = new Node(cur.val)
6    copy.next = cur.next
7    cur.next = copy
8    cur = copy.next
9  }
10  cur = head
11  while (cur) {
12    if (cur.random) cur.next!.random = cur.random.next
13    cur = cur.next!.next
14  }
15  cur = head
16  const newHead = head.next!
17  while (cur) {
18    const copy = cur.next!
19    cur.next = copy.next
20    copy.next = copy.next ? copy.next.next : null
21    cur = cur.next
22  }
23  return newHead
24}