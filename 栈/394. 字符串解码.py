class Solution:
    def decodeString(self, s: str) -> str:
            # 100[200[a]]
        stack1,stack2=[],[]
        multi=''
        for c in s:
            if c.isdigit():
                multi+=c 
            elif c.isalpha():
                stack2.append(c)
            elif c=='[':
                stack1.append(int(multi))
                multi=''
                stack2.append(c)
            else:
                sub=''
                while True:
                    tmp=stack2.pop()
                    if tmp=='[':
                        break
                    sub=tmp+sub
                tmp_num=stack1.pop()
                sub*=tmp_num
                stack2.append(sub)
        return ''.join(stack2)

# 两个栈，一个记录数字，一个记录字母和'['.遇到右括号时候弹出一个数字栈，字母栈弹到左括号为止.（把数字和字母对应起来）
#注意数字可能是多位数，用字符串multi记录。遇到'['时将其压人字母栈，清空multi