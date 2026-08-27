class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for i in range(len(target) - 1, -1, -1):
            # Try to keep target[0:i] unchanged
            cnt = count[:]

            possible = True
            for j in range(i):
                x = ord(target[j]) - ord('a')

                if cnt[x] == 0:
                    possible = False
                    break

                cnt[x] -= 1

            if not possible:
                continue

            # Make this position larger than target[i]
            cur = ord(target[i]) - ord('a')

            for c in range(cur + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    result = target[:i] + chr(c + ord('a'))

                    # Put remaining characters in smallest order
                    for x in range(26):
                        result += chr(x + ord('a')) * cnt[x]

                    return result

        return ""