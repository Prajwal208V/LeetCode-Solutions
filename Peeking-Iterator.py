1# Below is the interface for Iterator, which is already defined for you.
2#
3# class Iterator:
4#     def __init__(self, nums):
5#         """
6#         Initializes an iterator object to the beginning of a list.
7#         :type nums: List[int]
8#         """
9#
10#     def hasNext(self):
11#         """
12#         Returns true if the iteration has more elements.
13#         :rtype: bool
14#         """
15#
16#     def next(self):
17#         """
18#         Returns the next element in the iteration.
19#         :rtype: int
20#         """
21class PeekingIterator:
22    def __init__(self, iterator):
23        self.iterator = iterator
24        self._next = None
25        self._has_next = False
26        if iterator.hasNext():
27            self._next = iterator.next()
28            self._has_next = True
29
30    def peek(self):
31        return self._next
32
33    def next(self):
34        val = self._next
35        if self.iterator.hasNext():
36            self._next = self.iterator.next()
37            self._has_next = True
38        else:
39            self._has_next = False
40            self._next = None
41        return val
42
43    def hasNext(self):
44        return self._has_next
45
46# Your PeekingIterator object will be instantiated and called as such:
47# iter = PeekingIterator(Iterator(nums))
48# while iter.hasNext():
49#     val = iter.peek()   # Get the next element but not advance the iterator.
50#     iter.next()         # Should return the same value as [val].