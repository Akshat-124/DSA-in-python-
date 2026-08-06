class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        x = int(total ** 0.5)

        return x if x * x == total else -1