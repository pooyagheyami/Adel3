# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyPanel8
###########################################################################

class MPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 150,260 ), style = wx.TAB_TRAVERSAL )
		
		Vsz = wx.BoxSizer( wx.VERTICAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u" آپارتمان", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn1.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u" ویلائی", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn2.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u" مغازه", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn3.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn3, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn4 = wx.Button( self, wx.ID_ANY, u" زمین", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn4.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn4, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		        
                        
		self.SetSizer( Vsz )
		self.Layout()
		
		# Connect Events
		#self.btn1.Bind( wx.EVT_BUTTON, self.doit )
		#self.btn2.Bind( wx.EVT_BUTTON, self.doit )
		#self.btn3.Bind( wx.EVT_BUTTON, self.doit )
		#self.btn4.Bind( wx.EVT_BUTTON, self.doit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Shwhid(self,btns):
                #print btns
                if '1' not in btns:
                        self.btn1.Hide()
                else:
                        self.btn1.Show()
                if '2' not in btns:
                        self.btn2.Hide()
                else:
                        self.btn2.Show() 
                if '3' not in btns:
                        self.btn3.Hide()
                else:
                        self.btn3.Show() 
                if '4' not in btns:
                        self.btn4.Hide()
                else:
                        self.btn4.Show()
                
	
	
###########################################################################
## Class MyPanel3
###########################################################################

class APanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 150,260 ), style = wx.TAB_TRAVERSAL )
		
		Vsz = wx.BoxSizer( wx.VERTICAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"فروش", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn1.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"رهن", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn2.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"رهن اجاره", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn3.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn3, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn4 = wx.Button( self, wx.ID_ANY, u"برگشت", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn4.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn4, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( Vsz )
		self.Layout()
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.doit )
		self.btn1.Bind( wx.EVT_MOTION, self.doit )
		self.btn2.Bind( wx.EVT_BUTTON, self.doit )
		self.btn3.Bind( wx.EVT_BUTTON, self.doit )
		self.btn4.Bind( wx.EVT_BUTTON, self.doit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def doit( self, event ):
		event.Skip()
	
	
	
