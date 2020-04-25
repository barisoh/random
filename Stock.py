print("Enter stock info below")
x = input("What is the stock name: ?")
price = int(input("What is the stock price: ?"))
growth = int(input("What is the stock growth: ?"))

future_price = price * (1+ (growth/100))

if future_price > 100:
    print("High value amount tax")
    tax = future_price * .1
    

future_price = future_price - tax

print("Expected stock price: " + str(future_price))


