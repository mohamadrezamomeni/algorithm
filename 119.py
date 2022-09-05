class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def recursiveResolveRow(num):
            if num == 0:
                return [1]
            r = recursiveResolveRow(num-1)

            temp = []
            for i in range(num+1):
                val1 = 0
                val2 = 0
                if i == 0:
                    val1 = 0
                    val2 = r[i]
                elif i == num:
                    val2 = 0
                    val1 = r[i-1]
                else:
                    val1 = r[i-1]
                    val2 = r[i]

                temp.append(val1+val2)

            return temp
        return recursiveResolveRow(rowIndex)
