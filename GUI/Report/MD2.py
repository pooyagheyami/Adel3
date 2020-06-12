#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
from MDftar4 import *


class telframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL)
        self.parent=parent

                       
        self.panel = MyPanel1(self)

        
    def closeit(self):
        self.Close(True)

def size():
    return (870,440)

def main(panel=None ):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    
    parent =  panel.GetParent()
    
    frame = telframe(parent )
    frame.SetTitle(u'دفتر املاک')
    frame.SetSize(size())
    #frame.SetPosition((1000,100))
    frame.Show()
    

    

if __name__ == '__main__':
    #app = wx.App(False) 
    main()
    #app.MainLoop()
    
