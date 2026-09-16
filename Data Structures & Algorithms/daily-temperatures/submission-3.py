class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack != [] and temperatures[i] > temperatures[stack[-1]]:
                temp_ind = stack.pop()
                diff = i - temp_ind
                result[temp_ind] += diff
            stack.append(i)
        
        return result

        