class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_N=((len(nums)*(len(nums)+1))//2)
        sum_num=sum(nums)
        return sum_N-sum_num