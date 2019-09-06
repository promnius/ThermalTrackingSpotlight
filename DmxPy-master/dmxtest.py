from DmxPy import DmxPy
#import pysimpledmx
import time

dmx = DmxPy('/dev/ttyUSB0')
#dmx = pysimpledmx.DMXConnection(0)
#dmx = pysimpledmx.DMXConnection("/dev/ttyUSB0")
#dmx = DmxPy('COM12')
#dmx.setChannel(0, 100)
#dmx.setChannel(1, 100)
dmx.setChannel(2, 100)
dmx.setChannel(3, 100)
print("motion!")
dmx.render()
time.sleep(2)
dmx.setChannel(3, 100)
time.sleep(2)
dmx.blackout()
dmx.render()
