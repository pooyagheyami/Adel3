# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import GUI.proman as pro

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"بخش بايگاني", pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, 1001, u"جدید...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, 1002, u"بازکردن", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, 1002, u"ذخیره...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem3 )
		
		self.m_menuItem14 = wx.MenuItem( self.m_menu1, 1002, u"ذخیره به...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem14 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu1, 1002, u"تنظیمات", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu1, 1002, u"چاپ", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem5 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem6 = wx.MenuItem( self.m_menu1, 107, u"خروج", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem6 )
		
		self.m_menubar1.Append( self.m_menu1, u"بایگانی" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu2, 2001, u"سوابق", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem7 )
		
		self.m_menuItem8 = wx.MenuItem( self.m_menu2, 2005, u"لیست ها", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem8 )
		
		self.m_menuItem9 = wx.MenuItem( self.m_menu2, 3001, u"جزئیات", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem9 )
		
		self.m_menuItem10 = wx.MenuItem( self.m_menu2, 3002, u"مشخصات", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem10 )
		
		self.m_menu2.AppendSeparator()
		
		self.m_menuItem11 = wx.MenuItem( self.m_menu2, 3004, u"جستجو", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem11 )
		
		self.m_menubar1.Append( self.m_menu2, u"مشاهده" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem12 = wx.MenuItem( self.m_menu3, 7001, u"درباره...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem12 )
		
		self.m_menuItem13 = wx.MenuItem( self.m_menu3, 6001, u"توضیحات", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem13 )
		
		self.m_menubar1.Append( self.m_menu3, u"راهنما" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.SetSashSize( 110 )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		
		self.m_panel1 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,500 ), wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_treeCtrl1 = wx.TreeCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer2.Add( self.m_treeCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		self.m_panel2 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,500 ), wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		self.m_splitter1.SplitVertically( self.m_panel1, self.m_panel2, 100 )
		bSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.Bind(wx.EVT_MENU_RANGE,self.OnMenu)
	
	def __del__( self ):
		pass
	
	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 100 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )

	def OnMenu(self,event):
                self.mid = event.GetId()
                #print self.mid
                if self.mid == 107:
                        #q = self.GetParent()
                        #q.Close()
                        self.Close()
                else:
                        a = pro.DoProgram(self.mid)
                        s = a.size() if 'size' in dir(a) else ()
                        win1 = wx.Frame(self,-1)
                        win1.SetSize(s)
                        a.main(win1)
                
                
                
	

