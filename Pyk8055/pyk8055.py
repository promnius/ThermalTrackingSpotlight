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
        print "Diconnecting the device...",
        self.lib.CloseDevice()
        print "done."
        
    def analog_in(self,channel):
        print "Checking analogue channel %d..." % channel,
        status = self.lib.ReadAnalogChannel(channel)
        print "done."
        return status
    
    def analog_all_in(self):
        data1,data2 = c_int(),c_int()
        print "Checking all analogue channels...",
        self.lib.ReadAllAnalog(byref(data1), byref(data2))
        print "done."
        return data1.value, data2.value
       
    def analog_clear(self,channel):
        print "Clearing analogue channel %d..." % channel,
        self.lib.ClearAnalogChannel(channel)
        print "done."

    def analog_all_clear(self):
        print "Clearing both analogue channels...",
        self.lib.ClearAllAnalog()
        print "done."

    def analog_out(self,channel, value):
        print "Changing the value of analogue channel %d to %d..." % (channel,value),
        if 0 <= value <= 255:
            self.lib.OutputAnalogChannel(channel,value)
            print "done."
        else:
            print
            print "Value must be between (inclusive) 0 and 255"
            
    def analog_all_out(self,data1,data2):
        print "Changing the value of both analogue channels...",
        if 0 <= data1 <= 255 and 0 <= data2 <= 255:
            self.lib.OutputAllAnalog(data1,data2)
            print "done."
        else:
            print
            print "Value must be between (inclusive) 0 and 255"
            
    def digital_write(self, data):
        print "Writing %d to digital channels..." %data,
        self.lib.WriteAllDigital(data)
        print "done."

    def digital_off(self,channel):
        print "Turning digital channel %d OFF..." % channel,
        self.lib.ClearDigitalChannel(channel)
        print "done."

    def digital_all_off(self):
        print "Turning all digital channels OFF...",
        self.lib.ClearAllDigital()
        print "done."
        
    def digital_on(self,channel):
        print "Turning digital channel %d ON..." % channel,
        self.lib.SetDigitalChannel(channel)
        print "done."
    
    def digital_all_on(self):
        print "Turning all digital channels ON...",
        self.lib.SetAllDigital()
        print "done."
         
    def digital_in(self,channel):
        print "Checking digital channel %d..." % channel,
        status = self.lib.ReadDigitalChannel(channel)
        print "done."
        return status

    def digital_all_in(self):
        print "Checking all digital channels..." ,
        status = self.lib.ReadAllDigital()
        print "done."
        return status
        
    def counter_reset(self,channel):
        print "Reseting Counter value...",
        self.lib.ResetCounter(channel)
        print "done,"

    def counter_read(self,channel):
        print "Reading Counter value from counter %d..." % channel,
        status = self.lib.ReadCounter(channel)
        print "done."
        return status
    def counter_set_debounce(self,channel,time):
        if 0<= time <= 5000:
            print "Setting Counter %d's debounce time to %dms..." % (channel,time),
            self.lib.SetCounterDebounceTime(channel,time)
            print "done."
        else:
            print "Time must be between 0 and 5000ms (inclusive)."
            
        
        


