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
JSON = {"job": "ElConfig", "time": [{"start": 1633896000, "end": 1633899600}], "meters": [{"type": 94, "iface": "Ethernet", "address": "192.168.205.6:2002"}, {"type": 5, "password": "373737373737", "deviceidx": 0, "iface": "Hub", "address": "134256651", "uart": "9600,8n1"}]}


JSON = {"method":"get", "table": "MeterTable"}
answer = Setup(JSON=JSON, API="meter_db_settings", type_connect='ssh')
print(lol)
