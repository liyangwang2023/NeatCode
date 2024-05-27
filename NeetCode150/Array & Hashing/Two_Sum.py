class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for i, num in enumerate(nums):
            if num in dict_:
                return [dict_[num], i]
            else:
                dict_[target - num] = i