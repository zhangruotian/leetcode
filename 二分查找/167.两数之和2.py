class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        hashmap[target-numbers[0]]=0
        for i in range(1,len(numbers)):
            if numbers[i] in hashmap:
                return [hashmap[numbers[i]]+1,i+1]
            else:
                hashmap[target-numbers[i]]=i
# hashmap tc:O(n) sc:O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1
# 顺序array，头尾双指针。需要增大l++，减小r--
# tc:O(n) sc:O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l=i+1
            r=len(numbers)
            while l<r:
                m=(l+r-1)//2
                if numbers[m]==target-numbers[i]:
                    return [i+1,m+1]
                elif numbers[m]<target-numbers[i]:
                    l=m+1
                else:
                    r=m
# 顺序array，二分查找。固定一个数nums[i]，从其右侧二分查找target-nums[i].
# tc:O(nlogn) sc:O(1)