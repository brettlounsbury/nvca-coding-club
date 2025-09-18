# Iterate from 1 to 5
for i in range(1, 6):
    i_as_string = str(i) # convert the integer to a string
    # This makes a new string that has the number and a space in it.
    # It then replicates the string i times, so you would have "1 " or "2 2 " or "3 3 3 ", etc
    output_string = f"{i} " * i # This makes a new string that has the number and a space
    # Since we don't want it to end in a space, we rstrip() the string.  This removes all the
    # whitespace (spaces, tabs) from the end (r = right side = end) of the string
    output_string = output_string.rstrip()
    print(output_string)