# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums[i+1:]:
                li = [i]
                li.append(nums[i+1:].index(x) + i + 1)
                return li

        
