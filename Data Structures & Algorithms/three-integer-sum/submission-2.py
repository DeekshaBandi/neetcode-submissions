class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        track = defaultdict(int)

        for num in nums:
            track[num] += 1
        
        out = []
        for i in range(len(nums)):
            track[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums)):
                track[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if track[target] > 0:
                    out.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                track[nums[j]] += 1
        return out