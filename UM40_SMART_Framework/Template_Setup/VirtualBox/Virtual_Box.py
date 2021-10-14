# Здесь расположим Поиск нашей виртуальной машины -
# Это важно - вынести в отдельный файл - тк необходимо при запуске в многопоточном режиме
from UM40_SMART_Framework.Config import machine_name
import virtualbox
vbox = virtualbox.VirtualBox
vbox = vbox()

# Ищем нашу виртуальную тачку
vm = vbox.find_machine(machine_name)