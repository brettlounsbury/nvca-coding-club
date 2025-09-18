# Here we have 2 nested for loops that iterate over 1-10.
# for every value of i, 10 values of j are multiplied.  This will perform 100 calculations.
for i in range(1, 11):
    products = [] # this is an empty list
    for j in range(1, 11):
        # add the string value of the product to the end of the list.
        products.append(str(i * j))
    # " ".join(products) tells python to take every element in the products list and
    # put them in a string separated by spaces.
    print(" ".join(products))