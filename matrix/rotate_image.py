from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])

        for i in range(n // 2):
            for j in range(i, (n - i - 1)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp
