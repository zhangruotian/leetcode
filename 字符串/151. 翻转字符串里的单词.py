
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '
# built-in API

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s[::-1]
        word=''
        words=''
        for i,c in enumerate(s):
            if c !=' ':
                if s[i-1] ==' ' and word:
                    words+=word+' '
                    word=c
                else:
                    word=c+word
        words+=word
        return words
# 先整个反转字符串，再翻转每一个单词。 时间O(n)，空间O(n)。