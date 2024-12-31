def stock_picker(prices):
    # If there are fewer than 2 prices, no profit can be calculated
    if not prices or len(prices) < 2:
        return -1

    # Initialize the minimum price and maximum profit
    min_price = prices[0]
    max_profit = -1  # Start with no profit

    # Loop through the prices starting from the second price
    for price in prices[1:]:
        # Calculate the potential profit
        profit = price - min_price
        # Update the maximum profit if the current profit is greater
        if profit > max_profit:
            max_profit = profit
        # Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price

    return max_profit

# Examples:
print(stock_picker([10, 12, 4, 5, 9]))  # ➞ 5
print(stock_picker([14, 20, 4, 12, 5, 11]))  # ➞ 8
print(stock_picker([80, 60, 10, 8]))  # ➞ -1
