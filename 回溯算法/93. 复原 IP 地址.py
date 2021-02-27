class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path,res,n=[],[],len(s)
        self.backTrack(s,path,res,0,1,n)       #需要begin记录字符串截取到哪了,需要level看有几个segment了
        return res
    
    def backTrack(self,s,path,res,begin,level,n):
        if n-begin>(5-level)*3 or n-begin<5-level:
            return  #剩下的字符太多，剪枝
        if level==5:
            res.append('.'.join(path[:]))  
            return 
        for i in range(1,4):
            ip=s[begin:begin+i]
            if int(ip)>255 or int(ip)<0:  #排除数值不符合的
                continue
            if ip[0]=='0' and len(ip)>1:  #排除'0'打头的
                continue
            path.append(ip)
            self.backTrack(s,path,res,begin+i,level+1,n)
            path.pop()
            
#https://leetcode-cn.com/problems/restore-ip-addresses/solution/hui-su-suan-fa-hua-tu-fen-xi-jian-zhi-tiao-jian-by/
