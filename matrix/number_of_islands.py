from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()  # avoid duplicates
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            # Use BFS to find the boundary of an island
            # Prefer using iterative approach than recursive to implement BFS

            # initialize a queue
            search_queue = deque()
            visited.add((row, col))
            search_queue.append((row, col))

            # kickstart BFS
            while search_queue:
                row, col = search_queue.popleft()

                # up, down, right, left as we only check the adjacency horizontally or vertically
                # TODO this could be optimized. Some directions on the boundary don't need to check
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        (r in range(rows) and c in range(cols))  # range check
                        and (grid[r][c] == "1")  # island check
                        and ((r, c) not in visited)  # visitation check
                    ):
                        search_queue.append((r, c))
                        visited.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    # only kickstart a BFS on new found island
                    bfs(row, col)
                    count += 1

        return count
