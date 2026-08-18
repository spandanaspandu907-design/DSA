class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_char(s, i):
            skip = 0

            while i >= 0:
                if s[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    return s[i], i - 1
                i -= 1

            return '', -1
        i, j = len(s) -1, len(t) -1
        while i >= 0 or j >= 0:
            a, i = next_char(s, i)
            b, j = next_char(t, j)

            if a != b:
                return False

        return True
        