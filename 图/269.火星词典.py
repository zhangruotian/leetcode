class Solution:
    from collections import deque,defaultdict
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegree = {c:0 for w in words for c in w}
        res = ''
        for i in range(len(words)-1):
            worda,wordb = words[i],words[i+1]
            MIN = min(len(worda),len(wordb))
            for j in range(MIN):
                if j==MIN-1 and worda[j]==wordb[j] and len(worda)>MIN:
                    return res
                if worda[j]!=wordb[j]:
                    graph[worda[j]].append(wordb[j])
                    indegree[wordb[j]]+=1
                    break

        q = deque([char for char,count in indegree.items() if count==0])
        while q:
            popped = q.popleft()
            res+=popped
            for node in graph[popped]:
                indegree[node]-=1
                if indegree[node]==0:
                    q.append(node)
        if len(res)!=len(indegree):
            return ''
        return res
# 比较2个相邻words，可以得到directed graph的一个edge。根据所有的words建图并且维护indegree list。然后拓扑排序得到顺序。
# 注意corner cases。
# 1. ['ab','bc','cd'] 不能只输出abc，d也得输出，放到哪里都行只要不影响abc的顺序。因此初始化indegree的时候要把所有的char都初始化。
# 2. ['abc','ab'] 这种不合法，输出""
# 3. ['a','b','z','x','z'] 有环，无法合法判断顺序，输出""
