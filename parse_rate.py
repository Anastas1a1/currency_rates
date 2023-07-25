import pandas as pd

def parse_rate(char_code, date):
    try:
        url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + date
        df = pd.read_xml(url, encoding='cp1251')
    except:
        print('Ошибка получения данных')
        return 0

    res = df.loc[(df['CharCode'] == char_code)]
    print(res['CharCode'].values[0], '( ', res['Name'].values[0], ' ): ',  res['Value'].values[0])


char_code = input('Введите код валюты: ')
date = input('Введите дату в формате дд/мм/гггг: ')

parse_rate(char_code, date)
