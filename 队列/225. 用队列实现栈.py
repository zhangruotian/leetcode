class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q=deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        tmp=self.pop()
        self.q.append(tmp)
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.q)==0:
            return True
        return False
#一个队列

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1=deque()
        self.q2=deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1)>1:
            self.q2.appendleft(self.q1.popleft())
        tmp=self.q1.popleft()
        while self.q2:
            self.push(self.q2.pop())
        return tmp

    def top(self) -> int:
        """
        Get the top element.
        """
        tmp=self.pop()
        self.q1.append(tmp)
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.q1)==0 and len(self.q2)==0:
            return True
        return False
#两个队列