#In the name of God
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import Pnl0
from  Config.Init import *

class telframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.parent=parent

        txt = thistxt('about.txt')
        btn = u'تائيد'
               
        self.panel = Pnl0.MyPanel1(self,txt,btn)

        
    def closeit(self):
        self.Close(True)

def size():
    return (-1,-1)

def main(panel=None ):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    
    parent =  panel.GetParent()
    
    frame = telframe(parent )
    frame.SetTitle(u'درباره')
    frame.SetSize((400,300))
    frame.Show()
    

    

if __name__ == '__main__':
    #app = wx.App(False) 
    main()
    #app.MainLoop()
    
