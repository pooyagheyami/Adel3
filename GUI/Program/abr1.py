# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import Backres as BR
#from buyit import *

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 100,250 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		#self.m_button1 = wx.Button( self, wx.ID_ANY, u"بایگانی...", wx.DefaultPosition, wx.DefaultSize, 0 )
		#bSizer4.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"پشتیبانی...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"بازیابی...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"بستن", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		# Connect Events
		#self.m_button1.Bind( wx.EVT_BUTTON, self.onarchive )
		self.m_button2.Bind( wx.EVT_BUTTON, self.onbackup )
		self.m_button3.Bind( wx.EVT_BUTTON, self.onrestore )
		self.m_button4.Bind( wx.EVT_BUTTON, self.onclose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onarchive( self, event ):
                pass
		#self.a = Archiv.MyFrame1(self)
		#self.a.SetSize((700,500))
		#self.a.Show()
	
	def onbackup( self, event ):
		#txt = thistxt('disit.txt')
		#btn = u'تائيد'
		self.b = wx.Frame(self,style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)
		self.panel = BR.MyPanel1(self.b)
		self.panel.SetLayoutDirection(2)
		self.b.SetSize((510,220))
		self.b.SetTitle(u"پشتيباني اطلاعات")
		self.b.Show()
                
		
	
	def onrestore( self, event ):
                #txt = thistxt('disit.txt')
		#btn = u'تائيد'
		
		self.r = wx.Frame(self,style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)
		self.panel = BR.MyPanel2(self.r)
		self.panel.SetLayoutDirection(2)
		self.r.SetSize((510,220))
		self.r.SetTitle(u"بازيابي اطلاعات")
		self.r.Show()
	
	def onclose( self, event ):
		q = self.GetParent()
		q.Close()

	

