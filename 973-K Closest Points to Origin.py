#leetcode practice question 973
#return the k amount of points closest to the origin given k and a list of points 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [(float('-inf'), []) for _ in range(k)]
        
        heapq.heapify(maxHeap)

        for x, y in points:
            dist = sqrt((x**2) + (y**2)) * -1
            if dist >= maxHeap[0][0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (dist, [x,y]))

        return [point for dist, point in maxHeap]