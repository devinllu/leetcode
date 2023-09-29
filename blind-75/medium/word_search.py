'''
description: given 2d array of chars, find pattern horizontally + vertially that matches word

double for loop, iterate through every cell and find first char
then recurse on all 4 sides, until you find a valid pattern
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(board, word, i, j, visited):
            
            if not word:
                return True
            
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    if board[x][y] == word[0] and (x, y) not in visited:
                        visited.add((x, y))
                        if helper(board, word[1:], x, y, visited):
                            return True
                        else:
                            visited.remove((x, y))
                    
            return False
                    
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if board[i][j] == word[0]:
                    res = helper(board, word[1:], i, j, {(i, j)})
                    
                    if res:
                        return True
        
        return False