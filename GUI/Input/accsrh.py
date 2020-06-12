# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from Config.Init import *
import Utility.Adaad2 as adad

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent , data ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 252,436 ), style = wx.TAB_TRAVERSAL )

		self.SetFont( wx.Font( 11, 74, 90, 92, False, FONT_TYPE ) )
		self.inum = adad.Adaad(1,'')
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.VERTICAL )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"لیست مشتریان", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Hsz1, 0, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.VERTICAL )
		
		self.DVLC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES  )
		self.Col1 = self.DVLC1.AppendTextColumn( u"کد" )
		self.Col2 = self.DVLC1.AppendTextColumn( u"نام مشتری" )
		self.Col3 = self.DVLC1.AppendTextColumn( u"تلفن " )
		Hsz2.Add( self.DVLC1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )
		
		Hsz3 = wx.BoxSizer( wx.VERTICAL )
		
		self.btn = wx.Button( self, wx.ID_ANY, u"انتخاب", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Hsz3, 0, wx.EXPAND, 5 )

		#for itemvalues in data:
                #    self.DVLC1.AppendItem(itemvalues)
                for d in data:
                        d = (self.inum.e2f2(d[0]),d[1],self.inum.e2f2(d[2]))
                        self.DVLC1.AppendItem(d)

                self.idata = data

                for c in  self.DVLC1.Columns:
                        c.Sortable = True
                        c.Reorderable = True

		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.getacc, id = wx.ID_ANY )
		self.btn.Bind( wx.EVT_BUTTON, self.selct )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def getacc( self, event ):
		a= self.DVLC1.GetSelectedRow()
                self.retdata()
		q = self.GetParent()
                q.Close()
	
	def selct( self, event ):
		a= self.DVLC1.GetSelectedRow()
                self.retdata()
		q = self.GetParent()
                q.Close()
                
                        
        def retdata(self):
                a= self.DVLC1.GetSelectedRow()
                data = []
                
                if a == -1:
                        data.append(' ')
                else:
                        data.append((unicode(self.DVLC1.GetValue(a,0)),
                                     unicode(self.DVLC1.GetValue(a,1)),
                                     unicode(self.DVLC1.GetValue(a,2))))
                return data        
	

