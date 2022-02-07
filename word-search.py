class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Store rows and cols
        rows=len(board)
        cols=len(board[0])
        # path storing the visited celss. Prevents visiting visited cell
        found = False
        pathway=set()
        def dfs(r,c,i):
            # if word found
            if i == len(word):
                found = True
                return True
            # if the conditions fall apart
            if (r<0 or
               c<0 or
               r>=rows or
               c>=cols or
               word[i] != board[r][c] or
               (r,c) in pathway): return False
            
            pathway.add((r,c))
            
            # check top right bottom left
            result = (dfs(r+1, c, i+1 ) or 
                     dfs(r-1, c, i+1 ) or
                     dfs(r, c+1, i+1 ) or
                     dfs(r, c-1, i+1 ) )
            # reste path
            pathway.remove((r,c))
            #return result
            return result
        for elemR in range(0,rows):
            for elemC in range(0,cols):
                if dfs(elemR, elemC, 0): return True
        return False
                    
        