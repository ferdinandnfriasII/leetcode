#leetcode practice question 1046
#determine the last possible weight of stone after playing the stone game
#smashing the heaviest stones until there is one stone left or zero.

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #create maxHeap for stones list
        maxHeap = [-x for x in stones]
        
        heapq.heapify(maxHeap)
        
        while len(maxHeap) != 1:
            if len(maxHeap) == 0:
                return 0
            else:
                stone1 = heapq.heappop(maxHeap)
                stone2 = heapq.heappop(maxHeap)

                if stone1 != stone2:
                    heapq.heappush(maxHeap, stone1 - stone2)
        
        return maxHeap[0] * -1