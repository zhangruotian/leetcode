#两个list
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
        
# 一个list，元素是tuple
class MinStack:
    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            min_val = min(self.stack[-1][1],val)
            self.stack.append((val,min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
#不使用额外空间
#栈里维护与最小值之间的差值
class MinStack:
    # 
    # -3.  0.  -3    
    # -3.  -1. -3
    # 0.   2. -2.   
    # -2   0  -2

    def __init__(self):
        self.stack=[]
        self.min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            diff = val-self.min
            self.stack.append(val-self.min)
            if diff<0:
                self.min = val

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop>0:
            res = pop+self.min
        if pop<=0:
            res = self.min
            self.min = self.min - pop

    def top(self) -> int:
        pop = self.stack[-1]
        return pop+self.min if pop>0 else self.min

    def getMin(self) -> int:
        return self.min
