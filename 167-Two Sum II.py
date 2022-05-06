#leetcode practice question 167
#Two sum part two, however returns index of both numbers

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        output = []

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1 

            elif numbers[l] + numbers[r] < target:
                l += 1

        output.append(l + 1)
        output.append(r + 1)

        return output
