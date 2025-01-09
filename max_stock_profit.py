def stock_picker(prices):
    if len(prices) < 2:
        return -1  # Cannot make any transactions

    min_price = float('inf')  # Initialize to infinity
    max_profit = -1  # Start with no profit

    for price in prices:
        # Update the minimum price seen so far
        if price < min_price:
            min_price = price
        
        # Calculate potential profit
        profit = price - min_price
        
        # Update the maximum profit
        if profit > max_profit:
            max_profit = profit

    return max_profit if max_profit > 0 else -1

# Examples
print(stock_picker([10, 12, 4, 5, 9]))  # ➞ 5
print(stock_picker([14, 20, 4, 12, 5, 11]))  # ➞ 8
print(stock_picker([80, 60, 10, 8]))  # ➞ -1
