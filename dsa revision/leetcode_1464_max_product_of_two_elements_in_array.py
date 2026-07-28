class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r = nlargest(2,nums)
        return (r[0]-1)*(r[1]-1)
        