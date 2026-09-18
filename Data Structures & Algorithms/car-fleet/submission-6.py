class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)

        stack = [
            (target - cars[0][0]) / cars[0][1]
        ]

        for i in range(1, len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if time > stack[-1]:
                stack.append(time)
            else:
                continue
        return len(stack)


        