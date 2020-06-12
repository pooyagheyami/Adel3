#In the name of God
# -*- coding: utf-8 -*-
#!usr/bin/env python



import wx


def size():
    return (-1,-1)

def main(panel=None):
    
    q= wx.GetActiveWindow()
    p= wx.GetApp()
    
    if str(q) == 'None':
        p.Exit()
        wx.App_CleanUp()
    else:
        #print q.m_mgr
        q.m_mgr.UnInit()
        q.Destroy()
        wx.App_CleanUp()
    
if __name__ == '__main__':
    main(None)
