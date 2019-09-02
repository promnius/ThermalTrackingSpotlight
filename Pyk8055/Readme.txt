A Python module created to interact with the Velleman K8055 kit.

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



Prerequisites:
----------------

- Requires K8055D.dll to be in the same directory/folder.


Info:
------

I created this so that I could tinker with the kit in the current language I was using and most fluent in(Python). 
It seamlessly intergrates it as an object, allowing you to access it various functions with ease.Error handeling isn't really there,
but provided you access the module normally and the dll is present, there should be no problems.


Files:
--------
- K8055D.dll Dynamic Link Library file for K8055 device from  http://www.velleman.eu/downloads/files/downloads/k8055dll_rev3_0_2.zip
- pyk8055.py Module to interact with the k8055 device. Fully verbose.
- pyk8055-nv.py is the Non-verbose version of the pyk8055.py. It will only show messages when connecting/disconnecting the device and 
on one or two functions where you must enter a value between two limits.

Supports all functions in the K8055D.dll.