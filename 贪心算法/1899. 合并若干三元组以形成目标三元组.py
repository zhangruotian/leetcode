class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = False, False, False
        ta,tb,tc = target
        for a,b,c in triplets:
            if a==ta and b<=tb and c<=tc:
                first=True
            if b==tb and a<=ta and c<=tc:
                second=True
            if c==tc and a<=ta and b<=tb:
                third=True
            if first and second and third:
                return True
        return False

# 对于a来说，要有a==ta，并且b,c都要<=tb,tc，这时候证明找到了可用的a。对于b，c来说也是同样的过程。
