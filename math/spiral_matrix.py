class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # the key is to visualize the pattern
        res = []

        while matrix:
            # step 1: add first row
            res+=matrix.pop(0) # expand list to append

            # step 2: append last element of all lists
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())  # pop the last without parameter

            # step 3: add reverse of the last row
            if matrix:
                res+=matrix.pop()[::-1]  # reversed index

            # step 4: append first element of all all rows in reversed order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))

            # step 5: recursively iterate through above 4 steps

        return res