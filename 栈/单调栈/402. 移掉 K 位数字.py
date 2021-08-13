class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num): return '0'
        res=[]
        stack=[num[0]]
        flag=False
        for i in range(1,len(num)):
            if flag: break
            if int(num[i])>=int(stack[-1]):
                stack.append(num[i])
            else:
                while stack and int(num[i])<int(stack[-1]):
                    tmp=stack.pop()
                    k-=1
                    if k==0:
                        res=stack[:]
                        for j in range(i,len(num)):
                            res.append(num[j])
                        flag=True
                        break
                stack.append(num[i])
        for _ in range(k):
            stack.pop()
        if not res:
            res=stack[:]
        res_str=''
        for i in range(len(res)):
            if not res_str and res[i]=='0':
                continue
            res_str+=res[i]
        return res_str if res_str else '0'

# 单调栈，遇到比stack[-1]大的或相等的直接入栈，遇到小的弹出栈顶直到stack为空或者stack[-1]比这个数大。
# 去除的过程中可能已经去除k次，则把栈和num剩余的值连接起来。如果按此方式循环玩后还未到达k，则把
# stack中的元素向外pop直到=k
# 最后记得去除开头的'0'