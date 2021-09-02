class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        old_r, old_c = len(mat), len(mat[0])
        if old_r * old_c != r * c:
            return mat
        new_mat = [[None for i in range(c)] for j in range(r)]
        i = 0
        old_i = 0
        old_j = 0
        while i < r:
            j =  0
            while j < c:
                new_mat[i][j] = mat[old_i][old_j]
                old_j += 1
                if old_j % old_c == 0:
                    old_i += 1
                    old_j = 0
                j += 1
            i += 1
        return new_mat
