'''
  ThingSpeak.py - This is send data to ThingSpeak via http post method.
  Created by Metin KOC (saucompeng), September 11, 2018.
'''
from gprsiot import gprsiot
import time

api_key = "XXXXXXXXXXXXX"; # change with api-key

data = "field1=%d"

node = gprsiot.GPRSIoT()
node.disable()
node.enable()
node.powerUp()

node.sendATComm("ATE1","OK\r\n")

node.getIMEI()
time.sleep(0.5)
node.getFirmwareInfo()
time.sleep(0.5)
node.getHardwareInfo()
time.sleep(0.5)

node.setGSMBand(node.GSM_900)
time.sleep(0.5)
node.setMode(node.GSM_MODE)
time.sleep(0.5)

node.connectToOperator()
time.sleep(0.5)
node.getSignalQuality()
time.sleep(0.5)
node.getQueryNetworkInfo()
time.sleep(0.5)

node.deactivateContext()
time.sleep(0.5)
node.activateContext()
time.sleep(0.5)

node.sendDataThingspeak(api_key, data % node.readTemp())


