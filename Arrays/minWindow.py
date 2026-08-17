class Solution:
    def minWindow(self, s, t):
        from collections import Counter

        need = Counter(t)
        window = {}
        left = 0
        have = 0
        required = len(need)
        ans = ""

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                if not ans or right - left + 1 < len(ans):
                    ans = s[left:right + 1]

                ch = s[left]
                window[ch] -= 1

                if ch in need and window[ch] < need[ch]:
                    have -= 1

                left += 1

        return ans