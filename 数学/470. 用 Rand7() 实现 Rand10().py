# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rand1=(rand7()-1)*7+rand7()
        while True:
            if rand1<=40:
                return rand1%10+1
            rand2=((rand1-41)%10)*7+rand7()
            if rand2<=60:
                return rand2%10+1
            rand3=((rand2-61)%10)*7+rand7()
            if rand3<=20:
                return rand3%10+1

            

        

        

        #https://www.youtube.com/watch?v=Wyauxe92JJA
        #https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/xiang-xi-si-lu-ji-you-hua-si-lu-fen-xi-zhu-xing-ji/