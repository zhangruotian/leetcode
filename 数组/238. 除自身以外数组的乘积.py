class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left =    [1,2,6,24]
        # right = [24,24,12,4]

        # res = [1,1,2,6]
        # res = [1*24,1*12,2*4,6]
        res = [1]*len(nums)
        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*suffix
            suffix = suffix*nums[i]
        return res
            
# 第一趟遍历：从左到右，计算并存储“左侧乘积”
# 目标： 让 res[i] 存储位置 i 左边所有元素的累积乘积。
# 做法： 初始化一个 res 数组全为1。从左到右遍历，res[i] 的值由 res[i-1] 和 nums[i-1] 决定。
# 结果： 遍历结束后，res 数组里的每个值都已经是“答案的一半”了。

# 第二趟遍历：从右到左，乘以“右侧乘积”
# 目标： 将每个位置 i 缺失的“右侧乘积”部分，乘回到 res[i] 中。
# 做法： 维护一个单独的 suffix 变量，表示从右边累积过来的乘积。从右到左遍历，在每个位置 i，先用 res[i] 已有的值（左侧积）乘以 suffix（右侧积），得到最终答案。然后更新 suffix，为下一个位置做准备。
# 结果： 遍历结束后，res 数组就是我们最终的答案。

# 直观示例：nums = [1, 2, 3, 4]
# 初始化:
# res = [1, 1, 1, 1]

# 第一趟 (从左到右):
# res 依次变为:
# [1, 1, 1, 1]
# [1, 1, 2, 1]
# [1, 1, 2, 6]  <- 第一趟结束。此时 res 存储的是左侧乘积。

# 第二趟 (从右到左):
# 初始化 suffix 变量为 1 (最右元素的右侧没有数字，乘积为1)。
# i = 3: res[3] = res[3] * suffix  -> 6 * 1 = 6。   更新 suffix = 1 * 4 = 4。
# i = 2: res[2] = res[2] * suffix  -> 2 * 4 = 8。   更新 suffix = 4 * 3 = 12。
# i = 1: res[1] = res[1] * suffix  -> 1 * 12 = 12。  更新 suffix = 12 * 2 = 24。
# i = 0: res[0] = res[0] * suffix  -> 1 * 24 = 24。  更新 suffix = 24 * 1 = 24。

# 最终结果:
# res = [24, 12, 8, 6]  
        
