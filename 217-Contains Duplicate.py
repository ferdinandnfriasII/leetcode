#LeetCode practice question 217
#Determine whether or not an array contains duplicate integers
#

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        
        return False