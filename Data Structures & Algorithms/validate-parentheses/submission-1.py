class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            # opening brackets → push
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)

            else:
                # must have something to match
                if not stack:
                    return False

                top = stack[-1]

                # manual matching
                if ch == ")" and top == "(":
                    stack.pop()
                elif ch == "]" and top == "[":
                    stack.pop()
                elif ch == "}" and top == "{":
                    stack.pop()
                else:
                    return False

        return len(stack) == 0