# import UM40_SMART_Framework
#
# from Service.ConfigParser import IP_port, IP_address
#
# Setup = UM40_SMART_Framework.Service(IP_address=IP_address, IP_port=IP_port)
#
# result = Setup(API='lol', JSON='lol', type_connect ='ssh' )
#
# print(result.answer_JSON)


from UM40_SMART_Framework import Setup


JSON = {"method":"put", "table": "MeterTable",
        # 'ids':[]
        'settings': [
{'addr': '1388',
 'id': 1,
 'ifaceCfg': '',
 'ifaceName': 'Iface4',
 'index': 1,
 'pId': 0,
 'passRd': '789456',
 'passWr': '1597531234567890',
 'rtuFider': 0,
 'rtuObjNum': 0,
 'rtuObjType': 0,
 'type': 42,
 'typeName': 'SPODES_MILUR'}
]

}

# {'measures': [{'devices': [{'deviceIdx': 1, 'id': 0, 'meter': 1, 'vals': [{'tags': [{'tag': 'const', 'val': None}, {'tag': 'kI', 'val': 1.0}, {'tag': 'kU', 'val': 1.0}, {'tag': 'cArrays', 'val': 1}, {'tag': 'isAm', 'val': True}, {'tag': 'isClock', 'val': True}, {'tag': 'isDst', 'val': False}, {'tag': 'isRm', 'val': True}, {'tag': 'isRp', 'val': True}, {'tag': 'isTrf', 'val': True}, {'tag': 'model', 'val': ''}, {'tag': 'serial', 'val': '211500050411372'}], 'ts': 1635752804}]}], 'measure': 'ElConfig'}], 'res': 0}
JSON =  {"measures": ["ElConfig"], "ids": [1], "tags": [], "time": [], "flags": [], "method": "get"}

# JSON = {"method": "post", "measures": [
#                            {"measure": "ElConfig", "devices": [
#                             {"id": 1, "vals": [{"ts": 1635752804, "tags": [
#                                                                            {"tag": "serial", "val": "0110188597"},
#                                                                            {'tag': 'const', 'val': None},
#                                                                            {'tag': 'kI', 'val': 1.0},
#                                                                            {'tag': 'kU', 'val': 1.0},
#                                                                            {'tag': 'cArrays', 'val': 1},
#                                                                            {'tag': 'isAm', 'val': True},
#                                                                            {'tag': 'isClock', 'val': True},
#                                                                            {'tag': 'isDst', 'val': False},
#                                                                            {'tag': 'isRm', 'val': True},
#                                                                            {'tag': 'isRp', 'val': True},
#                                                                            {'tag': 'isTrf', 'val': True},
#                                                                            {'tag': 'model', 'val': ''}
# ]}]}]}]}


JSON = {"method":"get", "table": "MeterTable"}




answer = Setup(JSON=JSON, API="meter_db_settings", type_connect='ssh')


print(answer)