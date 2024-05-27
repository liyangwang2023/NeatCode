class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_1 = {}
        for char in s:
            if char in dict_1:
                dict_1[char] += 1
            else:
                dict_1[char] = 1
        
        for char in t:
            if char in dict_1:
                dict_1[char] -= 1
            else:
                return False
        
        for key, item in dict_1.items():
            if item != 0:
                return False

        return True