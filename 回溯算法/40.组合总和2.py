class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res,path,visited = [],[],[False]*len(candidates)
        self.dfs(candidates,target,path,res,0,0,visited)
        return res
    
    def dfs(self,candidates,remain,path,res,index,level,visited):
        if remain<0:
            return
        if remain==0:
            res.append(path[:])
            return
        for i in range(index,len(candidates)):
            if i-1>=0 and candidates[i]==candidates[i-1] and not visited[i-1]:
                continue
            path.append(candidates[i])
            visited[i] = True
            self.dfs(candidates,remain-candidates[i],path,res,i+1,level+1,visited)
            path.pop()
            visited[i] = False

#与39题不同之处：
#不能重复使用candidates里面的元素，因此self.backTrack(candidates,target-candidates[i],path,res,i+1,visited) i+1保证下层的决策不包含上个元素
# candidates中有重复 ，所以排序后使用visited跳过
# [1 2 5 2]找和为5的，第二个2不能回头取1(会与1 2重复)因此与39题一样用index保证只能往后取。
