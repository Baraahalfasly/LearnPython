def show_the_love(lst):
    # Find the smallest value in the list
    min_value = min(lst)
    
    # Keep track of the total donations
    total_donation = 0
    
    # Adjust the list to calculate donations
    for i in range(len(lst)):
        if lst[i] != min_value:
            donation = lst[i] * 0.25
            lst[i] -= donation
            total_donation += donation
    
    # Add the donations to the smallest element
    for i in range(len(lst)):
        if lst[i] == min_value:
            lst[i] += total_donation
            break
    
    # Convert all values to integers
    lst = [round(x) for x in lst]
    
    return lst

# Examples
print(show_the_love([4, 1, 4]))      # ➞ [3, 3, 3]
print(show_the_love([16, 10, 8]))    # ➞ [12, 8, 15]
print(show_the_love([2, 100]))       # ➞ [27, 75]
