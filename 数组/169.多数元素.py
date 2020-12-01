class Solution:
    def majorityElement(self, nums): 
        count=0
        candidate=0
        for num in nums:
            if count==0:
                candidate=num
                count=1
            else:
                count+=1 if num==candidate else -1
        return candidate
       
# 多数元素：在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。（找出与数组中最多元素不同，多一个条件:>n/2）
# 可以考虑用摩尔投票法，不同的元素抵消掉，剩下的必是多数元素。
# 维护count和candidate变量，从头开始遍历。
# 情况1：count为0，则把candidate设为下一个元素num, count设为1。
# 情况2：count不为0，若下一个元素num与candidate一样，则count+1；不一样，则count-1。
# 时间复杂度 O(n),空间复杂度O(1)

class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
  
# 用hashmap记录下{'element':count}，然后返回最大count的key。
# 这里用collection.Counter创建对象，Counter是dict的子类，counts对象记录了{'element':count}。
# counts对象有dict的一切方法，counts.keys()  counts.values().....
# max(a,key=) key为方程名。例如 max([1,2,-3],key=lambda x:abs(x)) 返回[1,2,-3]中绝对值最大的数。
# max(counts.keys(), key=counts.get) 
# counts.keys()要返回的东西
# counts.get(0)=counts[0] value
# max(counts.keys(), key=counts.get) 返回最大的value对应的key