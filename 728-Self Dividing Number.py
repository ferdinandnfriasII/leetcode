#leetcode practice question 728
#determine if numbers in a range are self dividing (each digit can divide number without a remainder)

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        left = 1, right = 22
        
        input : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        
        self dividing number CANT have ZEROs and has to be divisible by each digit in number
        
        
        step 1. if range is from left to right starts anywhere from 1 - 9, immediately add to output because all numbers
                between 1 - 9 are divisible to themselves
                ex. if range is 4 - 10
                    output = [4, 5, 6, 7 ,8 , 9, ...] 
        step 2. 
        
        
        or 
        
        step 1. for loop through range left to right
        step 2. nested for loop dividing each number by numbers they contain
        step 3. if any result contains a remainder then do not add
        step 4. add number to output 
        
        """
        
        res = []
        
        for num in range(left, right + 1):
            count = 0
            for digit in str(num):
                if digit == '0' or num % int(digit) != 0:
                    break
                    
                count += 1
                if count == len(str(num)):
                    res.append(num)
                    
        return res