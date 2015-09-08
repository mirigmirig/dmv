import platform
import os
import signal

if __name__ == "__main__":

	#program termination
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	if platform.system()=="Linux":
		import dmv_indicator
		app_tray = dmv_indicator.LinuxTray()
		app_tray.run_indicator()
	else:
		#Win option
		import dmv_task_bar_icon
    		app_tray = wx.App(False)
    		dmv_task_bar_icon.TaskBarIcon()
		app_tray.MainLoop()


		
