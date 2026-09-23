class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mem = {}
        mem1 = {}

        for char in s:
            if char in mem:
                mem[char] += 1
            else:
                mem[char] = 1
        for char in t:
            if char in mem1:
                mem1[char] += 1
            else:
                mem1[char] = 1
        if mem == mem1:
            return True
        else:
            return False

        

        