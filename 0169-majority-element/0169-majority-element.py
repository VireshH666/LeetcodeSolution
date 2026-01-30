class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        big=nums[0]
        ct=1
        for i in range(1,len(nums)):
            if big==nums[i]:
                ct+=1
            else:
                ct-=1   
                if ct==0:
                    big=nums[i]
                    ct=1 
                    
        return big                
        