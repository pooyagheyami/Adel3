#In the name of God
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
from  abr1 import *

class telframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL)
        self.parent=parent
                       
        self.panel = MyPanel1(self)
        
    def closeit(self):
        self.Close(True)
def size():
    return (100,250)

def main(panel=None ):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    
    parent =  panel.GetParent()
    
    frame = telframe(parent )
    frame.SetTitle(u'پشتيباني')
    frame.SetSize(size())
    frame.SetPosition((900,400))
    frame.Show()
    

    

if __name__ == '__main__':
    #app = wx.App(False) 
    main()
    #app.MainLoop()
    
