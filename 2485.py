class Solution:
    def pivotInteger(self, n: int) -> int:
        listNums = []
        reversNums = []
        for i in range(1, n+1):
            if len(listNums) == 0:
                listNums.append(i)
                continue
            listNums.append(i+listNums[i-2])

        for i in range(n, 0, -1):
            if len(reversNums) == 0:
                reversNums.append(i)
                continue
            reversNums.append(i + reversNums[n-i-1])
        reversNums = reversNums[::-1]
        for i, v in enumerate(listNums):
            if listNums[i] == reversNums[i]:
                return i+1

        return -1
