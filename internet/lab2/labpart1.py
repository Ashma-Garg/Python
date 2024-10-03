import time
from datetime import timedelta, datetime

def resetLabTime():
    time.sleep(10)

def TaskOne():
    isTakeInput = True
    while isTakeInput:
        light = input("Enter the Signal colour: ")
        start = True
        if light.lower() == "red":
            start = False
            print("traffic stopped")
        elif light.lower() == "green":
            start = True
            print("Traffic moves")
            break
        elif light.lower() == "yellow":
            start = False
            print("Waiting for signal to turn green in 10 secs")
            resetLabTime()
            start = True
            print("Traffic moves again")
            break
        else:
            print("Invalid input")


def findDaysForChirs():
    current_time = datetime.now()
    # Define the next Christmas date
    this_year = current_time.year
    next_christmas = datetime(this_year, 12, 25)

    # If Christmas has already passed this year, set it for next year
    if current_time > next_christmas:
        next_christmas = datetime(this_year + 1, 12, 25)

    # Calculate the number of days until the next Christmas
    days_until_christmas = (next_christmas - current_time).days

    # Print the result
    print(f"{days_until_christmas} days left till next Christmas.")


def TaskTwo():
    # task 1
    time_delta = timedelta(days=365, hours=5, minutes=1)
    print(time_delta) 

    #task 2
    current_time = datetime.now()
    print(f"Today is: {current_time}")

    # task 3
    two_years_from_now = current_time + timedelta(days=730)
    print(f"Two years from now it will be: {two_years_from_now}")

    # task 4
    weeks_and_days_delta = timedelta(weeks=2, days=3)
    future_date = current_time + weeks_and_days_delta
    print(f"In 2 weeks and 3 days it will be: {future_date}")

    # task 5
    three_weeks_ago = current_time - timedelta(weeks=3)
    print(f"Three weeks ago it was {three_weeks_ago.strftime('%A %B %d, %Y')}")

    # task 6
    findDaysForChirs()


def TaskThree():
    # task 1
    with open("grocerylist.txt", "r") as file:

        # task 2
        L1 = ['tea', 'bakery', 'soaps', 'rice', 'candies', 'lotions']

        # task 3
        d1 = {}

        # task 4
        while True:
            category = file.readline().strip()  # Read the category
            if not category:
                break  # End of file
        
            if category in L1:
                item = file.readline().strip()  # Read the item
                quantity = int(file.readline().strip())  # Read the quantity
                d1[category] = (item, quantity)  # Add the category, item, and quantity to d1
            else:
                # Skip the item and quantity if category not in L1
                file.readline()  # Skip the item
                file.readline()  # Skip the quantity
                print(f"{category} category not available.")
            file.readline()
            print(d1)

    # task 5
    while True:
        s = input("Enter a category (e.g., 'tea'): ").strip()

        # step 6
        if s in d1:
            item, quantity = d1[s]
            print(f"Category: {s}, Item: {item}, Quantity: {quantity}")

            while True:
                try:
                    n = int(input("Enter how many items you would like to order: "))

                    if n < 0:
                        print("Negative inputs are not accepted. Please enter a valid positive number.")
                        continue
                    else:
                        print("Congratulations – Your order is successfully placed.")
                        break

                # Handle non-integer input errors
                except ValueError:
                    print("Error: Please enter a valid integer number.")
                    break
            break
        else:
            # Handle invalid categories
            print(f"Error: {s} category is not available. Please try another category.")

            
def make_a_file():
    file_name = "my_name.txt"
    with open(file_name, "w") as file:
        file.write("Ashma")
        file.close()



user_input = input("Which part do you want to run: ")

if user_input == "1":
    TaskOne()
elif user_input == "2":
    TaskTwo()
elif user_input == "3":
    TaskThree()
elif user_input == "4":
    make_a_file()
else:
    print("Invalid Command")