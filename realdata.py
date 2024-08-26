import pandas as pd
import requests
import json
import sys

if not sys.warnoptions:  # не выводит незначимые ошибки
    import warnings
    warnings.simplefilter("ignore")


def get_realdata():
    """
    Загружает данные BTCUSDT и ETHUSDT за последний час
    """
    symbol_eth = 'ETHUSDT'
    symbol_btc = 'BTCUSDT'
    interval = '1m'
    limit = 60

    url = f'https://api.binance.com/api/v3/klines?symbol={symbol_eth}&interval={interval}&limit={limit}'
    response_eth = requests.get(url)
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol_btc}&interval={interval}&limit={limit}'
    response_btc = requests.get(url)
    data_eth = json.loads(response_eth.text)
    data_btc = json.loads(response_btc.text)
    prices_eth = pd.DataFrame(data_eth, dtype=float)
    prices_btc = pd.DataFrame(data_btc, dtype=float)
    prices_eth = prices_eth.iloc[:, :3]
    prices_btc = prices_btc.iloc[:, :3]
    columns = ['time', 'open', 'close']
    prices_eth.columns = columns
    prices_btc.columns = columns
    prices_eth['time'] = pd.to_datetime(prices_eth['time'], unit='ms')
    prices_btc['time'] = pd.to_datetime(prices_btc['time'], unit='ms')
    prices_eth = prices_eth.set_index('time')
    prices_btc = prices_btc.set_index('time')
    prices_eth['Change %'] = 100*(prices_eth['close'] - prices_eth['open'])/prices_eth['open']
    prices_btc['Change %'] = 100*(prices_btc['close'] - prices_btc['open'])/prices_btc['open']
    prices_eth.drop(prices_eth.columns[0:2], axis=1, inplace=True)
    prices_btc.drop(prices_btc.columns[0:2], axis=1, inplace=True)
    return prices_eth, prices_btc


def own_movement(model, prices_eth, prices_btc):
    """
    Вычисляем изменение цены ETH и BTC с учетом предсказания модели
    """
    eth_data = prices_eth.copy()
    btc_data = prices_btc.copy()
    eth_pr = model.predict(btc_data[['Change %']])
    eth_own = eth_data['Change %'].sum() - eth_pr.sum()
    return eth_own


def moving_average(prices_eth, prices_btc):
    """
    Вычисляем скользящее среднее изменения цены ETH и BTC
    """
    eth_data = prices_eth.copy()
    btc_data = prices_btc.copy()
    spread = eth_data['Change %'].sub(btc_data['Change %'], axis=0)
    rolling_mean = spread.rolling('60min').mean()
    spread_adj = spread - rolling_mean
    eth_futures_movements = prices_eth['Change %'] - spread_adj
    eth_movements = eth_futures_movements.sum()
    return eth_movements
