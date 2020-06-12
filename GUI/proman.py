# In the name of God
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Database.wxsq2 as DB
import os
from Config.Init import *

class Mymenu(DB.WXDB):
    def __init__(self,database='Menu.db',pathdb=DATABASE_PATH):
        DB.WXDB.__init__(self,database,pathdb)
        self.database=pathdb+database
        #print self.database
        self.connect()
    def connectit(self):
        
        self.con =  self.connect()
        with self.con:
            
            return self.con.cursor() 
        
        
#imenu = Mymenu()
#print imenu.connect()

def program(itemid):
    
    handler = []
    #imenu.connect()
    imenu = Mymenu()
    #print imenu.database

    sql1 = """SELECT mitem.itemid, mitem.handler
            FROM mitem
            WHERE mitem.itemid = """
    handler = imenu.execute(sql1+str(itemid))
    #c.close()
    #print handler
    return handler[0][1]


def menudir(itemid):
    directory = ''
    #print itemid
    imenu = Mymenu()
    

    #han=WXDB.WXDB('Menu.db')
    sql = """ SELECT menubar.mbardir
              FROM mitem  JOIN menubar
              ON mitem.mbarid = menubar.mbarid
              WHERE mitem.itemid = """
    directory = imenu.execute(sql+str(itemid))
    #print directory[0][0]
    return directory[0][0]

def DoProgram(item):
    #print item
    
    
    p=program(item)
    d=menudir(item)
    imenu = Mymenu()
    #r = WXDB.WXDB("Menu.db")
    sql = """select mitem.handler
          from mitem
          WHERE  mitem.handler  notnull
          """
    I=imenu.execute(sql)
    #print I
    Ii =[]
    for it in I:
        Ii.append(it[0])
    #print Ii
    a=d+'.'+p
    i = __import__(a,globals(),locals(),Ii,-1)
    #print dir(i)
    #i.main()

    return i
