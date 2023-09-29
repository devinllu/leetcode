'''
description: find all groups of islands (1's) surrounded by water (0s) on all 4 sides

for each node, dfs and set all horizontal + vertical 1s into 0s, recurse
guarantees that each iteration will count as 1 island (marking all islands as visited)
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        counter = 0
        
        def dfs(r, c):
            
            if grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            
            if (r - 1) >= 0:
                dfs(r - 1, c)
                    
            if (r + 1) < len(grid):
                dfs(r + 1, c)
                    
            if (c - 1) >= 0:
                dfs(r, c - 1)
                    
            if (c + 1) < len(grid[0]):
                dfs(r, c + 1)
            

                
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    counter += 1
        return counter