from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)

        first = []
        mid = ""

        for ch in sorted(cnt):
            first.append(ch * (cnt[ch] // 2))
            if cnt[ch] % 2:
                mid = ch

        first = "".join(first)
        return first + mid + first[::-1]