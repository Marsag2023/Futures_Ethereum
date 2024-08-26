import pandas as pd
import matplotlib.pyplot as plt


def clean(data):
    """
    Очищает данные от лишних знаков и преобразует в числа

    :param data: исходные данные
    :return: очищенные данные
    """
    for i in range(len(data)):
        if '%' in data[i]:
            data[i] = data[i][0:data[i].index('%')]
    return data.astype(float)


def output_graphs() -> object:
    """
    Загружаем исходные исторические данные и выводим графики изменения цены биткоина и эфириума
    для изкчения
    :return: графики изменения цены
    """
    cols = ['Date', 'Change %']
    btc_data = pd.read_csv('Bitcoin Historical Data.csv', usecols=cols)  # загружаем данные и сортируем по дате
    eth_data = pd.read_csv('Ethereum Historical Data.csv', usecols=cols)
    btc_data = btc_data.sort_values('Date')
    eth_data = eth_data.sort_values('Date')
    btc_data['Change %'] = clean(btc_data['Change %'])  # очищаем данные от лишних знаков и преобразуем
    eth_data['Change %'] = clean(eth_data['Change %'])
    fig, ax = plt.subplots(figsize=(12, 12), nrows=2, ncols=2)  # рисуем графики
    fig.suptitle('Графики для анализа данных')
    ax[0, 0].plot([i for i in range(0, 367)], btc_data['Change %'][:367], label='BTCUSDT')
    ax[0, 0].plot([i for i in range(0, 367)], eth_data['Change %'][:367], label='ETHUSDT', linestyle='dashed')
    ax[0, 0].set_title('Изменение цен BTCUSDT&ETHUSDT в течении года')
    ax[0, 0].legend()
    ax[0, 1].plot([i for i in range(0, 60)], btc_data['Change %'][0:60], label='BTCUSDT')
    ax[0, 1].plot([i for i in range(0, 60)], eth_data['Change %'][0:60], label='ETHUSDT', linestyle='dashed')
    ax[0, 1].set_title('Изменение цен BTCUSDT&ETHUSDT за первые 2 месяца')
    ax[0, 1].legend()
    ax[1, 0].plot([i for i in range(0, 60)], btc_data['Change %'][150:210], label='BTCUSDT')
    ax[1, 0].plot([i for i in range(0, 60)], eth_data['Change %'][150:210], label='ETHUSDT', linestyle='dashed')
    ax[1, 0].set_title('Изменение цен BTCUSDT&ETHUSDT в середине года')
    ax[1, 0].legend()
    ax[1, 1].plot([i for i in range(0, 60)], btc_data['Change %'][307:], label='BTCUSDT')
    ax[1, 1].plot([i for i in range(0, 60)], eth_data['Change %'][307:], label='ETHUSDT', linestyle='dashed')
    ax[1, 1].set_title('Изменение цен BTCUSDT&ETHUSDT за последние 2 месяца')
    ax[1, 1].legend()
    plt.show()
    return btc_data, eth_data
