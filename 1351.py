class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for x in range(len(grid)):
            l, r = 0, len(grid[x]) - 1
            while l <= r:
                m = (l + r) // 2
                if grid[x][m] < 0:
                    r = m - 1
                else:
                    l = m + 1
            res += len(grid[x]) - l
        return res
