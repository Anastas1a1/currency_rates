import pandas as pd


def fetch_exchange_rate(char_code=None, num_code=None, date='25/07/2023'):
    try:
        url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + date
        df = pd.read_xml(url, encoding='cp1251')
    except Exception as e:
        print('Произошла ошибка при получении данных:', e)
        return None

    try: 
        if char_code:
            res = df.loc[df['CharCode'] == char_code]
            if res.empty:
                print('Валюта с кодом', char_code, 'не найдена.')
                return None
        elif num_code:
            res = df.loc[df['NumCode'] == num_code]
            if res.empty:
                print('Валюта с кодом', num_code, 'не найдена.')
                return None
            char_code = res['CharCode'].values[0]
        currency_name = res['Name'].values[0]
        exchange_rate = res['Value'].values[0]

        print(f'Код валюты: {char_code} ( {currency_name} ): {exchange_rate}')
        return exchange_rate
    except Exception as e:
        print('Произошла ошибка при обработке данных:', e)
        return None

if __name__ == "__main__":
    code = input('Введите код валюты: ')
    date = input('Введите дату в формате дд/мм/гггг: ')
    if code.isdigit():
        exchange_rate = fetch_exchange_rate(num_code=int(code), date=date)
    else:
         exchange_rate = fetch_exchange_rate(char_code=code, date=date)
    

   
