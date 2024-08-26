import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def building_model(btc_data, eth_data):
    """
    Строит модель линейной регрессии и выводит результаты.

    :param btc_data: Данные BTC
    :param eth_data: Данные ETH
    :return: Модель линейной регрессии
    """
    # X = np.array(btc_data['Change %']).reshape(-1, 1)  # Формируем исходные данные
    # y = np.array(eth_data['Change %'])
    X = btc_data[['Change %']] # Формируем исходные данные
    y = eth_data['Change %']
    X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size=0.5, random_state=0)
    model = LinearRegression()  # Создание модели линейной регрессии
    model.fit(X_train, y_train)  # Обучение модели на обучающем наборе
    y_pred = model.predict(X_test)   # Прогнозирование на тестовой выборке
    mse = mean_squared_error(y_test, y_pred)   # Вычисление метрик качества
    r2 = r2_score(y_test, y_pred)
    print(f'MSE (Среднеквадратическая ошибка): {mse}')
    print(f'R² (Коэффициент детерминации): {r2}\n')
    plt.scatter(X_test, y_test, label='real')  # Рисуем график
    plt.scatter(X, model.predict(X), label='predict')
    plt.legend()
    plt.xlabel('Реальные значения')
    plt.ylabel('Предсказанные значения')
    plt.title('Реальные и предсказанные значения')
    plt.show()
    return model
