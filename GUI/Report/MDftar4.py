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
import Database.MDataGet as DG
import Utility.Adaad2 as adad
import RMolk63 as RM

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 860,503 ), style = wx.TAB_TRAVERSAL )

		self.iMolk = DG.GetData(u'',u'')
		self.inum = adad.Adaad(1,'')

		self.SetFont( wx.Font( FONT_SIZE, 70, 90, 92, False, FONT_TYPE ) )
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Vsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.srcbtn = wx.Button( self, wx.ID_ANY, u"جستجو", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz2.Add( self.srcbtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"دفتر املاک", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.txt1.Wrap( -1 )
		self.txt1.SetFont( wx.Font( 19, 70, 90, 90, False, wx.EmptyString ) )
		
		Vsz2.Add( self.txt1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.clsbtn = wx.Button( self, wx.ID_ANY, u"بستن", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz2.Add( self.clsbtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Vsz2, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		Vsz3 = wx.BoxSizer( wx.VERTICAL )
		
		chs1Choices = [ u"فروش", u"رهن", u"رهن اجاره" ]
		self.chs1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 95,-1 ), chs1Choices, 0 )
		self.chs1.SetSelection( 0 )
		Vsz3.Add( self.chs1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		#chs2Choices = [ u"آپارتمان", u"ویلائی", u"مغازه", u"زمین" ]
		chs2Choices = []
		imtype = self.iMolk.gMltype()
		for t in imtype:
                    chs2Choices.append( t[1] )
                    
		self.chs2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 95,-1 ), chs2Choices, 0 )
		self.chs2.SetSelection( 0 )
		Vsz3.Add( self.chs2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Vsz3, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.pnl1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER )
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		Vsz30 = wx.BoxSizer( wx.VERTICAL )
		
		self.fld9 = wx.TextCtrl( self.pnl1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 92,-1 ), wx.TE_RIGHT )
		self.fld9.SetLayoutDirection(2)
		Vsz30.Add( self.fld9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld8 = wx.TextCtrl( self.pnl1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 92,-1 ), wx.TE_RIGHT )
		self.fld8.SetLayoutDirection(2)
		Vsz30.Add( self.fld8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Hsz3.Add( Vsz30, 0, wx.EXPAND, 5 )
		
		Vsz31 = wx.BoxSizer( wx.VERTICAL )
		
		self.txt9 = wx.StaticText( self.pnl1, wx.ID_ANY, u"مبلغ کل از", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.txt9.Wrap( -1 )
		Vsz31.Add( self.txt9, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.txt8 = wx.StaticText( self.pnl1, wx.ID_ANY, u"تا", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.txt8.Wrap( -1 )
		Vsz31.Add( self.txt8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Hsz3.Add( Vsz31, 0, wx.EXPAND, 5 )
		
		Vsz32 = wx.BoxSizer( wx.VERTICAL )
		
		self.fld7 = wx.TextCtrl( self.pnl1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 92,-1 ), wx.TE_RIGHT )
		self.fld7.SetLayoutDirection(2)
		Vsz32.Add( self.fld7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld6 = wx.TextCtrl( self.pnl1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 92,-1 ), wx.TE_RIGHT )
		self.fld6.SetLayoutDirection(2)
		Vsz32.Add( self.fld6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Hsz3.Add( Vsz32, 0, wx.EXPAND, 5 )
		
		Vsz33 = wx.BoxSizer( wx.VERTICAL )
		
		self.txt7 = wx.StaticText( self.pnl1, wx.ID_ANY, u"متري از", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.txt7.Wrap( -1 )
		Vsz33.Add( self.txt7, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.txt6 = wx.StaticText( self.pnl1, wx.ID_ANY, u"تا", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.txt6.Wrap( -1 )
		Vsz33.Add( self.txt6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Hsz3.Add( Vsz33, 0, wx.EXPAND, 5 )
		
		Vsz34 = wx.BoxSizer( wx.VERTICAL )
		
		self.fld5 = wx.TextCtrl( self.pnl1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_RIGHT )
		self.fld5.SetLayoutDirection(2)
		Vsz34.Add( self.fld5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.fld4 = wx.TextCtrl( self.pnl1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_RIGHT )
		self.fld4.SetLayoutDirection(2)
		Vsz34.Add( self.fld4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Hsz3.Add( Vsz34, 0, wx.EXPAND, 5 )
		
		Vsz35 = wx.BoxSizer( wx.VERTICAL )
		
		self.txt5 = wx.StaticText( self.pnl1, wx.ID_ANY, u"متراژ از", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.txt5.Wrap( -1 )
		Vsz35.Add( self.txt5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.txt4 = wx.StaticText( self.pnl1, wx.ID_ANY, u"تا", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.txt4.Wrap( -1 )
		Vsz35.Add( self.txt4, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		Hsz3.Add( Vsz35, 0, wx.EXPAND, 5 )
		
		Vsz36 = wx.BoxSizer( wx.VERTICAL )
		
		self.fld3 = wx.TextCtrl( self.pnl1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		Vsz36.Add( self.fld3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.fld2 = wx.TextCtrl( self.pnl1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ),  wx.TE_RIGHT )
		self.fld2.SetLayoutDirection(2)
		Vsz36.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Hsz3.Add( Vsz36, 1, wx.EXPAND, 5 )
		
		Vsz37 = wx.BoxSizer( wx.VERTICAL )
		
		self.txt3 = wx.StaticText( self.pnl1, wx.ID_ANY, u"تعداد خواب", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt3.Wrap( -1 )
		Vsz37.Add( self.txt3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.txt2 = wx.StaticText( self.pnl1, wx.ID_ANY, u"قدمت", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )
		Vsz37.Add( self.txt2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		Hsz3.Add( Vsz37, 1, wx.EXPAND, 5 )
		
		
		Hsz3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		Box1Choices = [ u"همه" ]
		imantgh = self.iMolk.gMntgh()
		for m in imantgh:
                    Box1Choices.append( m[1] )
                    
		self.Box1 = wx.ComboBox( self.pnl1, wx.ID_ANY, u"همه", wx.DefaultPosition, wx.Size( 90,-1 ), Box1Choices, 0 )
		self.Box1.SetSelection( 0 )
		Hsz3.Add( self.Box1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt1 = wx.StaticText( self.pnl1, wx.ID_ANY, u"نام منطقه", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		Hsz3.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.pnl1.SetSizer( Hsz3 )
		self.pnl1.Layout()
		Hsz3.Fit( self.pnl1 )
		Vsz1.Add( self.pnl1, 0, wx.EXPAND |wx.ALL, 5 )
		
		Vsz4 = wx.BoxSizer( wx.VERTICAL )
		
		self.DVLC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES|wx.STATIC_BORDER )
		self.Column1 = self.DVLC1.AppendTextColumn( u"قيمت",width = 92,align=wx.ALIGN_LEFT )
		self.Column2 = self.DVLC1.AppendTextColumn( u"متري",width = 92,align=wx.ALIGN_LEFT )
		self.Column3 = self.DVLC1.AppendTextColumn( u"تعداد خواب" ,width = 72,align=wx.ALIGN_LEFT)
		self.Column4 = self.DVLC1.AppendTextColumn( u"قدمت" ,width = 42,align=wx.ALIGN_LEFT)
		self.Column5 = self.DVLC1.AppendTextColumn( u"مفید" ,width = 52,align=wx.ALIGN_LEFT)
		self.Column6 = self.DVLC1.AppendTextColumn( u"متراژ" ,width = 52,align=wx.ALIGN_LEFT)
		self.Column7 = self.DVLC1.AppendTextColumn( u"آدرس",width = 220,align=wx.ALIGN_RIGHT )
		self.Column8 = self.DVLC1.AppendTextColumn( u"منطقه",width = 70,align=wx.ALIGN_RIGHT )
		self.Column9 = self.DVLC1.AppendTextColumn( u"نام ملک",width = 80,align=wx.ALIGN_RIGHT )
		self.Column10 = self.DVLC1.AppendTextColumn( u"کد ملک" ,width = 60)
		Vsz4.Add( self.DVLC1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		Vsz1.Add( Vsz4, 1, wx.EXPAND, 5 )

		self.sql1 = u" where Molks.Res = 1 "
		self.sql2 = u" and Molks.Mtype = 0 "
		
		self.loadata(  )
		for c in  self.DVLC1.Columns:
                        c.Sortable = True
                        c.Reorderable = True
		self.Column1.Sortable = False
		self.Column2.Sortable = False
		#self.Column3.Sortable = False
		#self.Column4.Sortable = False

		
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.srcbtn.Bind( wx.EVT_BUTTON, self.srchit )
		self.clsbtn.Bind( wx.EVT_BUTTON, self.retit )
		self.chs1.Bind( wx.EVT_CHOICE, self.resit )
		self.chs2.Bind( wx.EVT_CHOICE, self.typit )
		self.fld9.Bind( wx.EVT_TEXT, self.mbl1 )
		self.fld8.Bind( wx.EVT_TEXT, self.mbl2 )
		self.fld7.Bind( wx.EVT_TEXT, self.mbl1 )
		self.fld6.Bind( wx.EVT_TEXT, self.mbl2 )
		self.fld5.Bind( wx.EVT_TEXT, self.mtr1 )
		self.fld4.Bind( wx.EVT_TEXT, self.mtr2 )
		self.fld3.Bind( wx.EVT_TEXT, self.inroom )
		self.fld2.Bind( wx.EVT_TEXT, self.inbuld )
		self.Box1.Bind( wx.EVT_COMBOBOX, self.areas )
		self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_REORDERED, self.ordr, id = wx.ID_ANY )
		self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_SORTED, self.Sort, id = wx.ID_ANY )
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.Rmolk, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def loadata( self  ):
                data = self.iMolk.Amlak4(self.sql1 + self.sql2)
                self.lstrow = []
		for d in data:
                        if d[2] == u'0':
                                DD = u'سه خوابه'
                        if d[2] == u'1':
                                DD = u'دو خوابه'
                        if d[2] == u'2':
                                DD = u'يک خوابه'
                        d = (self.inum.Digigrop(d[0],','),self.inum.e2f(d[1])
                             ,DD,self.inum.e2f(d[3]),self.inum.e2f(d[4]),self.inum.e2f(d[5])
                             ,d[6],d[7],d[8],self.inum.e2f(d[9]) )
                        self.DVLC1.AppendItem(d)
                        self.lstrow.append( self.inum.f2e(d[9]) )      
                    

	def srchit( self, event ):
		sql = u''
		data = self.GetData()
		
		if data[0] != 0:
                    sql = sql + " and Molks.Area = %s "%(data[0]-1)
                if data[1] != u'':
                    sql = sql + " and Molks.M3 <=  '%s' "%data[1]
                if data[2] != u'':
                    sql = sql + "  and substr(MSpcify.Spcfy,1,1) = '%s' "%self.groom(data[2])
                if data[3] != u'' and data[4] != u'':
                    sql = sql + " and Molks.M1 >= %s and Molks.M1 < %s "%(data[4],data[3])    
                #if data[4] != u'':
                #    sql = sql + " and Molks.M2 = '%s'  "%self.inum.e2f2(data[4])
                if data[5] != u'' and data[6] != '':
                    sql = sql + " and Molks.Amunt1 >= %s and Molks.Amunt1 < %s  "%(data[6],data[5])
                if data[7] != u'' and data[8] != '':
                    sql = sql + " and Molks.Amunt2 >= %s and Molks.Amunt2 < %s  "%(data[8],data[7])
                   
                newdata = self.iMolk.Amlak4(self.sql1+self.sql2+sql)
                #newdata = self.iMolk.Amlak22(sql)   
                self.DVLC1.DeleteAllItems()
		self.DVLC1.Refresh()
		self.lstrow = []
		for d in newdata:
                        
                        if d[2] == u'0':
                                DD = u'سه خوابه'
                        elif d[2] == u'1':
                                DD = u'دو خوابه'
                        elif d[2] == u'2':
                                DD = u'يک خوابه'
                        else:
                                DD = u'مغازه زمين'
                        d = (self.inum.Digigrop(d[0],','),self.inum.e2f(d[1])
                             ,DD,self.inum.e2f(d[3]),self.inum.e2f(d[4]),self.inum.e2f(d[5])
                             ,d[6],d[7],d[8],self.inum.e2f(d[9]) )
                        self.DVLC1.AppendItem(d)
                        self.lstrow.append( self.inum.f2e(d[9]) )  
                self.DVLC1.Refresh()    
	
	def retit( self, event ):
		q = self.GetParent()
                q.Close()
	def GetData( self ):
                f1 = self.Box1.GetSelection()
                f2 = self.fld2.GetValue()
                f3 = self.fld3.GetValue()
                f4 = self.fld4.GetValue()
                f5 = self.fld5.GetValue()
                f6 = self.fld6.GetValue()
                f7 = self.fld7.GetValue()
                f8 = self.fld8.GetValue()
                f9 = self.fld9.GetValue()
                
                return [f1,f2,f3,f4,f5,f6,f7,f8,f9]
	def resit( self, event ):
		ires = self.chs1.GetSelection()+1
		#print ires
		if self.chs1.GetSelection() == 1:
                        self.sql1 = u" where Molks.Res = %s "%ires
                        self.relst(2)
                        self.Column1.SetTitle(u"اجاره")
                        self.Column2.SetTitle(u"رهن کامل")
                        self.txt7.SetLabel(u"مبلغ رهن از")
                        self.txt9.SetLabel(u"اجاره از")
                        
                elif self.chs1.GetSelection() == 2:
                        self.sql1 = u" where Molks.Res = %s "%ires
                        self.relst(3)
                        self.Column1.SetTitle(u"مبلغ اجاره")
                        self.Column2.SetTitle(u"مبلغ پيش")
                        self.txt7.SetLabel(u"مبلغ رهن از")
                        self.txt9.SetLabel(u"اجاره از")
                        
                else:
                        self.Column1.SetTitle(u"قیمت")
                        self.Column2.SetTitle(u"متري")
                        self.txt7.SetLabel(u"مبلغ اجاره از")
                        self.txt9.SetLabel(u"مبلغ کل از")
                        self.sql1 = u" where Molks.Res = %s "%ires
                        self.relst(1)
                self.Refresh()
                self.Layout()        
	
	def typit( self, event ):
		if self.chs2.GetSelection() >= 0:
                        imtyp = self.chs2.GetSelection()
                        self.sql2 = u" and Molks.Mtype = %s "%imtyp
                                        
                self.relst(self.chs1.GetSelection()+1)
        def newd( self , d , sql ):
                if d == 1:
                        nwdata = self.iMolk.Amlak4(sql)
                if d == 2:
                        nwdata = self.iMolk.Amlak4(sql)
                if d == 3:
                        nwdata = self.iMolk.Amlak4(sql)
                return nwdata            
	def relst( self , D ):
                #print self.sql1,self.sql2
                sql = self.sql1 + self.sql2
                nwdata = self.newd(D,sql)
                self.DVLC1.DeleteAllItems()
		self.DVLC1.Refresh()
		self.lstrow = []
                for d in nwdata:
                        
                        if d[2] == u'0':
                                DD = u'سه خوابه'
                        elif d[2] == u'1':
                                DD = u'دو خوابه'
                        elif d[2] == u'2':
                                DD = u'يک خوابه'
                        else:
                                DD = u'مغازه'
                        d = (self.inum.Digigrop(d[0],','),self.inum.e2f(d[1])
                             ,DD,self.inum.e2f(d[3]),self.inum.e2f(d[4]),self.inum.e2f(d[5])
                             ,d[6],d[7],d[8],self.inum.e2f(d[9]) )
                        self.DVLC1.AppendItem(d)
                        self.lstrow.append( self.inum.f2e(d[9]) )
                        
                self.DVLC1.Refresh()
                self.Refresh()
                self.Layout()
	def mbl1( self, event ):
		event.Skip()
	
	def mbl2( self, event ):
		event.Skip()
	
	
	
	def mtr1( self, event ):
		event.Skip()
	
	def mtr2( self, event ):
		event.Skip()
	
	def inroom( self, event ):
		iroom = event.GetEventObject().GetValue()
		nroom = [u'3',u'2',u'1']
		troom = [u'سه خوابه',u'دو خوابه',u'يک خوابه']
		if iroom in nroom:
                    self.fld3.SetValue(troom[nroom.index(iroom)])
        def groom( self, txt):
                troom = [u'سه خوابه',u'دو خوابه',u'يک خوابه']
                nroom = [u'0',u'1',u'2']
                return  nroom[troom.index(txt)]

	
	def inbuld( self, event ):
		event.Skip()
	
	def areas( self, event ):
		event.Skip()
	
	def ordr( self, event ):
		event.Skip()
	
	def Sort( self, event ):
		event.Skip()
	
        def Rmolk( self , event ):
                r= self.DVLC1.GetSelectedRow()
                #print self.DVLC1.GetValue(r,8)
                #print self.DVLC1.GetValue(r,9)
                #mtyp = self.DVLC1.GetValue(r,7)
                mtyp = self.chs2.GetStringSelection()
                mcod = self.inum.f2e( self.DVLC1.GetValue(r,9) )
                mres = self.chs1.GetSelection() 
                #mres = self.chs1.GetSelection()
                chtyp = self.chs2.GetStringSelection()
                sres  = self.chs1.GetStringSelection()
                #print mtyp
                #print sres
                
                if mtyp == u"آپارتمان" :
                        lbls = [u": تاریخ",u"نام مشتری",u"تلفن تماس",u"آدرس",
                                u"نام ساختمان",u"متراژ",u"مفید",u"تعداد طبقات",u"قدمت"]
                        iid = 41
                if mtyp == u"ویلائی":
                        lbls = [u": تاریخ",u"نام مشتری",u"تلفن تماس",u"آدرس",
                                u"نام ويلائي",u"مساحت",u"مفید",u"عرض کوچه",u"قدمت"]
                        iid = 42
                if mtyp == u"مغازه":
                        lbls = [u": تاریخ",u"نام مشتری",u"تلفن تماس",u"آدرس",
                                u"کاربري",u"متراژ",u"بالکن",u"تعدادبر",u"متراژبر"]
                        iid = 43
                if mtyp == u"زمین":
                        lbls = [u": تاریخ",u"نام مشتری",u"تلفن تماس",u"آدرس",
                                u"کاربري",u"مساحت",u"عرض کوچه",u"تعدادبر",u"متراژبر"]
                        iid = 44        

                if sres == u"فروش" :
                        txts = [u"متري",u"قيمت کل"]
                        cods = [u'1',iid,mcod]
                if sres == u"رهن":
                        txts = [u"رهن کامل",u""]
                        cods = [u'2',iid,mcod]
                if sres ==  u"رهن اجاره":
                        txts = [u"مبلغ پيش",u"اجاره ماهيانه"]
                        cods = [u'3',iid,mcod]

                ttr = sres+' '+mtyp
                titr = lbls          
                #print self.lstrow   
                self.b = wx.Frame(self,style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)
		#txt = [u"مبلغ کل",u"متري"]
		self.panel = RM.MyPanel1(self.b,titr,txts,cods,self.lstrow)
		#self.panel.SetLayoutDirection(2)
		self.b.SetSize((485,435))
		self.b.SetTitle(ttr)
		self.b.Show()
