class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #hold the brackets that we havent yet matched
        pairs = {')' :'(' , '}' : '{', ']' : '['}

        #go through the string one character at a time. if close bracket either nothing is a match or the last open one would be a differnt match. if prev true - invalid string. if matched pop the stack. and save it 
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
