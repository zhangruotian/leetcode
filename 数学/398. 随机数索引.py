class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums


    def pick(self, target: int) -> int:
        cnt,res=0,-1
        for i in range(len(self.nums)):
            if self.nums[i]==target:
                cnt+=1
                if cnt==1 or random.randint(1,cnt)==1:
                    res=i
        return res

#蓄水池采样 T:o(n) S:(1)
#https://www.youtube.com/watch?v=SnlxL5_LF7g
#https://leetcode-cn.com/problems/random-pick-index/solution/xu-shui-chi-chou-yang-wen-ti-by-an-xin-9/