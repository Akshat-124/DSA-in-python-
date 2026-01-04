# def stocks(prices):       #leetcode-121                            #bruteforce (TC=o(n^2))
#     n=len(prices)
#     max_profit=0
#     for i in range (0,n):
#         for j in range (i+1,n):
#             if prices[j]>prices[i]:
#                 profit=prices[j]-prices[i]
#                 max_profit=max(max_profit,profit)
#                 i+=1
#     return max_profit
# prices=[7,2,1,5,6,4,8]
# print(stocks(prices))

def stocks(prices):                                 #optimal (TC=o(n))
    n=len(prices)
    max_profit=0
    min_price=float("inf")
    for i in range(0,n):
        min_price=min(min_price,prices[i]) 
        max_profit=max(max_profit,prices[i]-min_price)
        i+=1
    return max_profit
prices=[7,2,1,5,6,4,8]
print(stocks(prices))