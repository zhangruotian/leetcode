class Solution:
    def checkValidString(self, s: str) -> bool:
        max_left = 0
        min_left = 0
        for c in s:
            if c =='(':
                max_left+=1
                min_left+=1
            elif c== ')':
                max_left-=1
                min_left-=1
            else:
                max_left+=1
                min_left-=1
            if max_left<0:
                return False
            if min_left<0:
                min_left=0
        return min_left==0
# max_left：假设'*'是'('，到此为止左侧最多的左括号数量，如果<0，说明右括号太多，没能力match，返回false，比如(*)))
# min_left: 假设'*'是')'，到此为止左侧最少的左括号数量，如果<0，说明把前面的'*'都当作')'有点过了。把min_left=0，因为可以把前面的'*'改成空格或者'('，说明到目前为止可以
# perfect match，往后接着看。如果后面(或者从一开始到现在)，min_left一直>0，说明左括号太多了，匹配不完，返回false，比如(((*)。

class Solution:
    def checkValidString(self, s: str) -> bool:
        num_left,num_star = 0,0
        for c in s:
            if c=='(':
                num_left+=1
            elif c==')':
                num_left-=1
            else:
                num_star+=1
            if num_left+num_star<0:
                return False
        num_right,num_star = 0,0
        for c in s[::-1]:
            if c=='(':
                num_right-=1
            elif c==')':
                num_right+=1
            else:
                num_star+=1
            if num_right+num_star<0:
                return False
        return True
# 双向扫描，从左往右检查先出现')'导致失败的情况，从右往左检查先出现'('导致失败的情况。
