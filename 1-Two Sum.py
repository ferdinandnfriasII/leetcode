#leetcode practice question 1
#Find exactly one solution, can't use the same element twice

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return[i, hashmap[complement]]
            hashmap[nums[i]] = i