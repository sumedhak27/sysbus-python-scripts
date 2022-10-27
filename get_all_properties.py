#! /usr/bin/python3

import dbus
import json

bus = dbus.SystemBus()
obj1 = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
inf1 = dbus.Interface(obj1, 'org.freedesktop.DBus.ObjectManager')
res1 = inf1.GetManagedObjects()
for obj in res1:
    print(obj)
