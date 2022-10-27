#!/usr/bin/python3
import dbus
import json
bus = dbus.SystemBus()
ud_manager_obj = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
om = dbus.Interface(ud_manager_obj, 'org.freedesktop.DBus.ObjectManager')
for k,v in om.GetManagedObjects().items():
  drive_info = v.get('org.freedesktop.UDisks2.Drive', {})
  drive_properties = v.get('org.freedesktop.UDisks2.Drive.Ata')
  #if drive_info.get('ConnectionBus') == 'usb' and drive_info.get('Removable'):
  #if drive_info['MediaRemovable']:
  print("Device Path: %s" % k)
  print(json.dumps(drive_info, indent=4, sort_keys=True))
  print(json.dumps(drive_properties, indent=4, sort_keys=True))
