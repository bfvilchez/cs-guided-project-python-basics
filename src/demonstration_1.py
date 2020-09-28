"""
Define a function that transforms a given string into a new string where the
original string was split into strings of a specified size.

For example:
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"

The assumptions we are making about our input are the following:

- The input string's length is always greater than zero.
- The string has no spaces.
- The specified size is always a positive integer.
"""
def split_in_parts(s, part_length):
    # Your code here
    # split input string into smaller chuncks of the specified size.
    # iterate over characters in the input string. 
    # counter that will count up to part_length characters.
    

    output = []
    counter = 0

    for letter in s:
        if counter == part_length:
            output.append(" ")
            output.append(letter)
            counter = 1
        else:
            output.append(letter)
            counter += 1

    print(output)
    return output
# Your code here


random_word = "randomStringAgain"

split_in_parts(random_word, 4)

