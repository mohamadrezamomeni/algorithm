class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memory = {}

        def canMakeSentence(s):
            if s in memory:
                return memory[s]
            for w in wordDict:
                if w == s:
                    return True
                len_w = len(w)

                if s[0:len_w] == w:
                    valid = canMakeSentence(s[len_w:])
                    if valid == True:
                        memory[s] = True
                        return True
            memory[s] = False
            return False
        return canMakeSentence(s)
