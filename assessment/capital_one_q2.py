# ["aaabb", "aaaab", "bbbhaa", "ccncaa"]
# 
# find count of interesting strings in an array
# interesting strings are
    # given N... if a string has consecutive N same characters 
    # if length N of same character is not followed by same character and it is followed by some other character
    # if length N of same character is not preceeded by same character and it is preceeded by some other character
    # example N = 3, we need to find in all string if there is some char which is occuring N time in continuous order and if it does exists then find if the suvstring is followed or preceeded with some other charcter or not
    # if all rules satisfy than only it is interesting string other no



def find_count(array, n):
    """
    Counts and prints substrings within each string in a given array that appear
    exactly `n` times, using a sliding window approach with a dictionary to track
    character frequencies.

    Args:
        array (List[List[str]]): A list of strings where each string represents
            an element in the array to be processed further by the function.
        n (int): Used as the threshold for counting consecutive occurrences of
            characters in each element of the input array.
            
            The number determines how many times the same character must appear
            consecutively within an element to be counted.

    """
    result = 0
    for ele in array:
        dict_w = {}
        past_char = ""
        for e in ele:
            if ((not e == past_char) and dict_w.get(past_char, 0) < n) and not past_char == "":
                dict_w[past_char] = dict_w.get(past_char, -2) + 1
            
            if dict_w.get(e, 0) >= 0:
                dict_w[e] = dict_w.get(e, 0) + 1
            else:
                dict_w[e] = 1
            past_char = e

        for j in dict_w.values():
            if j == n:
                print(ele)
                result += 1
                break

    print(result)


array = ["aaabb", "aaaab", "bbbhaa", "ccncaa"]
n=3
find_count(array, n)