#leetcode practice question 424
#determine the longest repeating characters given the chance of replacing the character k amount of times

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        charDict = collections.defaultdict()                     
        l = 0
        
        #set all characters in string equal to 0 in the hashmap
        for r in range(len(s)):
            charDict[s[r]] = 0 
        
        #go through string incrementing character count in hashmap
        for r in range(len(s)):
            charDict[s[r]] += 1
            
            #loop through length of longest window - most frequent number > value of k
            while ((r - l) + 1) - max(charDict.values()) > k:
                charDict[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
    
        return res
        