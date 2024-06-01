import random
def update_stock_prices(stocks):
    for stock in stocks:
        stock['previous_price'] = stock['price']
        change_percent = random.uniform(-0.1, 0.1)  # Change in price by +/- 10%
        stock['price'] = round(stock['price'] * (1 + change_percent), 2)
    return stocks
stocks = [{'name': 'AAPL', 'price': 150, 'previous_price': 150},
        {'name': 'GOOG', 'price': 2800, 'previous_price': 2800},
        {'name': 'TSLA', 'price': 700, 'previous_price': 700}]
print(update_stock_prices(stocks))

def main():
    initial_cash = 10000
    days_of_simulation = 5
    stocks = [{'name': 'AAPL', 'price': 150, 'previous_price': 150},
              {'name': 'GOOG', 'price': 2800, 'previous_price': 2800},
              {'name': 'TSLA', 'price': 700, 'previous_price': 700}]
    portfolio = {'cash': initial_cash, 'stocks': {}}

    # for day in range(1, days_of_simulation + 1):
    #     print(f"\n--- Day {day} ---")
    #     daily_update(stocks)
    #     view_portfolio(portfolio)
main()