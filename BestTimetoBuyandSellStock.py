class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        buy_num = None
        
        if prices: 
            # do some stuff
            for i in prices:
                if buy_num is None:
                    buy_num = i
                else:
                    if i < buy_num:
                        buy_num = i
                    else:
                        if max_profit < (i - buy_num):
                            max_profit = i - buy_num
                        
                    
            
        return max_profit