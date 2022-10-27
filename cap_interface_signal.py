#! /usr/bin/python3
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GObject as gobject
import pprint
import json

class MessageListener:
    def __init__(self):
        print("Initializing System Bus and bus loop")
        DBusGMainLoop(set_as_default=True)
        _loop = gobject.MainLoop()
        self._bus = dbus.SystemBus()

        print("Initializing object and an interface ")
        disk_systemd = self._bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
        self._disk_manager = dbus.Interface(disk_systemd, dbus_interface='org.freedesktop.DBus.ObjectManager')

        print("Connect the code to listen to interface signal")
        self._disk_manager.connect_to_signal('InterfacesAdded', self._interface_added)
        self._disk_manager.connect_to_signal('InterfacesRemoved', self._interface_removed)

        _loop.run()

    def _interface_added(self, object_path, properties):
        if properties.get("org.freedesktop.UDisks2.Drive") is not None :
            print("Interface added.")
            print("Object Path : %s" %(object_path))
            pprint.pprint(json.dumps(properties["org.freedesktop.UDisks2.Drive"], indent=4, sort_keys=True))

    def _interface_removed(self, object_path, interfaces):
        for interface in interfaces:
            if interface=="org.freedesktop.UDisks2.Drive":
                print("Interface removed.")
                print("Object Path : %s" %(object_path))

if __name__ == "__main__" :
    MessageListener()

