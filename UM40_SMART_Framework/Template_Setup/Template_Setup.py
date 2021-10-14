# Здесь описан Класс отправки и приема сообщеий JSON
import json
# Декодинг из байтов
from UM40_SMART_Framework.Service import Byte_coding_decoding

from UM40_SMART_Framework.Template_Setup.Template_Types_Setup import \
    SetupTCPIP, \
    SetupDocker, \
    SetupVirtualBox, \
    SetupInsideLauncher, \
    SetupSSH

from sys import getsizeof
from time import sleep


class Setup:
    """
    Класс Запуска

    Из работающих методов - TCP\IP, Docker exet
    TCP\IP:
    Этот Метод отправляет по TCP\IP JSON и его же принимает
    Отдает dict который является JSON Который МЫ получиили

    Это Важно - Он Запускается по умолчанию

    Docker exet

    Этот метод работает ТОЛЬКО c включенным работающим docker контейнером.
    - из всех работающих докер контейнеров берется первый из них,
    и с помомью команды docker exec проваливаемся в контейнер
    - Далее с помощью метода echo наш jSON отправляется в нужную API
    - Для работы необходимо указать имя API

    Поддержанные имена API указаны в файле  Config.py в переменной path_to_API


    VirtualBOX

    Этот метод для

    """
    # Сделаем поле - на всякий случай
    JSON = {}
    jsoninbytes = None
    JSON_answer_byte = None
    JSON_dict = None
    JSON_str = None
    answer_JSON = None
    API = ''
    type_connect = ''
    options_setup = {}

    def __init__(self, JSON, API: str = 'test_api', type_connect: str = 'tcp\ip'):

        """
        Класс Запуска

        Из работающих методов - TCP\IP , Docker exet
        TCP\IP :
        Этот Метод отправляет по TCP\IP JSON и его же принимает
        Отдает dict который является JSON Который МЫ получиили

        Это Важно - Он Запускается по умолчанию

        Docker exet

        Этот метод работает ТОЛЬКО c включенным работающим docker контейнером.
        - из всех работающих докер контейнеров берется первый из них,
        и с помомью команды docker exec проваливаемся в контейнер
        - Далее с помощью метода echo наш jSON отправляется в нужную API
        - Для работы необходимо указать имя API

        Поддержанные имена API указаны в файле  Config.py в переменной path_to_API


        :param JSON: JSON что хотим отправить
        :param API:  имя АПИ - Необходима обязательно для запуска через Докер
        :param type_connect: Строка - нужна чтоб правильно указать способ конекта
        """

        # Итак - переопределяем наши поля
        if type(JSON) is dict:
            from UM40_SMART_Framework.Service.JSON_format_coding_decoding import code_JSON
            JSON = code_JSON(JSON)
        self.JSON = JSON
        self.API = API
        self.type_connect = type_connect

        # Теперь определяем способ конекта
        self.JSON_answer_byte = self.__definition_connection()

        # После того как получили ответ - Надо его декодировать

        # Сначала из байтов
        self.JSON_str = self.__decoding_from_bytes_to_str()

        # Потом из Строки в словарь
        self.JSON_dict = self.__transformation_from_json_to_dict()

        # После этого можно формировать ответ
        self.answer_JSON = self.JSON_dict

    def __definition_connection(self):

        """
        Пока что определяем способ Конекта - Работа с переменной  docker
        :return: Возвращаем наш Способ Конекта
        """

        # print(self.type_connect)
        answer_JSON = self.options_setup.get(self.type_connect)(self)

        # Определяем размер в байтах
        size = getsizeof(answer_JSON)
        sleep(1)
        print('Размер Полученого JSON , bytes : ', size)

        return answer_JSON

    def __decoding_from_bytes_to_str(self):
        # Берем наш байтовый ответ - и декодируем его
        JSON_answer_byte = self.JSON_answer_byte
        try:
            JSON_str = Byte_coding_decoding.from_bytes(JSON_answer_byte)
        except:
            JSON_str = str({"error": "Не удалось распапсить из байт кода"})
        finally:
            return JSON_str

    def __transformation_from_json_to_dict(self):
        # декодируем из json в dict
        JSON_str = self.JSON_str

        try:
            JSON_dict = json.loads(JSON_str)
        except:
            JSON_dict = {}
            JSON_dict['res'] = 999999
            JSON_dict['error'] = 'Ошибка парсинга ответа JSON'
            JSON_dict['JSON_answer'] = [JSON_str]

        finally:
            return JSON_dict

    def __setup_Docker(self):

        """Запуск в локально запущенном докер Контейнере"""
        answer_JSON = SetupDocker(JSON=self.JSON, API=self.API).answer_JSON

        return answer_JSON

    def __setup_TCPIP(self):

        """Запуск через TCPIP"""

        answer_JSON = SetupTCPIP(JSON=self.JSON, API=self.API).answer_JSON

        return answer_JSON

    def __setup_VirtualBox(self):

        """Запуск в гостевой запущенной виртуальной машине"""

        answer_JSON = SetupVirtualBox(JSON=self.JSON, API=self.API).answer_JSON

        return answer_JSON

    def __setup_Launcher_inside(self):

        """Запуск в самой LINUX среде """

        answer_JSON = SetupInsideLauncher(JSON=self.JSON, API=self.API).answer_JSON

        return answer_JSON

    def __setup_SSH(self):

        """Запуск через SSH соединие"""

        answer_JSON = SetupSSH(JSON=self.JSON, API=self.API).answer_JSON

        return answer_JSON

    options_setup = {
                     'tcp\ip': __setup_TCPIP,
                     'docker': __setup_Docker,
                     'virtualbox': __setup_VirtualBox,
                     'linux': __setup_Launcher_inside,
                     'inside_launcher': __setup_Launcher_inside,
                     'ssh': __setup_SSH,
                     }


# def setup(JSON):
#     """
#     Функция запуска
#     :param JSON:
#     :return:
#     """
#     json_total = JSON
#     print('Наш JSON\n', json_total)
#
#     jsoninbytes = Byte_coding_decoding.to_bytes(json_total)
#
#     print('Наш Байтовый JSON\n', jsoninbytes)
#     response = Connection.JSON_SendingReceiving(jsoninbytes)
#     JSON_answer_byte = response.socket_data
#     JSON_str = Byte_coding_decoding.from_bytes(JSON_answer_byte)
#     JSON_dict = json.loads(JSON_str)
#     print('рузультат\n', JSON_dict)
#
#     return JSON_dict
