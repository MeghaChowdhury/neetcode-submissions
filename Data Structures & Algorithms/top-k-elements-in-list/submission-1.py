class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for i in nums:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1

        freq = [[] for i in range(len(nums) + 1)]
        for num in store:
            freq[store[num]].append(num)
        result = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
             
        