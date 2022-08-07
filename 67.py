class Solution:
    def addBinary(self, a: str, b: str) -> str:

        max_binary = list(str(max(int(a), int(b))))
        min_binary = list(str(min(int(a), int(b))))

        result = ['0'] + [" " for i in range(len(max_binary))]

        i = len(max_binary) - 1
        j = len(min_binary) - 1
        carry = 0

        while i >= 0:

            if j >= 0:
                if max_binary[i] == "1" and min_binary[j] == "1" and carry == 1:
                    result[i+1] = "1"
                    carry = 1
                elif max_binary[i] == "1" and min_binary[j] == "1" and carry == 0:
                    result[i+1] = "0"
                    carry = 1
                elif carry == 1 and min_binary[j] == "0" and max_binary[i] == "0":
                    result[i+1] = "1"
                    carry = 0
                elif carry == 0 and min_binary[j] == "0" and max_binary[i] == "0":
                    print(i)
                    print(j)
                    result[i+1] = "0"
                    carry = 0
                elif carry == 1 and ((min_binary[j] == "1" and max_binary[i] == "0") or (max_binary[i] == "1" and min_binary[j] == "0")):
                    carry = 1
                    result[i+1] = "0"
                elif carry == 0 and ((min_binary[j] == "1" and max_binary[i] == "0") or (max_binary[i] == '1' and min_binary[j] == "0")):

                    carry = 0
                    result[i+1] = "1"
            else:
                if max_binary[i] == "1" and carry == 1:
                    carry = 1
                    result[i+1] = "0"
                elif max_binary[i] == "0" and carry == 0:
                    carry = 0
                    result[i+1] = "0"
                else:
                    carry = 0
                    result[i+1] = "1"

            i -= 1
            j -= 1

        if carry == 1:
            result[0] = "1"
        if result[0] == "0":
            del result[0]
        return ''.join(result)
