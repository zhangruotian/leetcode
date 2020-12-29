class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        if len(digits)==1:
            return [phoneMap[digits][x] for x in range(len(phoneMap[digits]))]
        new_list=[]
        original_list=self.letterCombinations(digits[1:])
        for s1 in phoneMap[digits[0]]:
            for s2 in original_list:
                new_list.append(s1+s2)
        return new_list