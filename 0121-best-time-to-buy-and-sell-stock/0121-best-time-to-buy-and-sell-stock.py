class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        pf=0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]   
            elif prices[i]-buy>pf:
                pf=prices[i]-buy
        return pf

