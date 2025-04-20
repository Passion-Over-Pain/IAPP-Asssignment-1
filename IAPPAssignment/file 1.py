stock_code = []
stock_price = []
stock_count = []

def AddStockCode():
    if len(stock_code) >= 50: #has to be less than 50
        print("Limit of stock is 50.")
        return

    new_code = input("Enter stock code: ")
    new_price = float(input("Enter stock price: "))

    # btw must we add exception handling with regards to the variable type? One is string, then floating-point, then int.

    #price must be less than 1000
    if new_price > 1000.00:
        print("Stock price cannot be greater than R1000.00.")
        return

    #adding the new items to their respective lists
    stock_code.append(new_code)
    stock_price.append(new_price)
    stock_count.append(0) #stock count set to 0

    print("Code and price successfully added.") #aye improve these messages if you'd like :]

def SearchCode(code):
    for x in range(len(stock_code)): #iterating through stock_code list
        if stock_code == code: #if the entered code matches an existing one in the list
            print(f"Code '{code}' was found at index: {x}")
        else:
            print(f"Code {code} was not found.")
            return -1 #it said to return a 'suitable' value if not found
