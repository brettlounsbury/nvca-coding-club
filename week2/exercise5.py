input_list = [10, 20, 33, 46, 55]

# Note: % is the modulo operator.  The modulo operator is how you get the remainder of a division
# operation.  In the case below, it would be the remainder of dividing the item by 5.
# If the value is 0, then there is no remainder and the item is evenly disible by 5.
for item in input_list:
    if item % 5 == 0:
        print(item)