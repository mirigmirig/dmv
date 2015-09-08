__author__ = 'Masha'

import wx
import subprocess
import os
import sys
import ctypes


TRAY_TOOLTIP = 'DMV BOT DEMO'
TRAY_ICON = 'icon.png'


def create_menu_item(menu, label, func, enabled):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    if enabled:
        item.Enable(False)
    else:
        item.Enable(True)
    menu.AppendItem(item)
    return item


class TaskBarIcon(wx.TaskBarIcon):
    def __init__(self):
        super(TaskBarIcon, self).__init__()
        self.started = False
        self.set_icon(TRAY_ICON)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Start Bot', self.start_bot, self.started)
        menu.AppendSeparator()
        create_menu_item(menu, 'Quit', self.quit, False)
        return menu

    def set_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)

    def start_bot(self, event):
        self.started = True
        #my_path = os.path.abspath(__file__)
        #mydir = os.path.dirname(my_path)
        #start = os.path.join(mydir, r"prog_exe\bot_gui.exe")
        #ctypes.windll.user32.MessageBoxA(0, my_path + " " + mydir +  " " + start, "Accept?", 1)
        #ctypes.windll.user32.MessageBoxA(0, sys.executable, "Accept?", 1)
        #self.proc = subprocess.Popen(start)
        #self.proc = subprocess.Popen(["python", "bot_gui.py"])


    def quit(self, event):
        if hasattr(self, 'proc'):
            self.proc.terminate()
        wx.CallAfter(self.Destroy)
