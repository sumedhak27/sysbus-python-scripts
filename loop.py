#! /usr/bin/python3

import dbus
from gi.repository import GLib

loop = GLib.MainLoop()
bus = dbus.SystemBus(mainloop=loop)
dbus.set_defalut_main_loop(loop)

def interface_added(self, object_path):
    print("Interface added : %s" % (object_path))

def interface_removed(self, object_path):
    print("INterface removed : %s" %(object_path))

disk_systemd = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
disk_manager = dbus.Interface(disk_systemd, dbus_interface='org.freedesktop.DBus.ObjectManager')
disk_manager.connect_to_signal('InterfacesAdded', interface_added)
disk_manager.connect_to_signal('InterfacesRemoved', interface_removed)

loop.run()

