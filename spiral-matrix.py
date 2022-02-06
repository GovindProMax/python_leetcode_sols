class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startR,rows = 0,len(matrix)
        startC,cols = 0,len(matrix[0])
        newMatrix=[]
        while startR<rows and startC < cols:
            
            for i in range(startC,cols):
                newMatrix.append(matrix[startR][i])
            startR+=1
            
            for i in range(startR,rows):
                newMatrix.append(matrix[i][cols - 1])
            cols-=1
            if not(startR<rows and startC < cols):
                break
            for i in range(cols,startC,-1):
                newMatrix.append(matrix[rows - 1][i -1])
            rows-=1
                
            for i in range(rows,startR,-1):
                newMatrix.append(matrix[i-1][startC])
            startC+=1
        return newMatrix
            