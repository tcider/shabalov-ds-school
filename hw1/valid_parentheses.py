class Solution:
    def is_valid(self, string: str) -> bool:
        stack = list()
        for char in string:
            if char in {"(", "{", "["}:
                stack.append(char)
            else:
                if len(stack):
                    tmp = stack.pop()
                else:
                    return False
                if (
                    (char == ")" and tmp != "(")
                    or (char == "]" and tmp != "[")
                    or (char == "}" and tmp != "{")
                ):
                    return False
        if len(stack):
            return False
        return True
