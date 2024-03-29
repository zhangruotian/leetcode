class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        n1,n2=len(num1),len(num2)
        res_arr=[0]*(n1+n2)
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                num1_int,num2_int=int(num1[i]),int(num2[j])
                res_arr[i+j+1]+=(num1_int*num2_int)%10
                res_arr[i+j]+=(num1_int*num2_int)//10
        for i in range(n1+n2-1,-1,-1):
            if res_arr[i]>=10:
                ele=res_arr[i]
                res_arr[i]=ele%10
                res_arr[i-1]+=ele//10
        res=""
        for i in range(n1+n2):
            if i==0 and res_arr[i]==0:
                continue
            res+=str(res_arr[i])
        return res
        #https://www.youtube.com/watch?v=G9OWbq-e9hw

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #.  9.  9. 9
        #.  9.  9. 9
        #8  9   1
        if num1=='0' or num2=='0':
            return '0'
        len1,len2=len(num1),len(num2)
        res=[0]*(len1+len2)
        for i in range(len2-1,-1,-1):
            for j in range(len1-1,-1,-1):
                val=int(num1[j])*int(num2[i])
                res[i+j+1]+=val%10
                res[i+j]+=val//10+res[i+j+1]//10
                res[i+j+1]=res[i+j+1]%10
        ans=''
        for i in range(len1+len2):
            if i==0 and res[i]==0:
                continue
            ans+=str(res[i])
        return ans
