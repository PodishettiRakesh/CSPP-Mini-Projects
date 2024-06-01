import random
def update_stock_prices(stocks):
    for stock in stocks:
        # print(stock)
        stock['previous_price'] = stock['price']
        change_percent = random.uniform(-0.1, 0.1)  # Change in price by +/- 10%
        # print(change_percent)
        stock['price'] = round(stock['price'] * (1 + change_percent), 2)
        print(stock)
    return stocks
# stocks = [{'name': 'AAPL', 'price': 150, 'previous_price': 150},
#         {'name': 'GOOG', 'price': 2800, 'previous_price': 2800},
#         {'name': 'TSLA', 'price': 700, 'previous_price': 700}]
# print(update_stock_prices(stocks))

def get_daily_change(stock):
    return round(((stock['price'] - stock['previous_price']) / stock['previous_price']) * 100, 2)

def buy_stock(portfolio, stocks, stock_name, quantity):
    stock = next(stock for stock in stocks if stock['name'] == stock_name)
    cost = stock['price'] * quantity
    if portfolio['cash'] >= cost:
        portfolio['cash'] -= cost
        if stock_name in portfolio['stocks']:
            portfolio['stocks'][stock_name]['quantity'] += quantity
        else:
            portfolio['stocks'][stock_name] = {'stock': stock, 'quantity': quantity}
        print(f"Bought {quantity} shares of {stock_name} at ${stock['price']} each.")
    else:
        print("Insufficient cash to buy stock.")


def view_portfolio(portfolio):
    print(f"Available cash: ${portfolio['cash']}")
    for stock_name, stock_info in portfolio['stocks'].items():
        stock = stock_info['stock']
        quantity = stock_info['quantity']
        print(f"{stock_name}: {quantity} shares at ${stock['price']} each")

def daily_update(stocks):
    print("\n--- Daily Update ---")
    update_stock_prices(stocks)
    for stock in stocks:
        print(f"{stock['name']}: New price ${stock['price']}, Daily change {get_daily_change(stock)}%")

def main():
    initial_cash = 10000
    days_of_simulation = 5
    stocks = [{'name': 'AAPL', 'price': 150, 'previous_price': 150},
              {'name': 'GOOG', 'price': 2800, 'previous_price': 2800},
              {'name': 'TSLA', 'price': 700, 'previous_price': 700}]
    portfolio = {'cash': initial_cash, 'stocks': {}}

    for day in range(1, days_of_simulation + 1):
        print(f"\n--- Day {day} ---")
        daily_update(stocks)
        view_portfolio(portfolio)
main()