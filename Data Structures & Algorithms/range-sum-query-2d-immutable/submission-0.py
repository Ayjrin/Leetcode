class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        return None

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summed = 0
        # start loop at region where the rows start through where they end
        for i in range(row1, row2 + 1):
            #start loop where col start through end
            for j in range(col1, col2 + 1):
                summed += self.matrix[i][j]
        return summed


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)