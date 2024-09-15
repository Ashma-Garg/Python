# find count of integers whose count of 0 is odd

def zero_count(array):
    count = 0
    for a in array:
        a_string = str(a)
        
        if not a_string.count('0') % 2 == 0:
            count += 1
    
    return count

array = [20, 10, 2010, 500010, 20003300006]
print(zero_count(array))
