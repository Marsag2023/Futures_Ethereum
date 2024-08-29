import historydata
import sklmodel
from realdata import get_realdata, own_movement, moving_average
import time
import datetime
if __name__ == '__main__':
    btc_data, eth_data = historydata.output_graphs()
    model = sklmodel.building_model(btc_data, eth_data)
    while True:
        prices_eth, prices_btc = get_realdata()
        eth_reg = own_movement(model, prices_eth, prices_btc)
        eth_ma = moving_average(prices_eth, prices_btc)
        current_time = 0
        if eth_reg <= -1 or eth_reg >= 1:
            current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            print("\033[31m {:*^70}".format(''))
            print("\033[31m {}".format(f'Текущее время: {current_time}'))
            print("\033[31m {}".format(f'Изменение цены ETH с учетом обученой модели: {eth_reg}'))
            print("\033[31m {:*^70}".format(''))
        if eth_ma <= -1 or eth_ma >= 1:
            print("\033[34m {:*^70}".format(''))
            print("\033[34m {}".format(f'Текущее время: {current_time}'))
            print("\033[34m {}".format(f'Изменение цены ETH с учетом скользящих средних: {eth_ma} % '))
            print("\033[34m {:*^70}".format(''))
        time.sleep(60)
