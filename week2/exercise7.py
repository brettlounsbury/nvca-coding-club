# While it is not the most efficient code, the simplest way to check if a number is a palindrome
# is to convert it to a string and then compare it to the reverse of the string.
# 123 would convert to "123" and the reverse would be "321" so it would not be a palindrome
# 121 would convert to "121" and the reverse would be "121" so it would be a palindrome
# The reason for converting to a string is that strings make it very easy to grab a digit by its
# index whereas this is more complicated to do with an integer
def is_palindrome(num):
    num_as_string = str(num)
    reversed_num = ""
    for i in range(len(num_as_string)):
        digit = num_as_string[i]
        # The key here that we are prepending the digit (adding to the front) instead of appending
        # (adding to the back).  With every new digit we are putting it at the front as we read
        # the original string from front to back, meaning we are reversing it
        reversed_num = digit + reversed_num
    return num_as_string == reversed_num


print(is_palindrome(123))
print(is_palindrome(121))