class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memory = {}
        result = []

        def recursiveFind(num):
            if num == 1:
                memory[num] = [1]
                result.append(memory[num])
                return memory[num]
            if num not in memory:
                r = recursiveFind(num-1)
            else:
                r = memory[num]

            temp = []
            for i in range(0, num):
                val1 = 0
                val2 = 0

                if i == 0:
                    val1 = 0
                    val2 = r[i]
                elif i == num-1:
                    val1 = r[i-1]
                    val2 = 0
                else:
                    val1 = r[i-1]
                    val2 = r[i]
                temp.append(val2+val1)

            memory[num] = temp
            result.append(temp)
            return temp

        recursiveFind(numRows)
        return result
