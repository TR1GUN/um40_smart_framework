IP_address = None
IP_port = None
user_login = None
user_password = None
domain = None
machine_name = None

from UM40_SMART_Framework.Service import ConfigParser
#
# print(IP_address)
# print(IP_port)
# print(user_login)
# print(user_password)


def Setup(JSON, API: str = 'test_api', type_connect: str = 'tcp\ip'):
    from UM40_SMART_Framework.Template_Setup.Template_Setup import Setup

    answer = Setup(JSON=JSON, API=API, type_connect=type_connect).answer_JSON

    return answer
