class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=list()
        if not grid:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    self.dfs(grid, i, j,visited)
                    count += 1
        print(visited)
        return count

    def dfs(self, grid, i, j,visited):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1" or (i,j) in visited:
            return

        visited.append((i,j))

        self.dfs(grid, i + 1, j,visited)
        self.dfs(grid, i - 1, j,visited)
        self.dfs(grid, i, j + 1,visited)
        self.dfs(grid, i, j - 1,visited)