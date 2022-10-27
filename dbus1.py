#! /bin/python

import dbus
_bus = dbus.SystemBus()
systemd = _bus.get_object("org.freedesktop.systemd1", "/org/freedesktop/systemd1")
_manager = dbus.Interface(systemd, dbus_interface='org.freedesktop.systemd1.Manager')
units = _manager.ListUnits()
for unit in units:
    print(unit)
