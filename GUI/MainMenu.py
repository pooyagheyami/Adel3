# In the name of God
# Cearte Menu main Frame File
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Database.wxsq2 as db
import wx
import os
from  Config.Init import *

class MainMenu():
    def __init__(self):
        self.createMenuBar()
        M = MenuData()
        self.m = M.menuBar()
        self.mid = 1001
        #print self.m


    def  createMenuBar(self):
        self.menuBar = wx.MenuBar()
        
        self.mhand = []

        self.m = MenuData()
        

        for eachMenuData in self.m.menuBar():
            menuLabel = eachMenuData[1]
            menuItem = self.m.menuItem(eachMenuData[0])
            
            self.menuBar.Append(self.createMenu(menuItem),menuLabel)
          
        #print self.menuBar    
        return self.menuBar

    def createMenu(self,menuData):
        self.menu = wx.Menu()
        for eachId,eachLabel,eachStatus in menuData:
            
            if not eachLabel:
                self.menu.AppendSeparator()
                continue

            self.menuItem = self.menu.Append(eachId,eachLabel,eachStatus)
        #print self.menu
        return self.menu

    def createHandler(self):
        #print self.menu.GetEventHandler()
        return self.menu.GetEventHandler
    def Onmenu(self,event):
        self.mid=event.GetId()
        #print self.GetItemId()
    def GetItemId(self):
        
        return self.menuItem
    def SetLayDir(self):
        self.menuBar.SetLayoutDirection(2)  
        



class MenuData(db.WXDB):
    def __init__(self,database='Menu.db',pathdb=DATABASE_PATH):
        db.WXDB.__init__(self,'Menu.db',DATABASE_PATH)
        
        self.db=pathdb+database
        #print self.db
        self.connect()

    def menuBar(self):
        c=self.connect()
        #print c
        sql = """ SELECT *
                  FROM menubar,access
                  where menubar.acclvlid = access.acclvlid
                  and access.acclevl = 'FF00'
              """
        self.mbar = []
        for row in   c.execute(sql):
            self.mbar.append(row)
        self.commit()
        #print self.mbar
        return self.mbar
    def menuItem(self,i):
        sql1 =  """SELECT DISTINCT mitem.itemid,mitem.itemname,mitem.status
                     FROM mitem,menubar
                     WHERE mitem.mbarid = """
        sql2 = """
                     ORDER BY mitem.itemid 
                  """
        self.mitem = []
        for itm in self.execute(sql1+str(i)+sql2):
            self.mitem.append(itm)
        #print self.mitem
        return self.mitem
    def menuDir(self):
        sql = """SELECT menubar.mbardir
                 FROM menubar
              """
        self.mdir =[]
        for row in self.execute(sql):
            self.mdir.append(row)
        #print self.mdir
        return self.mdir
        
    
