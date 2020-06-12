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
## Class MyPanel3
###########################################################################

class keyPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,150 ), style = wx.TAB_TRAVERSAL )

		self.itxt = ''
		V1 = wx.BoxSizer( wx.VERTICAL )
		
		H1 = wx.BoxSizer( wx.HORIZONTAL )
		keylst1 = [u"ض",u"ص",u"ث",u"ق",u"ف",u"غ",u"ع",u"ه",u"خ",u"ح",u"ج",u"چ"]
		keylst2 = [u"ش",u"س",u"ی",u"ب",u"ل",u"ا",u"ت",u"ن",u"م",u"ک",u"گ"]
		keylst3 = [u"ظ",u"ط",u"ز",u"ر",u"ذ",u"د",u"ئ",u"و",u"پ",u"ژ"]

		self.kbtn1 = []
		i = 0
		self.btab = wx.Button( self, wx.ID_ANY, u"TAB", wx.DefaultPosition, wx.Size( 45,-1 ), wx.BU_EXACTFIT )
		H1.Add( self.btab, 0, wx.EXPAND, 5 )

		for ky in keylst1:
                    self.kbtn1.append( wx.Button( self, wx.ID_ANY, ky, wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT ))
                    H1.Add( self.kbtn1[i], 1, wx.EXPAND, 5 )
                    #self.kbtn1[i].Bind( wx.EVT_BUTTON, self.onkey )
		    i += 1
                    
		
		self.bbck = wx.Button( self, wx.ID_ANY, u"<-", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		H1.Add( self.bbck, 1, wx.EXPAND, 5 )
		
		
		V1.Add( H1, 1, wx.EXPAND, 5 )
		
		H2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bcps = wx.Button( self, wx.ID_ANY, u"Caps Lock", wx.DefaultPosition, wx.Size( 60,-1 ), wx.BU_EXACTFIT )
		H2.Add( self.bcps, 0, wx.EXPAND, 5 )

		for ky in keylst2:
                    self.kbtn1.append( wx.Button( self, wx.ID_ANY, ky, wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT ))
                    H2.Add( self.kbtn1[i], 1, wx.EXPAND, 5 )
                    #self.kbtn1[i].Bind( wx.EVT_BUTTON, self.onkey )
		    i += 1
		
		self.bentr = wx.Button( self, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.Size( 85,-1 ), 0 )
		H2.Add( self.bentr, 1, wx.EXPAND, 5 )
		
		
		V1.Add( H2, 1, wx.EXPAND, 5 )
		
		H3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bshft1 = wx.Button( self, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		H3.Add( self.bshft1, 0, wx.EXPAND, 5 )

		for ky in keylst3:
                    self.kbtn1.append( wx.Button( self, wx.ID_ANY, ky, wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT ))
                    H3.Add( self.kbtn1[i], 1, wx.EXPAND, 5 )
                    #self.kbtn1[i].Bind( wx.EVT_BUTTON, self.onkey )
		    i += 1
		
		self.bshft2 = wx.Button( self, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		H3.Add( self.bshft2, 1, wx.EXPAND, 5 )
		
		
		V1.Add( H3, 1, wx.EXPAND, 5 )
		
		H4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bctrl1 = wx.Button( self, wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.Size( 60,-1 ), wx.BU_EXACTFIT )
		H4.Add( self.bctrl1, 0, wx.EXPAND, 5 )
		
		self.balt1 = wx.Button( self, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		H4.Add( self.balt1, 0, wx.EXPAND, 5 )
		
		self.bspce = wx.Button( self, wx.ID_ANY, u"Space", wx.DefaultPosition, wx.Size( 275,-1 ), 0 )
		H4.Add( self.bspce, 1, wx.EXPAND, 5 )
		
		self.balt2 = wx.Button( self, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		H4.Add( self.balt2, 0, wx.EXPAND, 5 )
		
		self.bcomd = wx.Button( self, wx.ID_ANY, u"Win", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		H4.Add( self.bcomd, 0, wx.EXPAND, 5 )
		
		self.bctrl2 = wx.Button( self, wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		H4.Add( self.bctrl2, 0, wx.EXPAND, 5 )
		
		
		V1.Add( H4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( V1 )
		self.Layout()
		
		# Connect Events
		#self.btab.Bind( wx.EVT_BUTTON, self.ontab )
		#self.bbck.Bind( wx.EVT_BUTTON, self.onbak )
		self.bcps.Bind( wx.EVT_BUTTON, self.oncaps )
		#self.bentr.Bind( wx.EVT_BUTTON, self.onenter )
		self.bshft1.Bind( wx.EVT_BUTTON, self.onshftl )
		self.bshft2.Bind( wx.EVT_BUTTON, self.onshftr )
		self.bctrl1.Bind( wx.EVT_BUTTON, self.lctrl )
		self.balt1.Bind( wx.EVT_BUTTON, self.lalt )
		#self.bspce.Bind( wx.EVT_BUTTON, self.onspce )
		self.balt2.Bind( wx.EVT_BUTTON, self.ralt )
		self.bcomd.Bind( wx.EVT_BUTTON, self.oncom )
		self.bctrl2.Bind( wx.EVT_BUTTON, self.rctrl )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ontab( self, event ):
		print event
	
	def onbak( self, event ):
		print event
	
	def oncaps( self, event ):
		print event
	
	def onenter( self, event ):
		print event
	
	def onshftl( self, event ):
		print event
	
	def onshftr( self, event ):
		print event
	
	def lctrl( self, event ):
		print event
	
	def lalt( self, event ):
		print event
	
	def onspce( self, event ):
		print event
	
	def ralt( self, event ):
		print event
	
	def oncom( self, event ):
		print event
	
	def rctrl( self, event ):
		print event
	def onkey( self, event ):
		return event.GetEventObject().GetLabel()
	
                
                
	

