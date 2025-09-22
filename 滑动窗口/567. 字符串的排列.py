from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        len1,len2 = len(s1),len(s2)
        if len1>len2:
            return False
        for i in range(len1):
            if s2[i] in s1_count:
                s1_count[s2[i]]-=1
        if not any(s1_count.values()):
            return True
        for i in range(len1,len2):
            if s2[i] in s1_count:
                s1_count[s2[i]]-=1
            if s2[i-len1] in s1_count:
                s1_count[s2[i-len1]]+=1
            if not any(s1_count.values()):
                return True
        return False
                    
# 哈希表（Counter）作为“账本”，记录目标字符串 s1 的字符“欠条”。
# 初始化账本：用 s1 初始化 Counter，记录需要匹配的所有字符及其数量。

# 处理初始窗口：
# 遍历 s2 的第一个窗口，每遇到一个字符，就在“账本”上将其数量减一（表示“偿还”了一个字符）。

# 滑动窗口并更新账本：
# 窗口向右滑动一格。
# 新字符进入：在账本上减一（继续“偿还”）。
# 旧字符离开：在账本上加一（表示之前“偿还”的这个字符不算了，重新“欠下”）。

# 判断条件：在每一步滑动后，检查账本。如果账本里所有字符的欠账都正好为 0，说明当前窗口完美“还清”了所有“欠条”，即找到了一个排列。
