from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        q = deque([beginWord])
        n = len(wordList)
        wordSet = set(wordList)
        alphas = list(map(chr,range(ord('a'),ord('z')+1)))
        for i in range(n+1):
            if not q:
                return 0
            for _ in range(len(q)):
                popped = q.popleft()
                if popped == endWord:
                    return i+1
                for next_word in self.find_next_words(popped,wordSet,alphas):
                    q.append(next_word)
                    wordSet.remove(next_word)
        return 0
    
    def find_next_words(self,popped,wordSet,alphas):
        next_words = []
        for i in range(len(popped)):
            for c in alphas:
                if c==popped[i]:
                    continue
                maybe_next = popped[:i]+c+popped[i+1:]
                if maybe_next in wordSet:
                    next_words.append(maybe_next)
        return next_words
# DFS适用于沿着一条路track完整的路径path，并且用visited保证这条路径不重复添加word。DFS一般要走完整个图/树才能知道结果。本题让找最短的，因此适合BFS,因为在某层找到符合要求的endWord就可以停止了。
# BFS过程中注意中，不需要知道某个word是上层谁的child。可以去重保障q上无duplicates，而且无上层已访问过的word，因为最终的结果肯定是没有重复word的。
# https://www.youtube.com/watch?v=hB_nYXFtwP0
