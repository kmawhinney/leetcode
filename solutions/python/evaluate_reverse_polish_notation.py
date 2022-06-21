class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_map = {"+": operator.add,
                        "-": operator.sub,
                        "*": operator.mul,
                        "/": operator.truediv}

        for token in tokens:
            if token in operator_map:
                val1 = stack.pop(-2)
                val2 = stack.pop(-1)
                new_val = operator_map[token](val1, val2)
                stack.append(int(new_val))
            else:
                stack.append(int(token))
        return stack[-1]
