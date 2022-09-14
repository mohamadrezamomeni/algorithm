class Solution:
    def wordBreak(self, s: str, wordDict):
        memory = {}

        def allContain(s):
            if s in memory:
                return memory[s]

            result = []
            for w in wordDict:
                if s == w:
                    result.append([w])
                w_len = len(w)
                if s[0:w_len] == w:
                    remained = allContain(s[w_len:])
                    for i in remained:
                        result = result + [[w] + i]

            memory[s] = result
            return result

        r = allContain(s)

        return [' '.join(i) for i in r]
