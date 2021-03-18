class Solution:

    def __init__(self, nums: List[int]):
        self.original=nums[:]
        self.shuf=nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.shuf)):
            rand=random.randint(i,len(self.shuf)-1)
            self.shuf[i],self.shuf[rand]=self.shuf[rand],self.shuf[i]
        return self.shuf





# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

#官方解答