def find_profits(prices:list):
    # TODO retrun list of profits
    profit = []
    
    if prices:
        min_price = prices[0]
    else:
        return profit
    # best practice
    # min_price = float('inf')
    for price in prices:
        if min_price>= price:
            profit.append(0)
            min_price = price
        else:
            best = price - min_price
            profit.append(best)

    return profit
    
""" model solution
def find_profits(prices):
    profits = []
    min_price = prices[0]

    for price in prices:
        min_price = min(min_price, price) # >= tiny faster
        profits.append(price - min_price)

    return profits

"""
if __name__ == "__main__":
    print(find_profits([1, 2, 3, 4])) # [0, 1, 2, 3]
    print(find_profits([4, 3, 2, 1])) # [0, 0, 0, 0]
    print(find_profits([1, 1, 1, 1])) # [0, 0, 0, 0]
    print(find_profits([2, 4, 1, 3])) # [0, 2, 0, 2]
    print(find_profits([1, 1, 5, 1])) # [0, 0, 4, 0]
    print(find_profits([3, 2, 3, 5, 1, 4])) # [0, 0, 1, 3, 0, 3]

    prices = list(range(1, 10**5+1))
    print(find_profits(prices)[:5]) # [0, 1, 2, 3, 4]
    print(find_profits([9, 6, 10, 10, 3, 6, 7, 6, 5, 7])) # [0, 0, 4, 4, 0, 3, 4, 3, 2, 4]