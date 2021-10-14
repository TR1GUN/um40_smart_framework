# Здесь парсим наши данные для того чтоб сделать коннект к Железке
import configparser
import os

# ----------------------------------------------------------------------------
# path ='/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
#
settings = 'settings.ini'


# Ищем директорию
def passage(file_name, folder):
    for element in os.scandir(folder):
        if element.is_file():
            if element.name == file_name:
                yield folder
        else:
            yield from passage(file_name, element.path)


# настройки берем из конфига
parser = configparser.ConfigParser()
parser.read(os.path.join(*passage(settings, os.getcwd()), settings))

import UM40_SMART_Framework

UM40_SMART_Framework.IP_address = parser['Test']['IP_address']
UM40_SMART_Framework.IP_port = parser['Test']['IP_port']
UM40_SMART_Framework.user_login = parser['Test']['user_login']
UM40_SMART_Framework.user_password = parser['Test']['user_password']
UM40_SMART_Framework.domain = parser['Test']['domain']
UM40_SMART_Framework.machine_name = parser['Test']['machine_name']
# ----------------------------------------------------------------------------
