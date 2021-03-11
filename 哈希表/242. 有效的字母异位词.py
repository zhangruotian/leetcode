class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        for x in s:
            if x not in hashmap:
                hashmap[x]=1
            else:
                hashmap[x]+=1
        for x in t:
            if x in hashmap:
                hashmap[x]-=1
            else:
                hashmap[x]=1
        for x in hashmap.values():
            if x!=0:
                return False
        return True