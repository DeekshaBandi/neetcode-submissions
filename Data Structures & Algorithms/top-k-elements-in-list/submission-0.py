class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        arr = []
        for i, j in count.items():
            arr.append([j, i])
        arr.sort()

        out = []
        while len(out) < k:
            out.append(arr.pop()[1])
        return out
