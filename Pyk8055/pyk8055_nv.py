'''
A Python module created to interact with the Velleman K8055 kit

Created By Fergus Leahy a.k.a. Fergul Magurgul
(https://sourceforge.net/projects/pyk8055/)

Copyright (C) 2010  Fergus Leahy (http://py-hole.blogspot.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

#  - Requires K8055D.dll to be in the same directory/folder.

from ctypes import *

class device():
    def __init__(self,port=0):
        print "Loading K8055 dll...",
        try:
            self.lib = WinDLL("K8055D.dll")
            print "done."
        except:
            print "failed!"
            print "Failed to find K8055d.dll in local folder."
            return
        print "Accessing the device on port %d..." % port,
        self.lib.OpenDevice(port)
        print "done."
        
    def disconnect(self):
        self.lib.CloseDevice()
        
    def analog_in(self,channel):        
        return self.lib.ReadAnalogChannel(channel)
    
    def analog_all_in(self):
        data1,data2 = c_int(),c_int()
        self.lib.ReadAllAnalog(byref(data1), byref(data2))
        return data1.value, data2.value
       
    def analog_clear(self,channel):
        self.lib.ClearAnalogChannel(channel)
    
    def analog_all_clear(self):
        self.lib.ClearAllAnalog()

    def analog_out(self,channel, value):
        if 0 <= value <= 255:
            self.lib.OutputAnalogChannel(channel,value)
        else:
            print "Value must be between (inclusive) 0 and 255"
            
    def analog_all_out(self,data1,data2):
        if 0 <= data1 <= 255 and 0 <= data2 <= 255:
            self.lib.OutputAllAnalog(data1,data2)
        else:
            print "Value must be between (inclusive) 0 and 255"
            
    def digital_write(self, data):
        self.lib.WriteAllDigital(data)

    def digital_off(self,channel):
        self.lib.ClearDigitalChannel(channel)

    def digital_all_off(self):
        self.lib.ClearAllDigital()
       
    def digital_on(self,channel):
        self.lib.SetDigitalChannel(channel)
    
    def digital_all_on(self):
        self.lib.SetAllDigital()
         
    def digital_in(self,channel): 
        return self.lib.ReadDigitalChannel(channel)
    
    def digital_all_in(self):
        return self.lib.ReadAllDigital()
    
    def counter_reset(self,channel):
        self.lib.ResetCounter(channel)
    
    def counter_read(self,channel):
        return self.lib.ReadCounter(channel)

    def counter_set_debounce(self,channel,time):
        if 0<= time <= 5000:
            self.lib.SetCounterDebounceTime(channel,time)
        else:
            print "Time must be between 0 and 5000ms (inclusive)."
            
        
        


