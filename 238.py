class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        haveZero = 0
        for num in nums:
            if num == 0:
                haveZero += 1
            else:
                result *= num

        answer = []
        for num in nums:
            if num != 0:
                if haveZero == 0:
                    answer.append(int(result/num))
                else:
                    answer.append(0)
            else:
                if haveZero > 1:
                    answer.append(0)
                else:
                    answer.append(int(result))
        return answer
