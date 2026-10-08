class Solution:

    def encode(self, strs: List[str]) -> str:
        store = []
        for i in strs:
            count = len(i)
            store.append(str(count) + "#" + i) #everything needs t be string

        return "".join(store) #Because the problem asks us to return one string, not a list.

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            i = j + 1 + length

        return res

