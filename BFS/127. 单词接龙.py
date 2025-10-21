from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        visited = {word:False for word in wordList}
        alpha= list(map(chr,range(ord('a'),ord('z')+1)))
        if endWord not in wordSet:
            return 0
        cnt = 1
        q = deque()
        q.append(beginWord)
        visited[beginWord] = True
        while q:
            for _ in range(len(q)):
                popped = q.popleft()
                for next_word in self.get_next_word(popped,visited,wordSet,alpha):
                    if next_word==endWord:
                        return cnt+1
                    q.append(next_word)
                    visited[next_word]=True
            cnt+=1
        return 0

    def get_next_word(self,popped,visited,wordSet,alpha):
        next_words = []
        for i in range(len(popped)):
            for al in alpha:
                new_word = popped[:i] + al + popped[i+1:]
                if new_word in wordSet and not visited[new_word]:
                    next_words.append(new_word)
        return next_words
# DFS适用于沿着一条路track完整的路径path，并且用visited保证这条路径不重复添加word。DFS一般要走完整个图/树才能知道结果。本题让找最短的，因此适合BFS,因为在某层找到符合要求的endWord就可以停止了。

