"""121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


"""


def max_profit(prices):
    lowest_price_so_far = None
    current_max = 0

    for price in prices:
        if lowest_price_so_far == None:
            lowest_price_so_far = price
        elif price > lowest_price_so_far:
            potential_profit = price - lowest_price_so_far
            if potential_profit > current_max:
                current_max = potential_profit
        elif price < lowest_price_so_far:
            lowest_price_so_far = price

    return current_max
