input_string = "NVCA Lions"

# We iterate from the beginning of the string (index 0) through the length of the string
# (len(input_string)) and we increment by 2 every time since we only want the even numbered
# characters.  The input_string[i] is retrieving the character at index i within the string.
for i in range(0, len(input_string), 2):
    print(input_string[i])