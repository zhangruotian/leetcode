class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32位掩码，用于模拟一个32位的计算环境
        mask = 0xFFFFFFFF
        
        # 循环直到进位为0
        while b != 0:
            # 1. 计算"无进位的和" (sum)
            # a ^ b 是对每一位进行相加，但不考虑进位
            # & mask 确保结果在32位内
            sum_val = (a ^ b) & mask
            
            # 2. 计算"进位" (carry)
            # a & b 找出所有需要进位的位 (两个都为1的位)
            # << 1 将进位左移一位，移动到正确的位置
            # & mask 确保结果在32位内
            carry = ((a & b) << 1) & mask
            
            # 3. 更新 a 和 b，为下一次迭代做准备
            # a 更新为当前的和，b 更新为当前的进位
            a, b = sum_val, carry

        # 循环结束后，a 中保存着最终结果的32位补码形式
        # 4. 判断结果的正负并返回
        # 如果 a 小于等于32位最大正数，说明结果是正数
        if a <= 0x7FFFFFFF:
            return a
        else:
            # 否则，a 是一个负数的32位补码，需要转回Python负数
            # 5. 将负数补码转回Python负数
            return ((a ^ mask) + 1) * (-1)
