#! /bin/python3

import dbus
from dbus import SystemBus, Interface
from gi.repository import GLib

def interface_added():
	print("Interface Added")
	#print("  Object Path: %r" % (object_path))
    
def interface_removed():
	print("Interface Removed")
	#print("  Object Path: %r" % (object_path))

loop = GLib.MainLoop()
bus = SystemBus()

if __name__ == "__main__":

	systemd = bus.get_object("org.freedesktop.systemd1", "/org/freedesktop/systemd1")
	manager = Interface(systemd, dbus_interface='org.freedesktop.systemd1.Manager')

	disk_systemd = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
	disk_manager = Interface(disk_systemd, dbus_interface='org.freedesktop.DBus.ObjectManager')

	disk_manager.connect_to_signal('InterfacesAdded', interface_added)
	disk_manager.connect_to_signal('InterfacesRemoved', interface_removed)

	'''units = manager.ListUnits()

	for unit in units:
		print(unit)
	'''
	loop.run()
