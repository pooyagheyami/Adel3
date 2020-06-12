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
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 816,427 ), style = wx.TAB_TRAVERSAL )

		self.iMolk = DG.GetData(u'',u'')
		self.inum = adad.Adaad(1,'')
		data = self.iMolk.Amlak2(u" where Molks.Res = 1 ")
		
		self.SetFont( wx.Font( FONT_SIZE, 70, 90, 92, False, FONT_TYPE ) )
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"دفتر املاک", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		self.txt1.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		Vsz2.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		Hsz = wx.BoxSizer( wx.HORIZONTAL )
		
		chs2Choices = [ u"همه", u"آپارتمان", u"ویلائی", u"مغازه", u"زمین" ]
		self.chs2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs2Choices, 0 )
		self.chs2.SetSelection( 0 )
		Hsz.Add( self.chs2, 0, wx.ALL, 5 )
		
		chs1Choices = [ u"فروش", u"رهن", u"رهن اجاره" ]
		self.chs1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs1Choices, 0 )
		self.chs1.SetSelection( 0 )
		Hsz.Add( self.chs1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz2.Add( Hsz, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Vsz2, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		Vsz3 = wx.BoxSizer( wx.VERTICAL )
		
		self.DVLC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES|wx.STATIC_BORDER )
		self.Column1 = self.DVLC1.AppendTextColumn( u"قیمت",width = 92 )
		self.Column2 = self.DVLC1.AppendTextColumn( u"قدمت",width = 72 )
		self.Column3 = self.DVLC1.AppendTextColumn( u"تعدادخواب",width = 92,align=wx.ALIGN_RIGHT )
		self.Column4 = self.DVLC1.AppendTextColumn( u"متراژ",width = 42 )
		self.Column5 = self.DVLC1.AppendTextColumn( u"آدرس" ,width = 212,align=wx.ALIGN_RIGHT )
		self.Column6 = self.DVLC1.AppendTextColumn( u"منطقه" ,width = 82,align=wx.ALIGN_RIGHT)
		self.Column7 = self.DVLC1.AppendTextColumn( u"نام ملک",width = 82 ,align=wx.ALIGN_RIGHT)
		self.Column8 = self.DVLC1.AppendTextColumn( u"نوع ملک" ,width = 62,align=wx.ALIGN_RIGHT)
		self.Column9 = self.DVLC1.AppendTextColumn( u"کد ملک" ,width = 52)
		Vsz3.Add( self.DVLC1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		Vsz1.Add( Vsz3, 1, wx.EXPAND, 5 )
		
		Vsz4 = wx.BoxSizer( wx.VERTICAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"بستن", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Vsz4, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.lstrow = []
		for d in data:
                        if d[2] == u'0':
                                DD = u'سه خوابه'
                        elif d[2] == u'1':
                                DD = u'دو خوابه'
                        elif d[2] == u'2':
                                DD = u'يک خوابه'
                        else:
                                DD = u'مغازه'
                                
                        d = (self.inum.Digigrop(d[0],','),self.inum.e2f(d[1])
                             ,DD,self.inum.e2f(d[3]),d[4],d[5],d[6],d[7],self.inum.e2f(d[8]) )
                        self.DVLC1.AppendItem(d)
                        self.lstrow.append( self.inum.f2e(d[8]) )


                for c in  self.DVLC1.Columns:
                        c.Sortable = True
                        c.Reorderable = True
                self.Column1.Sortable = False
		#self.Column2.Sortable = False
		#self.Column3.Sortable = False
		#self.Column4.Sortable = False
		
		self.SetSizer( Vsz1 )
		self.Layout()

		self.sql1 = u""
		self.sql2 = u""
		
		# Connect Events
		self.chs2.Bind( wx.EVT_CHOICE, self.chtyp )
		self.chs1.Bind( wx.EVT_CHOICE, self.chres )
		self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_REORDERED, self.ordr, id = wx.ID_ANY )
		self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_SORTED, self.Sort, id = wx.ID_ANY )
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.selct, id = wx.ID_ANY )
		self.btn1.Bind( wx.EVT_BUTTON, self.retrn )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def chtyp( self, event ):
		
		if self.chs2.GetSelection() > 0:
                        imtyp = self.chs2.GetSelection()-1
                        self.sql2 = u" and Molks.Mtype = %s "%imtyp
                else:
                        self.sql2 = u" "
                        
                self.relst(self.chs1.GetSelection()+1)        
	
	def chres( self, event ):
		ires = self.chs1.GetSelection()+1
		if self.chs1.GetSelection() == 1:
                        self.sql1 = u" where Molks.Res = %s "%ires
                        self.relst(2)
                        self.Column1.SetTitle(u"رهن کامل")
                        self.Column2.SetTitle(u"قدمت")
                elif self.chs1.GetSelection() == 2:
                        self.sql1 = u" where Molks.Res = %s "%ires
                        self.relst(3)
                        self.Column1.SetTitle(u"مبلغ اجاره")
                        self.Column2.SetTitle(u"مبلغ پيش")
                else:
                        self.Column1.SetTitle(u"قیمت")
                        self.Column2.SetTitle(u"قدمت")
                        self.sql1 = u" where Molks.Res = %s "%ires
                        self.relst(1)

                        
        def newd( self , d , sql ):
                if d == 1:
                        nwdata = self.iMolk.Amlak2(sql)
                if d == 2:
                        nwdata = self.iMolk.Amlak21(sql)
                if d == 3:
                        nwdata = self.iMolk.Amlak22(sql)
                return nwdata        
                

	def relst( self , D ):
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
                             ,DD,self.inum.e2f(d[3]),d[4],d[5],d[6],d[7],self.inum.e2f(d[8]) )
                        self.DVLC1.AppendItem(d)
                        self.lstrow.append( self.inum.f2e(d[8]) )
                        
                self.DVLC1.Refresh()
                self.Refresh()
                self.Layout()
           
	def ordr( self, event ):
		event.Skip()
	
	def Sort( self, event ):
		event.Skip()
	
	def selct( self, event ):
		r= self.DVLC1.GetSelectedRow()
                #print self.DVLC1.GetValue(r,8)
                #print self.DVLC1.GetValue(r,9)
		
                mtyp = self.DVLC1.GetValue(r,7)
                mcod = self.inum.f2e( self.DVLC1.GetValue(r,8) )
                mres = self.chs1.GetSelection()
                chtyp = self.chs2.GetStringSelection()
                sres  = self.chs1.GetStringSelection()
                #print mtyp
                #print sres
                
                if mtyp == u"آپارتمان" or chtyp == u"همه":
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
	
	def retrn( self, event ):
		q = self.GetParent()
                q.Close()
	
