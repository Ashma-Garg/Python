# find count of integers whose count of 0 is odd

def zero_count(array):
    """
    Iterates through each element of an input array, converting it to a string to
    check for zeros. It then increments a counter whenever the number of zeros in
    a string is odd, returning the total count at the end.

    Args:
        array (Sequence[int | float | str]): Assumed to be a list or other iterable
            sequence containing numeric (int or float) or string values that can
            include zeros.

    Returns:
        int: The number of elements in the input array where the count of zeros
        in their string representation is odd.

    """
    count = 0
    for a in array:
        a_string = str(a)
        
        if not a_string.count('0') % 2 == 0:
            count += 1
    
    return count

array = [20, 10, 2010, 500010, 20003300006]
print(zero_count(array))
