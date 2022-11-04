class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        memory = {}

        for i in ransomNote:
            if i in memory:
                memory[i] += 1
            else:
                memory[i] = 1
        for i in magazine:
            if i in memory and memory[i] > 0:
                memory[i] -= 1

        for i, v in memory.items():
            if v != 0:
                return False
        return True
