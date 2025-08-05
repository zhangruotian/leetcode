class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [(10,2),(8,4),(5,1),(3,3),(0,1)]
        times = [(target-p)/s for p,s in sorted(zip(position,speed),key=lambda x:x[0],reverse=True)]
        stack = []
        for i in range(len(times)):
            if not stack or times[i]>stack[-1]:
                stack.append(times[i])
        return len(stack)
# 单调栈
# 将车辆按位置（从近到远）排序后，用一个栈（Stack）来模拟：遍历车辆，若当前车到达时间比栈顶慢，则入栈形成新车队；否则合并。最终栈的大小即为车队数量。
