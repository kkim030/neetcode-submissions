class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #Top down memoization 

        #Time: O(coins * amount)
        #space: O(Amount)

        coins.sort()
        memo = {0:0}

        def min_coins(amt):
            #smallest number of coins to make the some amt
            if amt in memo:
                return memo[amt] #if we know what the return is, don't have to go through recursion
            minn = float('inf')
            for coin in coins:
                diff = amt - coin
                if diff < 0: #we sort bc no reason so that it stops with it starts -
                    break
                minn = min(minn, 1 + min_coins(diff))
            memo[amt] = minn
            return minn
        
        
        result = min_coins(amount)
        if result < float('inf'): #means it's an actual number
            return result
        else:
            return -1

    
        