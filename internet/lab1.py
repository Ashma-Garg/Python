L1 = ["university", "blue", 29, (4, 99, 186), [(6,'w'), 19, (5,'z')], "DATA", "N9E", 21, "Delta"]
L2 = ["openai", "law", 98, 8.00, "lion", "extranet"]

def run_commands_l1 ():
    """
    Attempts to execute various list operations on nested lists `L1` and possibly
    another list `L2`. It catches exceptions for each operation, printing the error
    message if an exception occurs.

    """
    print("Results from Part 1 - Task 1")
    try: 
        print(L1[2][1])
    except Exception as e:
        print(e)

    try:
        print(L1[3][0])
    except Exception as e:
        print(e)

    try:
        print(L1[4][2][1])
    except Exception as e:
        print(e)

    try:
        print(len(L1))
    except Exception as e:
        print(e)

    try:
        print(L1[14])
    except Exception as e:
        print(e)

    try:
        print(L1[-4:-1])
    except Exception as e:
        print(e)

    try:
        print(L1[2][14])
    except Exception as e:
        print(e)

    try:
        print(L2+L1)
    except Exception as e:
        print(e)
    
    try:
        print(L2*2)
    except Exception as e:
        print(e)

    try:
        L1[4][1] = 4
        print(L1[4][1])
    except Exception as e:
        print(e)

    try:
        del L2[-3]
        print(L1)
    except Exception as e:
        print(e)
    
    print()

def run_commands_l2():
    """
    Attempts to modify and append elements to two lists, L1 and L2. It performs a
    series of operations including appending an element, popping an element,
    inserting an element at a specific position, and appending multiple elements
    from a list containing integers.

    """
    print("Results from Part 1 - Task 2")
    try:
        L1.append("unlike")
        print(L1)
        L2.pop()
        print(L2)
        L1.insert(3, 4.8)
        print(L1)
        for i in list([44, 50]):
            L2.append(i)
        print(L2)

    except Exception as e:
        print(e)
    
    print()

s1 = "One should note that IEEE Transactions are extremely selected"
s2 = "There are two areas in cloud computing: performance and security"

def run_commands_p2_l1():
    """
    Executes multiple string operations on predefined strings `s1` and `s2`,
    including indexing, slicing, concatenation, and exception handling. It prints
    results of these operations to the console or error messages if exceptions occur.

    """
    print("Results from Part 2 - Task 1")
    try:
        print(s2[-1: -4: -1])
    except Exception as e:
        print(e)

    try:
        print(s1[1])
    except Exception as e:
        print(e)

    try:
        print(s2[-2:])
    except Exception as e:
        print(e)

    try:
        print(s2[0:20:2])
    except Exception as e:
        print(e)

    try:
        print(s1+" "+s2)
    except Exception as e:
        print(e)

    print()


def run_commands_p2_l2():
    """
    Executes a series of string manipulation and counting operations on variables
    s1 and s2, including checking for a suffix, splitting into individual words,
    converting to uppercase, replacing substrings, and counting character occurrences,
    with error handling in place.

    """
    print("Results from Part 2 - Task 2")
    try:
        if(s2.endswith("security")):
            print("S2 ends with 'security'")
        else:
            print("S2 doesn't end with 'security'")
    except Exception as e:
        print(e)

    try:
        print("List of words in S2:")
        for i in s2.split(" "):
            print(i)
    except Exception as e:
        print(e)

    try:
        print("Convert s1 and s2 to all uppercase letters:")
        print(s1.upper())
        print(s2.upper())
    except Exception as e:
        print(e)

    try:
        print("Replace the string 'data' of s2 with an empty string:")
        print("S2 Before change: ", s2)
        print("S2 after change: ", s2.replace("data", ""))
    except Exception as e:
        print(e)

    try:
        print("Count the number of times ‘E’ occurs in s1:")
        print(s1.count('E'))
    except Exception as e:
        print(e)
    
    print()


d1={"name": "Alex", "age": 35, (4, 'f'):['x', 'y', 'z'], 6: "Canada", 44: 99, 19:555} 
d2 = dict([("name","Nancy"), ("age", 44), ((3,4), ['a', 'b', 'c']), (0, "black"), (33, 67)])
d3 = dict(id=777, name="Michel", siblings=["Fung", "Martin", "Richard"]) 

def run_commands_p3_l1():
    """
    Iterates over various operations on three dictionaries (`d1`, `d2`, and `d3`)
    to demonstrate their behavior, including data retrieval, error handling,
    updates, and comparison of keys, values, and length.

    """
    print("Results from Part 3 - Task 1")
    try:
        print("D1 keys: ")
        print(d1.keys())
    except Exception as e:
        print(e)
    
    try:
        print("D2 values: ")
        print(d2.values())
    except Exception as e:
        print(e)
    
    try:
        print("D3 get id: ")
        print(d3.get("id"))
    except Exception as e:
        print(e)

    try:
        print("Get age from d2: ")
        print(d2.get("age"))
    except Exception as e:
        print(e)

    try:
        print("Get age from d3: ")
        print(d3.get("age"))
    except Exception as e:
        print(e)

    try:
        print("Get name from d3: ")
        print(d3.get("name", "Tim"))
    except Exception as e:
        print(e)

    try:
        print("Get items from d2: ")
        print(d2.items())
    except Exception as e:
        print(e)

    try:
        print("Get sinblings from d3: ")
        print(d3["siblings"])
    except Exception as e:
        print(e)

    try:
        print("Get sinblings from d2: ")
        print(d2)
        print(d2["siblings"])
    except Exception as e:
        print("Error in: ", e)

    try:
        print("D2 update d3: ")
        print(d2.update(d3))
    except Exception as e:
        print(e)

    try:
        print("D2[0]")
        print(d2[0])
    except Exception as e:
        print(e)

    try:
        print("D1 get (1,2)")
        print(d1.get((1, 2)))
    except Exception as e:
        print(e)

    try:
        print("d2['siblings']*: ")
        print(d2["siblings"])
    except Exception as e:
        print(e)

    try:
        print("D2 ['name]: ")
        print(d2["name"])
    except Exception as e:
        print(e)

    try:
        print("is d1 equals d2")
        print(d1 == d2)
    except Exception as e:
        print(e)

    try:
        print("Length of D2")
        print(len(d2))
    except Exception as e:
        print(e)

    try:
        print("print keys of d1")
        for key in d1.keys():
            print(key)
    except Exception as e:
        print(e)

    try:
        print("print keys of d2")
        for key in d2.keys():
            print(key)
    except Exception as e:
        print(e)

    print()


def rainfall():
    """
    Calculates and displays total, average monthly, maximum, and minimum rainfall
    for a year based on user input for each month's rainfall, then prints out these
    statistics along with the respective months for max and min rainfall values.

    """
    total_rainfall = 0.0
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    rainfall = [0.0] * 12  

    
    for i in range(12):
        rainfall[i] = float(input(f'Enter the rainfall for {months[i]}: '))
    
    
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12

    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]

    print()
    print(f'Total rainfall for the year: {total_rainfall}')
    print(f'Average monthly rainfall: {average_rainfall}')
    print(f'Highest rainfall was in {max_month}: {max_rainfall}')
    print(f'Lowest rainfall was in {min_month}: {min_rainfall}')



run_commands_l1()
run_commands_l2()
run_commands_p2_l1()
run_commands_p2_l2()
run_commands_p3_l1()
rainfall()
