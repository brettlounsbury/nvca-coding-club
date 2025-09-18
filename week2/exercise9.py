fibonacci_series = [0, 1] # first 2 digits are 0 and 1
# Start at index 2 (which is the third number in the sequence) since we are given the first 2
for i in range(2, 15):
    # the i'th fibonacci value is equal to the i-1'th and i-2'th fibonacci value
    fibonacci_series.append(fibonacci_series[i-2] + fibonacci_series[i-1])

# We can directly print lists, and they are fairly readable.
print(fibonacci_series)