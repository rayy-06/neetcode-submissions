class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(heights[0], 0)]
        result = 0

        for i in range(1, len(heights)):
            if heights[i] > stack[-1][0]:
                stack.append((heights[i], i))
            
            else:
                start = i
                while stack != [] and heights[i] <= stack[-1][0]:
                    new = stack.pop()
                    result = max(
                        result, 
                        new[0] * (i - new[1])
                    )
                    start = new[1]
                
                stack.append((heights[i], start))
        
        while stack != []:
            new = stack.pop()
            result = max(
                result,
                new[0] * (len(heights) - new[1])
            )
        
        return result

                

        