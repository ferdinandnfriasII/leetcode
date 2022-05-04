#leetcode practice question 20
#Determine whether a string is a valid parentheses ex. "[()(){}[]]"

class Solution:
    def isValid(self, s:str) -> bool:
        stack = []

        #if starts with right 
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False
        
        else:
            for i in s:
                if i == '(' or i == '[' or i == '{':
                    stack.append(i)
                
                else:
                    if len(stack) == 0:
                        return False

                    if i == ')':
                        if stack[-1] != '(':
                            return False
                    
                    if i == ']':
                        if stack[-1] != '[':
                            return False
                    
                    if i == '}':
                        if stack[-1] != '{':
                            return False
                    
                    stack.pop()

        return len(stack) == 0