class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for n in letters:
            if n > target:
                return n
        return letters[0]