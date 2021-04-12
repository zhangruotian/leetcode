class Solution {
    public int add(int a, int b) {
        a=a^b;
        b=a&b<<1;
        while(b!=0){
            a=a^b;
            b=a&b<<1;
        }
        return a;
        
    }
}

//python无int long之分，位运算容易出问题。本题直接用java比较简单。
//https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/