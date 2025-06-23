class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict,deque
        in_degrees = [0]*numCourses
        graph = defaultdict(list)
        for c,p in prerequisites:
            graph[p].append(c)
            in_degrees[c]+=1
        
        q = deque()
        for i in range(numCourses):
            if in_degrees[i]==0:
                q.appendleft(i)
        while q:
            popped = q.pop()
            if popped in graph:
                for c in graph[popped]:
                    in_degrees[c]-=1
                    if in_degrees[c]==0:
                        q.appendleft(c)
        return sum(in_degrees)==0

# 算法思路：拓扑排序
# 该算法通过模拟“上课”来检测课程依赖中是否存在“死循环”。如果不存在，则可以完成所有课程。

# 关键点
# 核心数据结构:

# 入度数组 in_degrees: 记录每门课需要几门先修课。
# 邻接表 graph: 记录一门课是哪些其他课程的先修课。
# 队列 q: 存放所有当前可以上的课（即入度为0的课）。
# 执行流程:

# 开始: 找到所有入度为0的课程，放入队列。
        
# 循环:
# 从队列里取出一门课（代表已完成）。
# 将这门课解锁的所有后续课程的入度减1。
# 如果某个后续课程入度变为0，也将其放入队列。
# 结束: 直到队列为空。
        
# 结果判断:
# 检查最终是否所有课程的入度都变成了0。如果是，说明没有循环，返回 True。否则，存在循环，返回 False。

# https://www.youtube.com/watch?v=fskPWs3Nuhc
