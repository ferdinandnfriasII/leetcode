#leetcode practice question 234
#Given a linked list, determine if it is a palindrome ex. 1 -> 2 -> 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.first = head
        
        def recursiveCheck(curr = head):
            if curr is not None:
                if not recursiveCheck(curr.next):
                    return False
                if self.first.val != curr.val:
                    return False
                self.first = self.first.next
            return True
        
        return recursiveCheck()
        
        
        """
        Solution when converting the linked list into an array of integers
        
        
        nums = []
        
        curr = head
        
        #convert linked list into an array of nums
        while curr is not None:
            nums.append(curr.val)
            curr = curr.next
            
        l, r = 0, len(nums) - 1
        
        while l < r:
            if nums[l] != nums[r]:
                return False
            l, r = l + 1, r - 1
        return True
        
        """