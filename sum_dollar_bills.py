def add_bill(bill_string):
    # Split the input string into individual bill items
    bills = bill_string.split(",")
    
    # Initialize total to 0
    total = 0
    
    # Iterate over each bill
    for bill in bills:
        # Check if the bill starts with 'd'
        if bill.startswith("d"):
            # Extract the numeric value, converting 'k' (for thousands) if present
            if 'k' in bill:
                total += int(bill[1:-1]) * 1000  # Convert 'd2k' to 2000
            else:
                total += int(bill[1:])  # Convert 'd20' to 20
    
    return total

# Test cases
print(add_bill("d20,p40,p60,d50"))          # ➞ 70
print(add_bill("p30,d20,p60,d150,p360"))    # ➞ 170
print(add_bill("p30,d2k,p60,d200,p360"))    # ➞ 2200
