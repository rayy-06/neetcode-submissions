class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []
        for i in range(len(temps)):
            if not stack or temps[i] <= temps[stack[-1]]:
                stack.append(i)
            else:   # temps[i] > temps[stack[-1]]
                while stack and temps[i] > temps[stack[-1]]:
                    j = stack.pop()
                    res[j] = i-j
                stack.append(i)
        return res
        