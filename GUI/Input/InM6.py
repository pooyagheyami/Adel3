# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import InMolk64 as IM
import Pmenu

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 150,260 ), style = wx.TAB_TRAVERSAL )
		
		Vsz = wx.BoxSizer( wx.VERTICAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u" فروش", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn1.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u" رهن", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn2.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u" رهن اجاره", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn3.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn3, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn4 = wx.Button( self, wx.ID_ANY, u" بستن ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn4.SetFont( wx.Font( 16, 70, 90, 92, False, "B Zar" ) )
		
		Vsz.Add( self.btn4, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Pcal1 = wx.PopupTransientWindow(self.GetTopLevelParent(),wx.SIMPLE_BORDER)
                self.pnl = Pmenu.MPanel(self.Pcal1)
                self.pnl.Bind(wx.EVT_BUTTON,self.Onbind,source=None)
		
		self.SetSizer( Vsz )
		self.Layout()
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.do1 )
		self.btn1.Bind( wx.EVT_MOTION, self.do1 )
		self.btn2.Bind( wx.EVT_BUTTON, self.do1 )
		self.btn2.Bind( wx.EVT_MOTION, self.do1 )
		self.btn3.Bind( wx.EVT_BUTTON, self.do1 )
		self.btn3.Bind( wx.EVT_MOTION, self.do1 )
		self.btn4.Bind( wx.EVT_BUTTON, self.onclose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	
	def do1( self, event ):
                self.t1 = event.GetEventObject().GetLabel()
                if self.t1 == u" رهن" or self.t1 == u" رهن اجاره"  :
                        self.pnl.Shwhid('123')
                else:
                        self.pnl.Shwhid('1234')
                self.Pcal1.SetSize((150,260))
		btn = event.GetEventObject()
                pos = btn.ClientToScreen( (0,0) )
                sz =  btn.GetSize()
                self.Pcal1.Position(pos, (-150, sz[1]-40))
                
                self.Pcal1.Show()
        def Onbind(self, event):
                self.t2 = event.GetEventObject().GetLabel()
                
                #d = self.pnl.Zdate(event)
                #self.idate.SetValue(d)
                #print self.t1,self.t2
                self.doit(None)
                

                
	def doit( self, event ):
                
                self.b = wx.Frame(self,style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)
                if self.t2 == u" آپارتمان":
                        lbls = [u": تاریخ",u"نام مشتری",u"تلفن تماس",u"آدرس",
                                u"نام ساختمان",u"متراژ",u"مفید",u"تعداد طبقات",u"قدمت"]
                        iid = 41
                if self.t2 == u" ویلائی":
                        lbls = [u": تاریخ",u"نام مشتری",u"تلفن تماس",u"آدرس",
                                u"نام ويلائي",u"مساحت",u"مفید",u"عرض کوچه",u"قدمت"]
                        iid = 42
                if self.t2 == u" مغازه":
                        lbls = [u": تاریخ",u"نام مشتری",u"تلفن تماس",u"آدرس",
                                u"کاربري",u"متراژ",u"بالکن",u"تعدادبر",u"متراژبر"]
                        iid = 43
                if self.t2 == u" زمین":
                        lbls = [u": تاریخ",u"نام مشتری",u"تلفن تماس",u"آدرس",
                                u"کاربري",u"مساحت",u"عرض کوچه",u"تعدادبر",u"متراژبر"]
                        iid = 44        

                if self.t1 == u" فروش":
                        txts = [u"متري",u"قيمت کل"]
                        cods = [u'1',iid]
                if self.t1 == u" رهن":
                        txts = [u"رهن کامل",u""]
                        cods = [u'2',iid]
                if self.t1 ==  u" رهن اجاره":
                        txts = [u"پيش",u"اجاره"]
                        cods = [u'3',iid]
                        
		ttr = self.t1+self.t2
                titr = lbls        
		#print titr
		self.panel = IM.MyPanel1(self.b,titr,txts,cods)
		#self.panel.SetLayoutDirection(2)
		self.b.SetSize((485,435))
		self.b.SetTitle(ttr)
		self.b.Show()
		q = self.GetParent()
		q.Hide()
		self.Pcal1.Hide()
		
	
	def onclose( self, event ):
		q = self.GetParent()
		q.Close()

	

