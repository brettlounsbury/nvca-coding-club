running_sum = 0
for i in range(10):
    # += means "increment and assign".
    # running_sum += i is a short form of running_sum = running_sum + i
    running_sum += i
    print(f"for iteration {i} sum is {running_sum}")