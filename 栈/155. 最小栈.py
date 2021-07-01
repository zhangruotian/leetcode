class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min_stack=[float(inf)]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x,self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


#不使用额外空间
#栈里维护与最小值之间的差值
class MinStack:
    # 1     4.       -3
    # -3    -1.      -3
    # 0     2        -2
    # -2    0        -2
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min_val=0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val=val
        else:
            diff=val-self.min_val
            self.stack.append(diff)
            if diff<0:
                self.min_val=val
            

    def pop(self) -> None:
        diff=self.stack.pop()
        if diff>0:
            res=diff+self.min_val
        else:
            res=self.min_val
            self.min_val=self.min_val-diff
        return res


    def top(self) -> int:
        return self.stack[-1]+self.min_val if self.stack[-1]>0 else self.min_val

    def getMin(self) -> int:
        return self.min_val