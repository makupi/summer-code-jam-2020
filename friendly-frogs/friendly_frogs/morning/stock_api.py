from yahoo_fin import stock_info as si

class Stock:

    def __getattr__(self, item):
        try:
            return si.get_live_price(item)
        except Exception:
            return 'No data'


def get_stocks_price(you_stocks):
    for stock in you_stocks:
        class_object = globals()['Stock']
        yield stock,class_object().__getattr__(stock)

if __name__ == "__main__":
    stocks = ['apple', 'microsoft', 'FELE']
    for name,price in get_stocks_price(stocks):
        print(name,price)
