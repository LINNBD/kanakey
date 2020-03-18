# This code is an example for a tutorial on Ubuntu Unity/Gnome AppIndicators:
# http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html

import os
import gi
import signal
import json

from urllib import request
from urllib.error import URLError
from urllib.request import urlopen

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify


APPINDICATOR_ID = 'myappindicator'

def main():
    indicator = appindicator.Indicator.new("customtray", os.path.abspath('icon.svg'), appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    item_EN_Layout = gtk.MenuItem('English(US)')
    item_EN_Layout.connect('activate', EN_Layout)
    menu.append(item_EN_Layout)
    item_JP_Layout = gtk.MenuItem('Japanese(日本語)')
    item_JP_Layout.connect('activate', JP_Layout)
    menu.append(item_JP_Layout)
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

# def fetch_EN_Layout():
#     with urlopen('http://api.icndb.com/jokes/random?limitTo=[nerdy]') as req:
#         msg = req.read()
#         msg = msg.decode('utf-8')
#         EN_Layout = json.loads(msg)['value']['EN_Layout']
#     return EN_Layout

# def EN_Layout(_):
#     notify.Notification.new("<b>EN_Layout</b>", fetch_EN_Layout(), None).show()

def EN_Layout(_):
    notify.Notification.new("Switched to English Input").show()

# def fetch_JP_Layout():
#     with urlopen('http://api.icndb.com/jokes/random?limitTo=[nerdy]') as req:
#         msg = req.read()
#         msg = msg.decode('utf-8')
#         JP_Layout = json.loads(msg)['value']['JP_Layout']
#     return JP_Layout

def JP_Layout(_):
    notify.Notification.new("Switched to Japanese Input").show()

def quit(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()