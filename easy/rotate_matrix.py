class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            new_matrix = []
            for i in range(len(matrix)):
                reversed_row = [r[i] for r in matrix[::-1]]
                new_matrix.append(reversed_row)
            return new_matrix
        
        for rotates in (mat, rotate(mat), rotate(rotate(mat)), rotate(rotate(rotate(mat)))):
            if rotates == target:
                return True
        
        return False