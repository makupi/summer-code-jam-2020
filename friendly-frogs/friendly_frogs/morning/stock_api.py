from yahoo_fin import stock_info as si

def get_stocks_price(you_stocks):
    for stock in you_stocks:
        try:
            yield stock,si.get_live_price(stock)
        except Exception:
            yield stock,'No data'

