class Solution:
    def isValid(self, s: str) -> bool:
        symbol_info = []
        try:
            for i in s:
                if "(" is i:
                    symbol_info.append("(")
                if ")" is i:
                    latest_symbol = symbol_info.pop()
                    if latest_symbol != "(":
                        return False
                if "{" is i:
                    symbol_info.append(i)
                if "}" is i:
                    latest_symbol = symbol_info.pop()
                    if latest_symbol != "{":
                        return False
                if "[" is i:
                    symbol_info.append(i)
                if "]" is i:
                    latest_symbol = symbol_info.pop()
                    if latest_symbol != "[":
                        return False
            print(symbol_info)
            if len(symbol_info) != 0:
                return False
            return True
        except:
            print(symbol_info)
            return False
