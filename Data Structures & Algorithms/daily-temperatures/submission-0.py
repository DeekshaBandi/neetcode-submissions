class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #num of days
        n = len(temperatures)

        stack = []

        #starts at 0 IF no warmer day occurs
        out = [0] * n  #??

        #go through each day with its index and temp. while current day is warmer than the day on top of the stack take that waiting day off the stack - pop. so current would then wait for its own warmest day. timewaited = current - the top one

        for i, temp in enumerate(temperatures): #daily temp and the ith day
            while stack and temperatures[stack[-1]] < temp:
                before = stack.pop()
                out[before] = i - before #??
            stack.append(i)
        return out
