def custom_sort(order, string):
    order_map = {char: index for index, char in enumerate(order)}
    return ''.join(sorted(string, key=lambda c: (order_map.get(c, float('inf')), string.index(c))))

# **Test cases**
print(custom_sort("edc", "abcdefzyx"))  # ➞ "edcabfxyz"
print(custom_sort("fby", "abcdefzyx"))  # ➞ "fbyacdexz"
print(custom_sort("", "abcdefzyx"))     # ➞ "abcdefzyx"
print(custom_sort("", ""))              # ➞ ""
