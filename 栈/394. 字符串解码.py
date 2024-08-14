class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                self.decode(stack)
        return ''.join(stack)
    
    def decode(self,stack):
        string = ''
        c = stack.pop()
        while c != '[':
            string = c+string
            c = stack.pop()
        
        num=''
        while stack and stack[-1].isdigit():
            c = stack.pop()
            num = c+num

        decoded = int(num)*string
        stack.append(decoded)
# stack， 遇到']' decode,遇到其他加入stack
