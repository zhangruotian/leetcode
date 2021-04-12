class Solution:
    def toHex(self, num: int) -> str:
        hex="0123456789abcdef"
        res=""
        for _ in range(8):
            res=hex[num&15]+res
            num=num>>4
            if num==0:
                break
        return res
#https://segmentfault.com/a/1190000021511009
#https://www.runoob.com/w3cnote/bit-operation.html
#https://www.youtube.com/watch?v=rRLg8YjiUSI