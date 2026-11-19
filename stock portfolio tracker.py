# Task 2: Stock Portfolio Tracker

# Hardcoded dictionary to define stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 170
}

def stock_portfolio_tracker():
    print("=== Stock Portfolio Tracker ===")
    print("Available Stocks & Prices per share:")
    for stock, price in stock_prices.items():
        print(f"  - {stock}: ${price}")
    
    portfolio = {}
    total_investment = 0.0
    
    print("\nEnter your portfolio details (Type 'done' when you finish):")
    while True:
        stock_name = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print(f"❌ {stock_name} price list madhe nahiye. Krupaya yantla kontari ek niwada: {list(stock_prices.keys())}")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity < 0:
                print("Quantity negative nasu shakat. Punha prayatna kara.")
                continue
        except ValueError:
            print("Krupaya valid number taka.")
            continue
            
        # Add to portfolio dictionary
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    if not portfolio:
        print("\nKontech stocks add kele nahiyet.")
        return

    print("\n--- Portfolio Summary ---")
    summary_data = []
    summary_data.append("=== Stock Portfolio Summary ===\n")
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        investment = price * qty
        total_investment += investment
        
        line = f"Stock: {stock} | Quantity: {qty} | Price: ${price} | Total: ${investment}"
        print(line)
        summary_data.append(line)
        
    grand_total_line = f"\nGrand Total Investment Value: ${total_investment}"
    print(grand_total_line)
    summary_data.append(grand_total_line)
    
    # Optional File Handling: Save result to a text file
    save_option = input("\nDo you want to save this summary to a .txt file? (yes/no): ").strip().lower()
    if save_option == 'yes':
        file_name = "stock_portfolio_report.txt"
        with open(file_name, "w") as file:
            file.write("\n".join(summary_data))
        print(f"✅ Portfolio successfully '{file_name}' madhe save zala ahe!")

if __name__ == "__main__":
    stock_portfolio_tracker()
