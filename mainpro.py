# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

import wx
import os
import sys

import GUI.window as window
from  Config.Init import *
#import Utility.user as user

class mainApp(wx.App):

    def OnInit(self):
        #check directory and path in config file and program

        #check Databases of program

        #check Date,Time,propertis of file

        #Inter username and password of users
               

        #Check lock if nassesry

        #check hardware and connection
        

        #do main windows of program 

        splash = MySplashScreen()
        splash.Show()


        
        
        return True
  
class MySplashScreen(wx.SplashScreen):
    def __init__(self):
        bmp = wx.Image(opj(SPALSH_PATH+"splash3.jpg")).ConvertToBitmap()
        wx.SplashScreen.__init__(self, bmp,
                                 wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,
                                 5000, None, -1)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.fc = wx.FutureCall(2000, self.ShowMain)


    def OnClose(self, evt):
        # Make sure the default handler runs too so this window gets
        # destroyed
        evt.Skip()
        self.Hide()
        
        # if the timer is still running then go ahead and show the
        # main frame now
        if self.fc.IsRunning():
            self.fc.Stop()
            self.ShowMain()


    def ShowMain(self):
        SIZE = wx.DisplaySize()
        size = (SIZE[0],SIZE[1]-30)

        #do main windows of program 

        frame = window.MainWin()
        frame.SetSize(size)
        frame.SetPosition((1,1))
        #frame.CenterOnScreen()
        
        frame.Show()
        
        #if self.fc.IsRunning():
        #    self.Raise()
        #wx.CallAfter(frame.ShowTip)




if __name__ == '__main__':
    app = mainApp()
    app.MainLoop()
