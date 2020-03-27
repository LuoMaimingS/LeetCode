class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        comb = 1
        for digit in digits:
            comb = comb * len(num_dic[digit])
        comb_list = [''] * comb
        for digit in digits:
            for char in num_dic[digit]:





