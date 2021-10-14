# Здесь пускай валяются общие конфиги


# Конфиг для определеняи пути апих.

path_to_API = \
    {
        'meterdev': '/etc/opt/uspd/meterdev/meterdev',
        'meter_db_data_api': '/etc/opt/uspd/meter_db_data_api/meter_db_data_api',
        'meter_db_settings': '/etc/opt/uspd/meter_db_settings_api/meter_db_settings_api',
        'uspd-meter_daemon': 'mosquitto_pub -t \'/meterdaemon/\' --stdin-line',
        'event_db_api': '/etc/opt/uspd/event_db_api/event_db_api',
        # файл является процессом для работы с БД настроек брокеров MQTT и аккаунтов SMTP
        'messenger_db_api': "/etc/opt/uspd/messenger_db_api/messenger_db_api",
        # файл является процессом для работы c БД iec60870 (JSON API)
        'iec60870_db_api': "/etc/opt/uspd/iec60870_db_api/iec60870_db_api",
        # файл является процессом для работы c БД зарядных станций (JSON API)
        'charge_stations_db_api': "/etc/opt/uspd/charge_stations_db_api/charge_stations_db_api",
    }

import UM40_SMART_Framework

IP_address = UM40_SMART_Framework.IP_address
IP_port = UM40_SMART_Framework.IP_port
user_login = UM40_SMART_Framework.user_login
user_password = UM40_SMART_Framework.user_password
domain = UM40_SMART_Framework.domain
machine_name = UM40_SMART_Framework.machine_name

# def ConfigParser():
#     # Здесь парсим наши данные для того чтоб сделать коннект к Железке
#     import configparser
#     import os
#     # ----------------------------------------------------------------------------
#     # path ='/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
#     path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
#
#     settings = '../settings.ini'
#     # настройки берем из конфига
#     parser = configparser.ConfigParser()
#     parser.read(os.path.join(path, settings))
#
#     import UM40_SMART_Framework
#
#     UM40_SMART_Framework.IP_address = parser['Test']['IP_address']
#     UM40_SMART_Framework.IP_port = parser['Test']['IP_port']
#     UM40_SMART_Framework.user_login = parser['Test']['user_login']
#     UM40_SMART_Framework.user_password = parser['Test']['user_password']
#     UM40_SMART_Framework.domain = parser['Test']['domain']
#
#     global IP_address = None
#     global IP_port = None
#     global user_login = None
#     global user_password = None
#     global domain = None
#
#     IP_address = None
#     IP_port = None
#     user_login = UM40_SMART_Framework.user_login
#     user_password = UM40_SMART_Framework.user_password
#     domain = UM40_SMART_Framework.domain
#
#     # ----------------------------------------------------------------------------
