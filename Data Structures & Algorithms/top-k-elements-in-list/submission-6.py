class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)] #empty lists

        for n,c in count.items():
            freq[c].append(n) #the index here is now how many times the num occurs
        
        res = []
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]: #couse some list can also have more value in it
                res.append(num)
                if len(res) == k:
                    return res

        

        