class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c:[] for word in words for c in word}
        indegrees = {c:0 for word in words for c in word}
        for i in range(len(words)-1):
            word1,word2=words[i],words[i+1]
            len_word1,len_word2 = len(word1),len(word2)
            find = False
            for j in range(min(len_word1,len_word2)):
                if word1[j]!=word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegrees[word2[j]]+=1
                    find=True
                    break
            if not find and len_word1>len_word2:
                return ''
        q = deque()
        res = ''
        for node,indegree in indegrees.items():
            if indegree==0:
                q.append(node)
        while q:
            popped = q.popleft()
            res+=popped
            for child in graph[popped]:
                indegrees[child]-=1
                if indegrees[child]==0:
                    q.append(child)
        return res if len(res)==len(indegrees) else ''

# 比较2个相邻words，可以得到directed graph的一个edge。根据所有的words建图并且维护indegree list。然后拓扑排序得到顺序。
# 注意corner cases。
# 1. ['ab','bc','cd'] 不能只输出abc，d也得输出，放到哪里都行只要不影响abc的顺序。因此初始化indegree的时候要把所有的char都初始化。
# 2. ['abc','ab'] 这种不合法，输出""
# 3. ['a','b','z','x','z'] 有环，无法合法判断顺序，输出""
