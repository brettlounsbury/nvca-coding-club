def list_start_and_end_equal(input_list):
    first_number = input_list[0] # The first element is always at index 0
    # You can retrieve the X-th element from the end of a string by using -X as the index
    # So for the last number, you can reference index -1
    # The code below is functionally equivalent to last_number = input_list[len(input_list)-1]
    last_number = input_list[-1] # input_list[len(input_list)-1]
    return first_number == last_number


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(list_start_and_end_equal(numbers_x))
print(list_start_and_end_equal(numbers_y))