#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
from InM6 import *
#import Pmenu


class telframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL)
        self.parent=parent

        #self.panel = Pmenu.MPanel(self)
        self.panel = MyPanel1(self)
        #self.SetLayoutDirection(2)
            
        
    def closeit(self):
        self.Close(True)

def size():
    return (160,280)

def main(panel=None ):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    
    parent =  panel.GetParent()
    
    frame = telframe(parent )
    frame.SetTitle(u'ملک جديد')
    frame.SetSize(size())
    SIZE = wx.DisplaySize()
    #print SIZE
    #frame.SetPosition((900,100))
    frame.SetPosition((SIZE[0]-170,100))
    frame.Show()
    

    

if __name__ == '__main__':
    #app = wx.App(False) 
    main()
    #app.MainLoop()
    
