class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)        # number of rows
        n = len(mat[0])     # number of columns
    
        k = k % n           # reduce unnecessary shifts
    
        for i in range(m):
            if i % 2 == 0:
                # even row → left shift
                shifted = mat[i][k:] + mat[i][:k]
            else:
                # odd row → right shift
                shifted = mat[i][-k:] + mat[i][:-k]
        
            # check if same as original row
            if shifted != mat[i]:
                return False
    
        return True
        