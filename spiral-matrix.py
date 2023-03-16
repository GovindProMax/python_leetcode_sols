class Solution:
    def spiralOrder(self, array: List[List[int]]) -> List[int]:
        startR,rows = 0,len(array)-1
        startC,cols = 0,len(array[0])-1
        newMatrix=[]
        while startR<=rows and startC <=cols:
            for c in range(startC,cols+1):
                newMatrix.append(array[startR][c])
            for r in range(startR+1,rows+1):
                newMatrix.append(array[r][cols])
            for c in range(cols-1,startC-1,-1):
                if startR==rows:
                    break
                newMatrix.append(array[rows][c])
            for r in range(rows-1,startR,-1):
                if startC==cols:
                    break
                newMatrix.append(array[r][startC])
            startR+=1
            startC+=1
            rows-=1
            cols-=1
        return newMatrix