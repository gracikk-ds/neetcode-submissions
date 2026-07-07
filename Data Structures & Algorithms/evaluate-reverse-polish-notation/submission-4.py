class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        digit_stack = []
        digit_stack_counter = 0
        operations = {"+", "-", "*", "/"}

        for token in tokens:
            # if token is digit -> we add it to digit stack             
            if token not in operations:
                digit_stack.append(token)
                digit_stack_counter += 1

            # if token is operator -> we check digit stack
            # pop 2 last elements
            # made the opeartions
            # update stask with the result.
            else:
                if digit_stack_counter < 2:
                    raise Exception("Digit stask has not enough values to perform the operation.")
                val1 = digit_stack.pop()
                digit_stack_counter -= 1
                val2 = digit_stack.pop()
                digit_stack_counter -= 1
                result = eval(f"{val2}{token}{val1}")
                digit_stack.append(int(result))
                digit_stack_counter += 1

        if digit_stack_counter != 1:
            return Exception("something is broken")
        return int(digit_stack.pop())
