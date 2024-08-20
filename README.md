### Описание задачи:

Задание состоит из двух частей:

1. Определить собственные движения цены фьючерса ETHUSDT, исключив из них движения, вызванные влиянием цены BTCUSDT. Описать выбранную методику, подобранные параметры и обоснование в README.
2. Написать программу на Python, которая в реальном времени (с минимальной задержкой) следит за ценой фьючерса ETHUSDT и, используя выбранный метод, определяет собственные движения цены ETH.
   При изменении цены на 1% за последние 60 минут, программа выводит сообщение в консоль. Программа должна продолжать работать дальше, постоянно считывая актуальную цену.Для определения
   собственных движений цены фьючерса ETHUSD, независимых от цены BTCUSD, можно использовать методы статистического анализа временных рядов.
   
Решение.

Одним из таких методов является метод «регрессии» (анализа корреляции) – позволяющий оценить силу и направление связи между двумя переменными. В данном случае переменные -это цены на фьючерсы ETHUSD и BTCUSD.
Для анализа необходимо:
Получить исторические данные о ценах обоих активов. Такие данные предоставляет сайт https://www.investing.com/
1.	Определить зависимую и независимую переменные. В нашем случае, зависимая переменная – цена ETHUSD, независимая переменная -цена BTCUSD,
2.	Подобрать функцию, описывающую взаимосвязь между переменными. Возможные варианты моделей регрессии: линейна, нелинейная, многофакторная и т.д. В работе использовалась линейная модель регрессии,
так как она достаточно проста в использовании и не требует большого количества вычислений.
4.	Был проведен анализ коэффициента корреляции между переменными. Коэффициент корреляции позволяет оценить силу связи между двумя переменными и может принимать значения от -1 до 1. Значение коэффициента
корреляции близкое к 0 говорит о том, что связь между переменными отсутствует. Значение близкое к 1 говорит о том, что связь между переменными положительная и тесная. Значение близкое к -1, что связь между
переменными отрицательна и тесная.
6.	Если коэффициент корреляции между ETHUSD  и  BTCUSD будет статистически значимым и близким к 1 или -1, значит, цена ETHUSD тесно связана с ценой BTCUSD и не отображает в полной мере собственные движения.
В этом случае для разделения собственных движений цен монет можно попробовать воспользоваться методами «Фильтра Калмана» или «Вейвлет-преобразованиями».
8.	Для подбора параметров модели регрессии использовался метод наименьших квадратов (МНК), который позволяет оценить параметры модели таким образом, чтобы ошибка между предсказанным значением и фактическим
значением была минимальна. В данном случае, в качестве параметром модели будут выступать коэффициенты a и b в уравнении регрессии y=a+bx, где y- цена ETHUSD,  a -сдвиг на ось y, b – коэффициент наклона

Таким образом, для определения собственных движений цены фьючерса ETHUSD, независимых от цены BTCUSD был использованы методы статистического анализа временных рядов, а именно метод регрессии. Определен
коэффициент корреляции между переменными, выбрана функция регрессии и ее параметры, а также добавлен дополнительны метод для разделения собственных движений цены.
Так как корелляция между фьючерсами очевидна (указана в задании и видна при первичном анализе), допускается возможность "вычесть" влияние BTCUSDT из ETHUSDT. То есть амплитуду изменения цены BTCUSDT буквально
отнимаем от аналогичного показателя ETHUSDT.
Например (приблизительные, округлённые для наглядности данные): В 18:00 ETHUSDT стоит - 1700, BTCUSDT - 27000, в 18:01 ETHUSDT стоит - 1750, BTCUSDT - 27100.
Согласно предложенной методике, мы сравниваем первый показатель со вторым для обоих фьючерсов, получаем, ETHUSDT: + ~2,9411, BTCUSDT + ~0,3703. Чистое изменение ETHUSDT = ~2,5708 (2,9411-0,3703)
