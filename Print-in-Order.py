1class Foo:
2    def __init__(self):
3        from threading import Lock
4        self.first_done = Lock()
5        self.second_done = Lock()
6        self.first_done.acquire()
7        self.second_done.acquire()
8
9
10    def first(self, printFirst: 'Callable[[], None]') -> None:
11        
12        # printFirst() outputs "first". Do not change or remove this line.
13        printFirst()
14        self.first_done.release()
15
16
17    def second(self, printSecond: 'Callable[[], None]') -> None:
18        
19        # printSecond() outputs "second". Do not change or remove this line.
20        self.first_done.acquire()
21        printSecond()
22        self.second_done.release()
23
24    def third(self, printThird: 'Callable[[], None]') -> None:
25        
26        # printThird() outputs "third". Do not change or remove this line.
27        self.second_done.acquire()
28        printThird()