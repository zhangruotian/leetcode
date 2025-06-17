class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            d[self.strs_to_count(word)].append(word)
        return list(d.values())
    
    def strs_to_count(self,strs):
        res = [0]*26
        for c in strs:
            res[ord(c)-ord('a')] += 1
        return tuple(res)

  #用tuple代替hashtable，因为mutable不能作为d字典的key。
