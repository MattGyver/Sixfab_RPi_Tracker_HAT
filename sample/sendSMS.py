'''
  sendSMS.py - This is basic SMS Service example.
  Created by Yasin Kaya (selengalp), January 2, 2019.
'''
from gprsiot import gprsiot
import time

node = gprsiot.gprsiot()
node.disable()
time.sleep(0.5)
node.enable()
time.sleep(0.5)
node.powerUp()

node.getResponse("RDY")
node.sendATComm("ATE1","OK\r\n")

node.sendSMS("xxxxxxxxxxxxx","hello world!")
