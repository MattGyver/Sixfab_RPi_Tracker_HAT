'''
  basicUDP.py - This is basic UDP example.
  Created by Yasin Kaya (selengalp), January 2, 2019.
'''
from gprsiot import gprsiot
import time

your_ip = "xx.xx.xx.xx" # change with your ip
your_port = "xxxx" # change with your port

node = gprsiot.gprsiot()
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

node.setIPAddress(your_ip)
time.sleep(0.5)
node.setPort(your_port)
time.sleep(0.5)

node.setGSMBand(node.GSM_900)
time.sleep(0.5)
node.setCATM1Band(node.LTE_B5)
time.sleep(0.5)
node.setNBIoTBand(node.LTE_B20)
time.sleep(0.5)
node.getBandConfiguration()
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

node.closeConnection()
time.sleep(0.5)
node.startUDPService()
time.sleep(0.5)

node.sendDataUDP("Hello World!\r\n")
time.sleep(0.5)
