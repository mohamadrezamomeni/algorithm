import string


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        memory = {}

        for i, v in enumerate(string.ascii_uppercase):
            memory[v] = i+1

        sum_all = 0
        for i, v in enumerate(columnTitle[::-1]):
            sum_all += 26**i * memory[v]
        return sum_all
