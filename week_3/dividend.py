def find_profits(prices:list):
    # TODO retrun list of profits + dividend(b-a)
    profit = []
    # need to take account of minimum value not min_price
    min_price = float('inf')
    # best = prices[i] - min_price + (date_sell - date_buy)
    # = (prices[i] + date_sell) - (min_price + date_buy)
    # = (prices[i] + {i})- (min_price + date_buy)
    # = cur_val - min_val
    # keep track of prices[i] + i ; 
    min_val = min_price

    # option 1: i in range len ....
    # option 2: enumerate
    for i,price in enumerate(prices):
        cur_val = price + i
        # lowest "price" 
        if cur_val < min_val: # faster than min( cur_val, min_val)
            min_val = cur_val
        # 0 when same prices, but dividend collects
        profit.append(cur_val - min_val)


    return profit

""" model solution 
def find_profits(prices):
    profits = []
    min_price = prices[0]

    for pos, price in enumerate(prices):
        min_price = min(min_price, price + pos) # slower than if a < b : b = a
        profits.append(price + pos - min_price)

    return profits
"""

if __name__ == "__main__":
    print(find_profits([1, 2, 3, 4])) # [0, 2, 4, 6]
    print(find_profits([4, 3, 2, 1])) # [0, 0, 0, 0]
    print(find_profits([1, 1, 1, 1])) # [0, 1, 2, 3]
    print(find_profits([2, 4, 1, 3])) # [0, 3, 1, 4]
    print(find_profits([1, 1, 5, 1])) # [0, 1, 6, 3]
    print(find_profits([3, 2, 3, 5, 1, 4])) # [0, 0, 2, 5, 2, 6]

    prices = list(range(1, 10**5+1))
    print(find_profits(prices)[:5]) # [0, 2, 4, 6, 8]