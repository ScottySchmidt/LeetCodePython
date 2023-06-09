"""
17. Letter Combinations of a Phone Number: Medium Amazon: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

# Final working solution, below average runtime could use improvement in future:
class Solution(object):
    def letterCombinations(self, digits):
        if len(digits)==0:
            return []
        
        phone_digits = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = [""]
        for d in digits:
            newList = []
            letters = phone_digits[d]
            for l in letters:
                for r in res:
                    newList.append(r+l)
            res = newList
        return res



# Initial solution passes almost half the test cases but does not flatten the list depending on number of digits.
# This method I realized does not dynamically account for number of digits (which makes the combos larger).
import itertools
class Solution(object):
    def letterCombinations(self, digits):
        phone_digits = {2: "abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"psrs", 8:"tuv", 9:"wxyz"}
        L = []

        for d in digits:
            for val, key in phone_digits.items():
                if int(d)==val:
                    keyList = list(key.split(" "))
                    L += keyList
        
        l = itertools.product(*L)
        flat_list = [item for sublist in l for item in sublist]
        return flat_list
        
