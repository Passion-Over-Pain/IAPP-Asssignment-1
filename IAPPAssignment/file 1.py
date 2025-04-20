
stock_codes = []
stock_prices = []
stock_items = []


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def AddStockCode():
    if len(stock_codes) >= 50: #has to be less than 50
        print("\033[91mError: Cannot exceed 50 stock codes in inventory.\033[0m")
        return

    new_code = input("Enter stock code: ") #string based AAA and A12 are both strings
    new_price = input("Enter stock price: ")
    if is_number(new_price):
        new_price = float(new_price)
    else:
        print("\033[91mError: The entered stock price is not a number.\033[0m")
        return

    #price must be less than 1000
    if new_price > 1000.00:
        print("\033[91mError: Stock price cannot be greater than R1000.00.\033[0m")
        return

    #adding the new items to their respective lists
    stock_codes.append(new_code)
    stock_prices.append(new_price)
    stock_items.append(0) #stock count set to 0

    print(f"\033[92mStock Code: {new_code} with price of {new_price} successfully added.\033[0m")

def SearchCode(code):
    for x in range(len(stock_codes)): #iterating through stock_code list
        if stock_codes[x] == code: #if the entered code matches an existing one in the list
            return x
    else:
        print(f"Stock Code: {code} was not found.")
        return -1 #Stock code does not exist in stock_codes

def AddStockItem():
    stock_code = input("Enter a stock code: ")
    stock_pos = SearchCode(stock_code)  #search stock_codes for stock_code
    if not stock_pos == -1:
        stock_item = input("Enter the number of stock items: ")
        if is_number(stock_item): #validate stock items is a number
            stock_item = int(stock_item)
        else:
            print("\033[91mError: The entered stock items is not a number.\033[0m")
            return
        while stock_item > 100 or stock_item < 0: #validating stock_items value
            print("\033[91mError: Stock count should be between 0 and 100.\033[0m")
            stock_item = input("Enter the number of stock items: ")
        stock_items[stock_pos] = stock_item
        print(f"\033[92mStock Code: {stock_codes[stock_pos]} successfully update with {stock_item} items\033[0m")
            
            
def DisplayStockList():
    if len(stock_codes) == 0:
        print("\033[91mError: There are no Stocks in the inventory.\033[0m")
        return
    stock_total = 0
    print(f"Stock Code:\tStock Item:\tStock Price:\tStock Total Value:") #\t character sequence if for tabs, formatting
    for x in range(len(stock_codes)):
        stock_value = stock_prices[x] * stock_items[x] #calculate stock value based on items x price
        stock_total += stock_value
        print(f"{stock_codes[x]}\t{stock_items[x]}\t{stock_prices[x]}\t{stock_value}")
    print(f"Total : {stock_total}")
def DisplaySystemOptions():
    print("1. Add Stock Code.")
    print("2. Add Stock Item.")
    print("3. Display Stock List.")
    print("4. Exit")


print("\033[94mWelcome to Micro Circuits.\033[0m")
DisplaySystemOptions()
option = input("Select an option to continue:")
if is_number(option):
    option = float(option)
while True:
    if option == 4: #to show the exit message on first check as well
        print("\033[93mThank you for visiting Micro Circuits...Exiting.\033[0m")
        break

    if option == 1:
        AddStockCode()
    elif option == 2:
       AddStockItem()
    elif option == 3:
        DisplayStockList()
    else:
        print(f"\033[91mError: {option} is not a valid option number.\033[0m")

    print("") #Blank line for formatting
    DisplaySystemOptions()
    option = input("Select an option to continue:")
    if is_number(option):
        option = float(option)


