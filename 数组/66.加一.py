class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # [9,9,9]
        last_digit = digits[-1]
        sum_ = last_digit+1
        carry = sum_//10
        digits[-1] = sum_%10
        i = len(digits)-2
        while i>=0 and carry:
            sum_ = digits[i]+carry
            carry = sum_//10
            digits[i] = sum_%10
            i-=1
        if carry:
            return [1]+digits
        return digits
        
# 199-->200 129-->130 都work
# 例外999
