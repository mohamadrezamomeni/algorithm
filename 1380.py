class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = []
        columns = []
        for row in matrix:
            rows.append(min(row))

        for column in zip(*matrix):
            columns.append(max(column))

        ans = []
        for i in rows:
            if i in columns:
                ans.append(i)

        return ans
