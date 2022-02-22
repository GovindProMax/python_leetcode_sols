class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total=0
        for char in operations:
            
            if char == "--X" or char == "X--":
                total = total - 1
            elif char == "++X" or char == "X++":
                total = total + 1
        return total