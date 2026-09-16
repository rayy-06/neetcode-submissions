
import operator
class Solution:
    def evaluate(self, v1, v2, o):
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        result = ops[o](v1, v2)
        return int(result)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "/", "*"]
        for val in tokens:
            if val not in operators:
                stack.append(val)
            else:
                val1 = int(stack.pop())
                val2 = int(stack.pop())

                result = self.evaluate(val2, val1, val)

                stack.append(str(result))
        return int(stack.pop())


        