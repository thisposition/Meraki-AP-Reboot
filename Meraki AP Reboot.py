import time
import meraki

API_Key = 'insert API key here'
dashboard = meraki.DashboardAPI(API_Key)
serials = ['Insert', 'Serial', 'Numbers', 'in', 'this', 'format']

for serial in serials:
    response = dashboard.devices.rebootDevice(serial)
    print(response)
    time.sleep(60)
