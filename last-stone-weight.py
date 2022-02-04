class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        stones = [-strs for strs in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            firstelement = heapq.heappop(stones)
            secondelement = heapq.heappop(stones)
            
            if secondelement > firstelement:
                heapq.heappush(stones, firstelement - secondelement)
        if len(stones) == 0:
            return 0
        return -stones[0]