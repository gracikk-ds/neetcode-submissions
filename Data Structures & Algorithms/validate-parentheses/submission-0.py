class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        matching = {key: value for key, value in zip(opening, closing)}

        stack = []
        for el in s:

            # if stack is empty
            if not stack:
                if el in opening:
                    stack.append(el)
                    continue
                else:
                    return False

            # if stack is not empty
            else:
                # if new element is the opening char
                # we add it to stack
                if el in opening:
                   stack.append(el)
                else:
                    # else we pop the last element from stack 
                    if el == matching[stack.pop()]:
                        continue
                    else:
                        return False
        if stack:
            return False
        return True                

