
print("Hello World!")
import pyenttec as dmx
port = dmx.select_port(1)
port.dmx_frame[0] = 123
port.render()