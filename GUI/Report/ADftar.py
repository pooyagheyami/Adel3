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
## Class MyPanel2
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 366,430 ), style = wx.TAB_TRAVERSAL )

		self.iMolk = DG.GetData(u'',u'')
		self.inum = adad.Adaad(1,'')
		data = self.iMolk.ShwAcc2()

		self.SetFont( wx.Font( FONT_SIZE, 74, 90, 92, False, FONT_TYPE ) )
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		self.titr1 = wx.StaticText( self, wx.ID_ANY, u"لیست مشتریان", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr1.Wrap( -1 )
		Vsz2.Add( self.titr1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Vsz2, 0, wx.EXPAND, 5 )
		
		Vsz3 = wx.BoxSizer( wx.VERTICAL )
		
		self.DVLC2 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Col0 = self.DVLC2.AppendTextColumn( u"درخواست" )
		self.Col1 = self.DVLC2.AppendTextColumn( u"تلفن" )
		self.Col2 = self.DVLC2.AppendTextColumn( u"نام حساب" )
		self.Col3 = self.DVLC2.AppendTextColumn( u"کد حساب" )
		#self.Col0 = self.DVLC2.AppendTextColumn( u"کد حساب" )
		#self.Col1 = self.DVLC2.AppendTextColumn( u"نام حساب"  )
		#self.Col2 = self.DVLC2.AppendTextColumn( u"تلفن" )
		#self.Col3 = self.DVLC2.AppendTextColumn( u"درخواست" )
		Vsz3.Add( self.DVLC2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		Vsz1.Add( Vsz3, 1, wx.EXPAND, 5 )
		
		Vsz4 = wx.BoxSizer( wx.VERTICAL )
		
		self.btn = wx.Button( self, wx.ID_ANY, u"برگشت", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Vsz4, 0, wx.EXPAND, 5 )

		for d in data:
                        d = (d[3],self.inum.e2f2(d[2]),d[1],self.inum.e2f(d[0]))
                        #print d
                        self.DVLC2.AppendItem(d)

		
		#for itemvalues in data:
                        
                #        self.DVLC2.AppendItem(itemvalues[::-1])
		
		for c in  self.DVLC2.Columns:
                        c.Sortable = True
                        c.Reorderable = True
                        
		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.btn.Bind( wx.EVT_BUTTON, self.retit )
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.selcit, id = wx.ID_ANY )
		
	
	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def retit( self, event ):
		q = self.GetParent()
                q.Close()
                
	def selcit( self, event ):
                r= self.DVLC2.GetSelectedRow()
                acod = self.inum.f2e(self.DVLC2.GetValue(r,3))
                self.b = wx.Frame(self,style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)
                
                self.panel = MyPanel5(self.b,acod)
                self.b.SetSize((830,320))
		self.b.Show()
	

###########################################################################
## Class MyPanel5
###########################################################################

class MyPanel5 ( wx.Panel ):
	
	def __init__( self, parent , accod ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 819,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )

		self.iMolk = DG.GetData(u'',u'')
		
		self.inum = adad.Adaad(1,'')
		
		Vsz4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"لیست ملکهای این مشتری", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( 18, 70, 90, 92, False, "Arial" ) )
		
		bSizer30.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz4.Add( bSizer30, 0, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.DVLC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES|wx.STATIC_BORDER )
		self.Column1 = self.DVLC1.AppendTextColumn( u"قيمت" )
		self.Column2 = self.DVLC1.AppendTextColumn( u"متري" )
		self.Column3 = self.DVLC1.AppendTextColumn( u"تعداد خواب" )
		self.Column4 = self.DVLC1.AppendTextColumn( u"قدمت" )
		self.Column5 = self.DVLC1.AppendTextColumn( u"مفید" )
		self.Column6 = self.DVLC1.AppendTextColumn( u"متراژ" )
		self.Column7 = self.DVLC1.AppendTextColumn( u"آدرس" )
		self.Column8 = self.DVLC1.AppendTextColumn( u"منطقه" )
		self.Column9 = self.DVLC1.AppendTextColumn( u"نام ملک" )
		self.Column10 = self.DVLC1.AppendTextColumn( u"کد ملک" )
		bSizer29.Add( self.DVLC1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		Vsz4.Add( bSizer29, 1, wx.EXPAND, 5 )

		
		for c in  self.DVLC1.Columns:
                        c.Sortable = True
                        c.Reorderable = True
		self.Column1.Sortable = False
		self.Column2.Sortable = False

		
		
		self.SetSizer( Vsz4 )
		self.Layout()
		self.loadata( accod )
		# Connect Events
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slcit, id = wx.ID_ANY )

		#self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_REORDERED, self.ordr, id = wx.ID_ANY )
		#self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_SORTED, self.Sort, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def loadata( self ,Acod ):
                #print Acod
                data = self.iMolk.Amlak4(" where Molks.Acc = %s "%Acod )
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
                        
                self.DVLC1.Refresh()
                self.Refresh()
                self.Layout()
                
        def slcit( self , event ):
                
		r= self.DVLC1.GetSelectedRow()
                #print self.DVLC1.GetValue(r,8)
                #print self.DVLC1.GetValue(r,9)
		
                mcod = self.inum.f2e( self.DVLC1.GetValue(r,9) )
                DDD = self.iMolk.ShwMlks(mcod)
                
                mtyp = self.iMolk.gMtyp(DDD[0][3])[0][0]
                
                #mres = self.iMolk.
                #chtyp = self.iMolk.
                sres  = self.iMolk.gCRes(DDD[0][2])[0][0]
                #print mtyp
                #print sres
                #print self.lstrow
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

                if sres == u"فروش":
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
                
                self.b = wx.Frame(self,style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)
		#txt = [u"مبلغ کل",u"متري"]
		self.panel = RM.MyPanel1(self.b,titr,txts,cods,self.lstrow)
		#self.panel.SetLayoutDirection(2)
		self.b.SetSize((485,435))
		self.b.SetTitle(ttr)
		self.b.Show()
