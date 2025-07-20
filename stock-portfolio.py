
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

def stock_portfolio_tracker():
    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' when you are finished entering stocks.\n")

    portfolio = {}
    total_investment = 0

    while True:
        stock = input("Enter stock symbol (e.g., AAPL): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❗ Stock not found in the list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
        except ValueError:
            print("❗ Invalid quantity. Please enter a number.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    print("\n📊 Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_investment += value
        print(f"{stock} - Qty: {qty} × ${stock_prices[stock]} = ${value}")

    print(f"\n💰 Total Investment Value: ${total_investment}")

    save = input("\nDo you want to save the result to 'portfolio.csv'? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.csv", "w") as file:
            file.write("Stock,Quantity,Price,Total\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                total = qty * price
                file.write(f"{stock},{qty},{price},{total}\n")
            file.write(f",,,Total Investment: ${total_investment}\n")
        print("✅ Portfolio saved to portfolio.csv")

# Run the tracker
stock_portfolio_tracker()
