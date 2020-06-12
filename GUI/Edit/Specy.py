# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
import wx.grid
import Database.MDataGet as DG

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent , txts , ccod ,stit):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 273,256 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		self.ccod = ccod
		#print self.ccod
		#print stit
		self.iData = DG.GetData(u'',u'')
		self.itits = self.iData.gTitel(stit)
		self.ispec = self.iData.gSpcy(self.ccod)
		self.row = len(self.itits)
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, txts[0], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, txts[1], wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz1, 0, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER )
		
		# Grid
		self.grid1.CreateGrid( self.row, 2 )
		self.grid1.EnableEditing( True )
		self.grid1.EnableGridLines( True )
		self.grid1.EnableDragGridSize( False )
		self.grid1.SetMargins( 0, 0 )
		
		# Columns
		self.grid1.SetColSize( 0, 99 )
		self.grid1.SetColSize( 1, 134 )
		self.grid1.EnableDragColMove( False )
		self.grid1.EnableDragColSize( True )
		self.grid1.SetColLabelSize( 30 )
		self.grid1.SetColLabelValue( 0, u"عنوان" )
		self.grid1.SetColLabelValue( 1, u"مشخصه" )
		self.grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grid1.EnableDragRowSize( True )
		self.grid1.SetRowLabelSize( 19 )
		self.grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		Hsz2.Add( self.grid1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		Vsz1.Add( Hsz2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"ثبت شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn2, 0, wx.ALL, 5 )
		
		
		Vsz1.Add( Hsz3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		#self.iData = DG.GetData(u'',u'')
		#self.itits = self.iData.gTitel(stit)
		#self.ispec = self.iData.gSpcy(self.ccod)
		self.lodtit()
		
		self.SetSizer( Vsz1 )
		self.Layout()

		self.svit = False
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn2.Bind( wx.EVT_BUTTON, self.aplyit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cancl( self, event ):
                self.svit = False
		q = self.GetParent()
                q.Close()
	
	def aplyit( self, event ):
                self.svit = True
                #self.sData = DG.SetData(u'',u'')
                #idata = self.gettit()
                #print idata
                #self.savtit(idata,self.sData)
                                       
		q = self.GetParent()
                q.Close()

	def lodtit(self):
                j = 0
                for t in self.itits:
                        self.grid1.SetCellValue(j,0,t[0])
                        
                        for s in self.ispec:
                                if s[1] in t:
                                        self.grid1.SetCellValue(j,1,s[0])
                        j = j + 1
                        
        def gettit(self):
                self.spcy = []
                for i in range(len(self.itits)):
                        ispc = self.grid1.GetCellValue(i,1)
                        if ispc != '':
                                self.spcy.append((self.ccod,self.itits[i][1],ispc))
                                #print self.itits[i][1]
                #print self.spcy
                return self.spcy
        def RetRev(self):
                return self.svit
        
