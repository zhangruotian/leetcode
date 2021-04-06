class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #邻接表，表示有向关系
        adjacent_list={}
        #入度，表示有多少node指向该node（本课有多少前置课）
        in_degree=[0]*numCourses
        pop_num=0
        # 邻接表和入度初始化
        for course,pre in prerequisites:
            if pre not in adjacent_list:
                adjacent_list[pre]=[course]
            else:
                adjacent_list[pre].append(course)
            in_degree[course]+=1

        #用队列维护拓扑顺序
        #把入度为0的node加入队列    
        q=deque([i for i,num in enumerate(in_degree) if num==0])
        while q:
            #dequeue
            tmp=q.popleft()
            pop_num+=1
            if tmp in adjacent_list:
                #将出队的node指向的node的入度-1.如果入度为0，加入队列
                for i in adjacent_list[tmp]:
                    in_degree[i]-=1
                    if in_degree[i]==0:
                        q.append(i)
        return pop_num==numCourses #若出队的数量与课程数量相等，则无环。若有环，环中node的的入度永不可能为0，出队数量会比课程数量少。
            
#https://www.youtube.com/watch?v=fskPWs3Nuhc