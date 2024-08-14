# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            rand49 = (rand7()-1)*7+rand7()
            if rand49<=40:
                return rand49%10+1
            else:
                rand63 = (rand49%10-1)*7+rand7()
                if rand63<=60:
                    return rand63%10+1
                else:
                    rand21 = (rand63%10-1)*7+rand7()
                    if rand21<=20:
                        return rand21%10+1


            #https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/xiang-xi-si-lu-ji-you-hua-si-lu-fen-xi-zhu-xing-ji/
