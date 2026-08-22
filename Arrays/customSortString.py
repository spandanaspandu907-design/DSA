class Solution:
    def customSortString(self, order, s):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        result = []

        for ch in order:
            if ch in freq:
                result.append(ch * freq[ch])
                del freq[ch]

        for ch, count in freq.items():
            result.append(ch * count)

        return ''.join(result)