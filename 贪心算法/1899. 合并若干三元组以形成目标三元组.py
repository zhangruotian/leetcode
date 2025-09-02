class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1,t2,t3 = target
        v1,v2,v3 = 0,0,0
        for triplet in triplets:
            tp1,tp2,tp3 = triplet
            if tp1>t1 or tp2>t2 or tp3>t3:
                continue
            v1,v2,v3 = max(v1,tp1),max(v2,tp2),max(v3,tp3)
        return [v1,v2,v3]==target

# triplet的三个元素中有任何一个比target中对应的元素大，这个元素一定不是有用的，跳过
# 剩余的triplets中，看所有triplets的第一个元素的最大值是不是target，看第二个最大，第三个最大，如果都是返回true
