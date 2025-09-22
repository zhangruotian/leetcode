from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0]*numCourses
        graph = defaultdict(list)
        q = deque()
        for e,s in prerequisites:
            graph[s].append(e)
            indegrees[e]+=1
        for i in range(numCourses):
            if indegrees[i]==0:
                q.append(i)
        while q:
            popped = q.popleft()
            for child in graph[popped]:
                indegrees[child]-=1
                if indegrees[child]==0:
                    q.append(child)
        return sum(indegrees)==0
# topological sort
