class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        res = []
        i = 0
        for num in freq:
            if i == k:
                break
            res.append(num)
            i += 1

        return res

