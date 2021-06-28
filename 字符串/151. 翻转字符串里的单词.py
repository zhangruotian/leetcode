
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '
# built-in API

class Solution:
    def reverseWords(self, s: str) -> str:
        res=''
        word=''
        reversed_s=''
        for c in s:
            reversed_s=c+reversed_s
        s=reversed_s

        for i in range(len(s)):
            if s[i]!=' ':
                if word and s[i-1]==' ':
                    res+=word+" "
                    word=s[i]
                else:
                    word=s[i]+word
        res+=word
        return res
# 先整个反转字符串，再翻转每一个单词。 时间O(n)，空间O(n)。