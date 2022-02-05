class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        column0 =[]
        row0=[]
        rows = len(matrix)
        cols = len(matrix[0])
        for i,mylist in enumerate(matrix):
            for j,elem in enumerate(mylist):
                if elem == 0:
                    column0.append(j)
                    row0.append(i)
        for r in row0:
            for c in range(0, cols):
                matrix[r][c] = 0

        for c in column0:
            for r in range(0, rows):
                matrix[r][c] = 0
            