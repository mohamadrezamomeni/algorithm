class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memory = {}
        for i in s:
            if i in memory:
                memory[i] += 1
            else:
                memory[i] = 1

        for i in t:
            if i in memory:
                memory[i] -= 1
            else:
                return False

        for i, v in memory.items():
            if v != 0:
                return False

        return True
