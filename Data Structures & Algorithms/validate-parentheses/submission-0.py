class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        match = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in match.values():
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] == match[ch]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0