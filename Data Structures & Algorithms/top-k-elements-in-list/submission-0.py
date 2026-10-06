class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for i in nums:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1

        ordered = sorted(store, key=store.get, reverse=True)
        return ordered[:k]
        