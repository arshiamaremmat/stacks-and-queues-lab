# custom_stack.py
from typing import List

def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.

    Approach:
      - Use a stack to track opening brackets.
      - On a closing bracket, the top of the stack must be the matching opener.
      - Valid iff the stack is empty at the end.
    """
    pairs = {')': '(', ']': '[', '}': '{'}
    openers = set(pairs.values())
    stack: List[str] = []

    for ch in s:
        if ch in openers:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            # Ignore any non-bracket characters (not used in provided tests)
            continue

    return len(stack) == 0