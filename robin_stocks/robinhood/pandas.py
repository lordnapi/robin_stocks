import pandas as pd
from robin_stocks.robinhood.helper import *
from robin_stocks.robinhood.orders import *

@login_required
def get_all_stock_orders_data_frame(info=None, convert_to_float=True,
convert_to_datetime=True, include_symbols=True):
    orders = get_all_stock_orders(info)
    df = pd.DataFrame(orders)
    if include_symbols:
        symbols = []
        for url in df.instrument:
            symbols.append(get_symbol_by_url(url))
        df['symbol'] = symbols
    if convert_to_float:
        for column in ['price', 'fees', 'average_price', 'quantity',
                       'cumulative_quantity', 'last_trail_price']:
            df[column] = df[column].astype(float)
    if convert_to_datetime:
        for column in ['created_at', 'updated_at', 'last_transaction_at',
                       'stop_triggered_at', 'last_trail_price_updated_at']:
            df[column] = pd.to_datetime(df[column])
    return(df)
