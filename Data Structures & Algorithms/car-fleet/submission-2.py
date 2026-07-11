class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)
        
        stack = []
        
        for p, s in pairs:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack) 