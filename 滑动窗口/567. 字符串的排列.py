from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        i = 0
        for j in range(len(s2)):
            if not s2[j] in cnt:
                while i<=j:
                    if s2[i] in cnt:
                        cnt[s2[i]]+=1
                    i+=1
            else:
                if cnt[s2[j]]>0:
                    cnt[s2[j]]-=1
                elif cnt[s2[j]]==0:
                    while cnt[s2[j]]==0:
                        cnt[s2[i]]+=1
                        i+=1
                    cnt[s2[j]]-=1
            if sum(cnt.values())==0:
                return True
        return False
                    
# 目标计数: 先用一个哈希表（Counter）统计出目标串 s1 中所有字符的种类和数量。
# 窗口滑动: 在长串 s2 上维护一个窗口。不断向右移动窗口的右边界 j，每经过一个字符，就将哈希表中对应的计数值减一。
# 窗口收缩: 如果出现以下情况，说明当前窗口不满足条件，需要从左边收缩窗口（移动左边界 i）：
# 1.窗口内某个字符的数量超过了 s1 所需的数量。
# 2.遇到了一个 s1 中根本不存在的字符。
# 判断条件: 当哈希表中所有字符的计数值都恰好为 0 时，意味着当前窗口内的字符串就是 s1 的一个排列，任务完成。

# 窗口收缩的逻辑：
# 当遇到一个s1中没有的字符时：
# 这说明当前窗口不可能构成排列。你的代码会直接放弃整个窗口，将左指针i移动到这个无关字符的下一个位置，并把窗口内所有字符的计数都“还”回去。

# 当窗口中某个所需字符的数量已经超了：
# 你的代码会从左侧开始收缩窗口（i++），把移出窗口的字符计数“还”回去，直到多余的那个字符被移出去了，才把当前这个新字符s2[j]加入窗口。
