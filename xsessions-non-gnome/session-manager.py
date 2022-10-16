#!/usr/bin/python3
import gi
import dbus
import dbus.service
import dbus.mainloop.glib
import os
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk
os.environ["PATH"]="/bin:/sbin:/usr/bin:/usr/sbin"

class Dialog(Gtk.Window):
    def __init__(self,primary="",secondary="",title=""):
        super().__init__(title=title)
        self.dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text=primary,
        )
        self.dialog.format_secondary_text(secondary)
    def run(self):
        response = self.dialog.run()
        ret = (response == Gtk.ResponseType.YES)
        self.dialog.destroy()
        return ret


class Service(dbus.service.Object):
   def __init__(self, message):
      self._message = message

   def run(self):
      dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
      bus_name = dbus.service.BusName("org.gnome.SessionManager", dbus.SessionBus())
      dbus.service.Object.__init__(self, bus_name, "/org/gnome/SessionManager")
      self._loop = GLib.MainLoop()
      self._loop.run()

   @dbus.service.method("org.gnome.SessionManager", in_signature='', out_signature='')
   def Logout(self,a):
      if Dialog("Log out of this system now?","Are you want to close all windows and log out?").run():
          os.system("pkill -KILL -u "+os.environ["USER"])
      
   @dbus.service.method("org.gnome.SessionManager", in_signature='', out_signature='')
   def Shutdown(self):
      if Dialog("Poweroff of this system now?","Are you want to close all windows and poweroff?").run():
          os.system("pkexec /usr/bin/gnome-session-quit --power-off")
      
   @dbus.service.method("org.gnome.SessionManager", in_signature='', out_signature='')
   def Reboot(self):
      if Dialog("Reboot of this system now?","Are you want to close all windows and reboot?").run():
          os.system("pkexec /usr/bin/gnome-session-quit --reboot")

Service(None).run()
