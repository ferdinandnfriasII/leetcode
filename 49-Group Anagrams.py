#leetcode practice question 49
#given an array of strings, group the anagrams together.

import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        strs = ["eat","tea","tan","ate","nat","bat"]
    
        eat -> aet
        tea -> aet 
        
        Note: when sorted, therefore if sorted str are equal they belong in the same list
        
        so create list dictionary for each possible sorted string, if the sorted string exists
        in the dictionary then append that string to the list. 
        

        ex. 
                       0               1                  2
        charDict = { "aet" : ["eat", "tea", ], "ant" : ["tan", ] }

        strs = ["eat","tea","tan","ate","nat","bat"]
                  0
                        1
                            2....

        How code runs: 
        defaultdict(<class 'list'>, {})
        defaultdict(<class 'list'>, {'aet': ['eat']})
        defaultdict(<class 'list'>, {'aet': ['eat', 'tea']})
        defaultdict(<class 'list'>, {'aet': ['eat', 'tea'], 'ant': ['tan']})
        defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan']})
        defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat']})
        defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})
        """
        
        charDict = collections.defaultdict(list)
        
        print(charDict)
        
        for s in strs:
            charDict["".join(sorted(s))].append(s)
        
            
        return charDict.values()
            