class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        right = len(matrix) -1
        b = 0
        
        # run until leftcolumn is less that right column
        while b < right:
            # iterate from left to right, x will take care of element in each row
            for x in range(right-b):
                #store top left elelemt in a temp variable
                tmp = matrix[b][b+x]
                
                # move bottom left to top right's location
                matrix[b][b+x] = matrix[right-x][b]
                
                # move bottom right to bottom left
                matrix[right-x][b] = matrix[right][right-x]
                
                # move top right to bottom right
                matrix[right][right-x] = matrix[b+x][right]
                
                #top right becomes the temo which was top left
                matrix[b+x][right] = tmp
            ## update boundaries
            b+=1
            right-=1