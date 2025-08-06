class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)+1
        while l<r:
            k = (l+r-1)//2
            h_k = sum([math.ceil(pile/k) for pile in piles])
            if h_k<=h:
                r=k
            if h_k>h:
                l=k+1
        return r
#二分查找来寻找吃香蕉的最低速度 k。
#它首先确定一个可能的速度范围（从1到最大香蕉数），然后不断测试这个范围的中间速度。
#如果该速度能让 Koko 在规定时间内吃完，就尝试更慢的速度（缩小范围到低速区）；如果不能，就必须提速（缩小范围到高速区），最终高效地锁定满足条件的最小速度。
#注意当刚好能吃完的时候也要尝试减小k，因为k减小后需要的时间可能还是没变。相当于一个lower bound的问题。
