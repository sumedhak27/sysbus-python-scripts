#! /usr/bin/python3
import dbus
import json
bus = dbus.SystemBus()
obj = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2/drives/ST1000LM035_1RK172_ZDE3LVZW')
inf = dbus.Interface(obj, 'org.freedesktop.DBus.Properties')
res = inf.GetAll('org.freedesktop.UDisks2.Drive.Ata')
print(json.dumps(res, indent=4, sort_keys=True))
