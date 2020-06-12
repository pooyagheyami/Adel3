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
from Config.Init import *
import Utility.Adaad2 as adad
from wx import MessageBox,OK,ICON_WARNING,ICON_INFORMATION

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 514,171 ), style = wx.TAB_TRAVERSAL )

		self.iMolk = DG.GetData(u'',u'')
		self.jMolk = DG.SetData(u'',u'')
		self.inumr = adad.Adaad(1,'')

		self.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )

		if self.iMolk.gCmpny() != []:
                    data = self.iMolk.gCmpny()
                    icomp = data[0][1]
                    rata = self.iMolk.gReven()
                    irev = rata[0][1]
                    self.nwb = False
                else:
                    icomp = ''
                    irev = ''
                    self.nwb = True
                    
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnl1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fld2 = wx.TextCtrl( self.pnl1, wx.ID_ANY, irev, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		Hsz1.Add( self.fld2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt2 = wx.StaticText( self.pnl1, wx.ID_ANY, u"نام عملکرد", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )
		Hsz1.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn1 = wx.Button( self.pnl1, wx.ID_ANY, u"....مشخصات بنگاه ", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld1 = wx.TextCtrl( self.pnl1, wx.ID_ANY, icomp, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		Hsz1.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt1 = wx.StaticText( self.pnl1, wx.ID_ANY, u"نام بنگاه", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.pnl1.SetSizer( Hsz1 )
		self.pnl1.Layout()
		Hsz1.Fit( self.pnl1 )
		Vsz1.Add( self.pnl1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn2 = wx.Button( self.pnl2, wx.ID_ANY, u"مناطق", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz21.Add( self.btn2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn3 = wx.Button( self.pnl2, wx.ID_ANY, u"نوع ملک", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz21.Add( self.btn3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn4 = wx.Button( self.pnl2, wx.ID_ANY, u"نوع درخواست", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz21.Add( self.btn4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz2.Add( Hsz21, 1, wx.EXPAND, 5 )
		
		
		self.pnl2.SetSizer( Vsz2 )
		self.pnl2.Layout()
		Vsz2.Fit( self.pnl2 )
		Vsz1.Add( self.pnl2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.pnl3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn5 = wx.Button( self.pnl3, wx.ID_ANY, u"تعریف شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn5, 0, wx.ALL, 5 )
		
		self.btn6 = wx.Button( self.pnl3, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn6, 0, wx.ALL, 5 )
		
		
		self.pnl3.SetSizer( Hsz3 )
		self.pnl3.Layout()
		Hsz3.Fit( self.pnl3 )
		Vsz1.Add( self.pnl3, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.bspc )
		self.btn2.Bind( wx.EVT_BUTTON, self.inarea )
		self.btn3.Bind( wx.EVT_BUTTON, self.inmktyp )
		self.btn4.Bind( wx.EVT_BUTTON, self.inres )
		self.btn5.Bind( wx.EVT_BUTTON, self.defin )
		self.btn6.Bind( wx.EVT_BUTTON, self.cancl )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def bspc( self, event ):
		name = self.fld1.GetValue()
                txt = [u'نام بنگاه',name]
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel3(iwin,txt,u'901-511',u'111')
		iwin.SetSize((261,310))
		iwin.ShowModal()
		if pnl.RetRev():
                    self.ispec = self.iMolk.gSpcy(u'901-511')
                    mdata = pnl.gettit()
                    self.savtit(mdata,self.jMolk)

		iwin.Destroy()
	def savtit(self,data,iSet):
                #print data
                #print self.ispec
                for i in range(len(data)):
                        for j in range(len(self.ispec)):
                                if data[i][1] in self.ispec[j]:
                                        idata = (data[i][2],)
                                        iSet.Specup("Spcfy = ? where Spc = '%s' and tit = '%s' "%(self.iacc,self.ispec[j][2]),idata)
                                        break
                        else:
                                iSet.Specin('Spc , tit, Spcfy ',data[i])
	
	def inarea( self, event ):
		titr = event.GetEventObject().GetLabel()
                data = self.iMolk.gMntgh()
                if data == []:
                        lcod = '0'
                else:
                        lcod = unicode(int(data[-1][0])+1)
                #print lcod,data
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel2(iwin,titr, data)
		iwin.SetSize((137,310))
		iwin.ShowModal()

		if pnl.aply :
                    data = pnl.savit()
                    data1 = [lcod,data[-1]]
                    self.jMolk.Inmntg(' Area , Aname ',data1)
                    
                self.Refresh()
		self.Layout()  
		iwin.Destroy()
	
	def inmktyp( self, event ):
		titr = event.GetEventObject().GetLabel()
                data = self.iMolk.gMltype()
                if data == []:
                        lcod = '0'
                else:
                        lcod = unicode(int(data[-1][0])+1)
                #print lcod
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel2(iwin,titr, data)
		iwin.SetSize((137,310))
		iwin.ShowModal()
		if pnl.aply :
                    data = pnl.savit()
                    data1 = [lcod,data[-1]]
                    self.jMolk.Inmtyp(' Mtype , Type ',data1)
                    
                self.Refresh()
		self.Layout()  

		iwin.Destroy()
	
	def inres( self, event ):
                data = self.iMolk.ShwRes2()
		titr = event.GetEventObject().GetLabel()
		if data == []:
                        lcod = '0'
                else:
                        lcod = unicode(int(data[-1][0])+1)
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel2(iwin,titr,data)
		
		iwin.SetSize((137,310))
		iwin.ShowModal()

		if pnl.aply:
                    data = pnl.savit()
                    data1 = [lcod,data[-1]]
                    #print data
                    self.jMolk.Inmres(' Res , Resname ',data1)

		self.Refresh()
		self.Layout()  

		iwin.Destroy()

	def chkin( self ):
                if self.fld1.GetValue() == u'':
                        MessageBox(u'نام بنگاه را مشخص کنيد',u'خطا',OK | ICON_WARNING)
                        return 0
                if self.fld2.GetValue() == u'':
                        MessageBox(u'عملکرد بنگاه را مشخص کنيد',u'خطا',OK | ICON_WARNING)
                        return 0
                if not self.nwb:
                        MessageBox(u'بنگاه قبلا ثبت شده',u'خطا',OK | ICON_WARNING)
                        return 0
                return 1
                        
	def defin( self, event ):
		if self.chkin():
                    f1 = self.fld1.GetValue()
                    f2 = self.fld2.GetValue()
                    d =  JalaliDatetime().now()
                    s = str(d.year)+str(d.month)+str(d.day)+str(d.hour)+str(d.minute)+str(d.second)
                    send = [' id , name , Rev , Dir , Spc ',' Rev, Reven , fdate , ldate' ]
                    data = [[u'1',f1,'1A','tmp'+s,u'901-511'],['1A',self.inumr.e2f2(f2),NOW[:4],NOW[:4].replace(u'\u06f7',u'\u06f8')]]
                    self.jMolk.InABRc(send,data)
                    MessageBox(u'بنگاه با موفقيت ثبت شد',u'اعلان',OK | ICON_INFORMATION)
                    q = self.GetParent()
                    q.Close()
	
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
	

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent , titr, data ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 137,310 ), style = wx.TAB_TRAVERSAL )

		self.data = data
		self.row = len(data)+1
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		self.titr1 = wx.StaticText( self, wx.ID_ANY, u"تیتر", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr1.Wrap( -1 )
		Vsz2.Add( self.titr1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Vsz2, 0, wx.EXPAND, 5 )
		
		Vsz3 = wx.BoxSizer( wx.VERTICAL )
		
		self.grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grid1.CreateGrid( self.row, 1 )
		self.grid1.EnableEditing( True )
		self.grid1.EnableGridLines( True )
		self.grid1.EnableDragGridSize( False )
		self.grid1.SetMargins( 0, 0 )
		
		# Columns
		self.grid1.EnableDragColMove( False )
		self.grid1.EnableDragColSize( True )
		self.grid1.SetColLabelSize( 0 )
		self.grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grid1.EnableDragRowSize( True )
		self.grid1.SetRowLabelSize( 19 )
		self.grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grid1.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		Vsz3.Add( self.grid1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		Vsz1.Add( Vsz3, 1, wx.EXPAND, 5 )
		
		Vsz4 = wx.BoxSizer( wx.VERTICAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"اضافه شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Vsz4, 0, wx.EXPAND, 5 )
		self.aply = False
		
		self.SetSizer( Vsz1 )
		self.Layout()

		self.loadit()
		
		# Connect Events
		self.grid1.Bind( wx.grid.EVT_GRID_EDITOR_CREATED, self.doeditor )
		self.grid1.Bind( wx.EVT_KEY_DOWN, self.dokey )
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.cancl )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def doeditor( self, event ):
		#print event.GetEventObject()
		pass
	
	def dokey( self, event ):
		#print event.GetEventObject()
		pass
	
	def addit( self, event ):
                self.aply = True
		self.savit()
		q = self.GetParent()
                q.Close()
	
	def cancl( self, event ):
                self.aply = False
		q = self.GetParent()
                q.Close()
	def loadit( self ):
                j = 0
                for d in self.data:
                    self.grid1.SetCellValue(j,0,d[1])
                    j = j + 1
        def savit( self ):
                d = []
                for r in range(self.row):
                    d.append( self.grid1.GetCellValue(r,0) )
                return d    

###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):
	
	def __init__( self, parent , txts , ccod ,stit):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 251,300 ), style = wx.TAB_TRAVERSAL )

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
		
		self.grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grid1.CreateGrid( self.row, 2 )
		self.grid1.EnableEditing( True )
		self.grid1.EnableGridLines( True )
		self.grid1.EnableDragGridSize( False )
		self.grid1.SetMargins( 0, 0 )
		
		# Columns
		self.grid1.SetColSize( 0, 74 )
		self.grid1.SetColSize( 1, 155 )
		self.grid1.EnableDragColMove( False )
		self.grid1.EnableDragColSize( True )
		self.grid1.SetColLabelSize( 30 )
		self.grid1.SetColLabelValue( 0, u"عنوان " )
		self.grid1.SetColLabelValue( 1, u"مشخصه" )
		self.grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grid1.EnableDragRowSize( True )
		self.grid1.SetRowLabelSize( 0 )
		self.grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		Hsz2.Add( self.grid1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )
		
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"ثبت شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"برگشت", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lodtit()
		self.svit = False
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.aplyit )
		self.btn2.Bind( wx.EVT_BUTTON, self.bakit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def aplyit( self, event ):
		self.svit = True
                                                      
		q = self.GetParent()
                q.Close()
	
	def bakit( self, event ):
		self.svit = False
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


###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):
	
	def __init__( self, parent , titr , data ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 225,300 ), style = wx.TAB_TRAVERSAL )

		self.row = len(data)+1
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		self.titr1 = wx.StaticText( self, wx.ID_ANY, titr, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr1.Wrap( -1 )
		Vsz2.Add( self.titr1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Vsz2, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		Vsz3 = wx.BoxSizer( wx.VERTICAL )
		
		self.grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grid1.CreateGrid( self.row, 2 )
		self.grid1.EnableEditing( True )
		self.grid1.EnableGridLines( True )
		self.grid1.EnableDragGridSize( False )
		self.grid1.SetMargins( 0, 0 )
		
		# Columns
		self.grid1.SetColSize( 0, 122 )
		self.grid1.SetColSize( 1, 65 )
		self.grid1.EnableDragColMove( False )
		self.grid1.EnableDragColSize( True )
		self.grid1.SetColLabelSize( 30 )
		self.grid1.SetColLabelValue( 0, u"عنوان" )
		self.grid1.SetColLabelValue( 1, u"کد" )
		self.grid1.SetColLabelValue( 2, wx.EmptyString )
		self.grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grid1.EnableDragRowSize( True )
		self.grid1.SetRowLabelSize( 0 )
		self.grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		Vsz3.Add( self.grid1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		Vsz1.Add( Vsz3, 1, wx.EXPAND, 5 )
		
		Vsz4 = wx.BoxSizer( wx.VERTICAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"اضافه شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Vsz4, 0, wx.EXPAND, 5 )
		i = 0
		for d in data:
                    self.grid1.SetCellValue(i,0,d[0])
                    self.grid1.SetCellValue(i,1,d[1])
                    i = i + 1
		self.aply = False
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.cancl )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addit( self, event ):
                self.aply = True
		self.loadt()
		q = self.GetParent()
                q.Close()
	
	def cancl( self, event ):
                self.aply = False
		q = self.GetParent()
                q.Close()
                
	def loadt( self ):
                data = []
                for r in range(self.row):
                    data.append( (self.grid1.GetCellValue(r,0),
                                  self.grid1.GetCellValue(r,1)) )
                return data    
                

