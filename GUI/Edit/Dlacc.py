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
import wx.grid
from Config.Init import *
import Database.MDataGet as DG
#import Utility.calcu as ca
#import Utility.calfar01 as calfar
import Utility.Adaad2 as adad
from wx import MessageBox,OK,ICON_WARNING,ICON_INFORMATION
import accsrh
import Specy

###########################################################################
## Class MyPanel7
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 366,430 ), style = wx.TAB_TRAVERSAL )

		self.iMolk = DG.GetData(u'',u'')
		self.inum = adad.Adaad(1,'')
		data = self.iMolk.ShwAcc2()

		
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
		
		#self.btn = wx.Button( self, wx.ID_ANY, u"برگشت", wx.DefaultPosition, wx.DefaultSize, 0 )
		#Vsz4.Add( self.btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		self.btn2 = wx.Button( self, wx.ID_ANY, u"انتخاب", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		
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
		#self.btn.Bind( wx.EVT_BUTTON, self.retit )
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.selcit, id = wx.ID_ANY )
		self.btn2.Bind( wx.EVT_BUTTON, self.selcit )
		self.btn1.Bind( wx.EVT_BUTTON, self.cancl )
	
	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()

                
        def selcit( self, event ):
                r= self.DVLC2.GetSelectedRow()
                acod = self.inum.f2e(self.DVLC2.GetValue(r,3))
                #data = [self.DVLC2.GetValue(r,2),self.DVLC2.GetValue(r,1)]
                self.b = wx.Frame(self,style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)
                #self.panel = MyPanel2(self.b,acod,data)
                #self.b.SetSize((430,170))
		#self.b.SetTitle(u"حذف مشتري")
                self.panel = MyPanel5(self.b,acod)
                self.b.SetSize((830,320))
		self.b.Show()

		self.panel.waitit()

		self.b.Close()

		          
	


		
###########################################################################
## Class MyPanel5
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent,acod,data ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 430,170 ), style = wx.TAB_TRAVERSAL )

		self.iMolk = DG.GetData(u'',u'')
		self.jMolk = DG.SetData(u'',u'')
		self.inumr = adad.Adaad(1,'')

		self.iacod = self.inumr.f2e(acod )  
		self.iname = data[0]
		self.iphon = data[1]
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fld1 = wx.TextCtrl( self, 51, self.iname, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
		Hsz1.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.fld1.SetLayoutDirection(2)
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"نام مشتری", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		self.txt1.SetFont( wx.Font( 14, 70, 90, 90, False, "B Zar" ) )
		
		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btns = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz1.Add( self.btns, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld0 = wx.TextCtrl( self, 50, self.iacod, wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_PROCESS_ENTER )
		Hsz1.Add( self.fld0, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt0 = wx.StaticText( self, wx.ID_ANY, u"کد مشتری", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt0.Wrap( -1 )
		self.txt0.SetFont( wx.Font( 14, 70, 90, 90, False, "B Zar" ) )
		
		Hsz1.Add( self.txt0, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fld2 = wx.TextCtrl( self, 52, self.iphon, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		Hsz2.Add( self.fld2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.fld2.SetLayoutDirection(2)
		
		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"تلفن تماس", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )
		self.txt2.SetFont( wx.Font( 14, 70, 90, 90, False, "B Zar" ) )
		
		Hsz2.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )
		
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"حذف شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Hsz3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"...مشخصات ", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )
		
		self.nwacc = False
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.fld1.Bind( wx.EVT_CHAR, self.nxtfld )
		self.btns.Bind( wx.EVT_BUTTON, self.accsrch )
		self.fld0.Bind( wx.EVT_CHAR, self.nxtfld )
		self.fld2.Bind( wx.EVT_CHAR, self.nxtfld )
		self.btn1.Bind( wx.EVT_BUTTON, self.savit )
		self.btn2.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn3.Bind( wx.EVT_BUTTON, self.spcacc )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def nxtfld( self, event ):
		fid =  event.GetEventObject().GetId()
                
		if event.GetKeyCode() == wx.WXK_RETURN:
                    if fid == 50:
                        self.fld1.SetFocus()
                    if fid == 51:
                        self.fld2.SetFocus()
                    if fid == 52:
                        self.btn1.SetFocus()
                event.Skip()        
	
	def accsrch( self, event ):
		self.lstmoin = self.iMolk.ShwAcc()
                #print self.lstmoin
		iwin = wx.Dialog(self,-1)
		pnl = accsrh.MyPanel1(iwin,self.lstmoin)
		iwin.SetSize((262,446))
		iwin.ShowModal()

		self.icust = pnl.retdata()
		#print self.icust
		self.fld0.SetValue(self.icust[0][0])
		self.fld1.SetValue(self.icust[0][1])
		self.fld2.SetValue(self.icust[0][2])

		self.Refresh()
		self.Layout() 
		iwin.Destroy()
	
	
	
	def savit( self, event ):
                if self.chkacc() == 1:
                    data = self.GetData()
                    self.jMolk.DelAcc("  Acc = '%s' "%self.accod)
                    self.jMolk.DelSpec(" Spc = %s "%self.ispec)
                    MessageBox(u'مشتري حذف شد',u'اعلان',OK | ICON_INFORMATION)
                    q = self.GetParent()
                    q.Close()
		

	def GetData( self ):
                f1 = self.fld0.GetValue()
                f2 = self.fld1.GetValue()
                f3 = self.fld2.GetValue()
                #f4 = self.Res+'1'+'-'+hex(int(self.Res[0])*100+int(f1))[2:]
                f4 = hex(int(f1))[2:]+'-'+hex(self.inumr.abjad(f2))[2:]
                
                #f5 = self.Res
                self.iacc = f4
                self.accod = f1
                return [f2,f3]
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
	def chkacc( self ):
                     
                if self.iMolk.gAccod(self.fld0.GetValue()) == []:
                    MessageBox(u'جهت ثبت مشتري جديد به ورود اطلاعات مشتري جديد برويد',u'خطا',OK | ICON_WARNING)
                    return 0
                
                return 1

                    
                    
	def spcacc( self, event ):
		txt1 = u"نام مشتري"
                txt2 = self.fld1.GetValue()
                txts = [txt1,txt2]
                tdata = self.GetData()
		iwin = wx.Dialog(self,-1)
		
		pnl = Specy.MyPanel2(iwin,txts,self.iacc,'111')
		
		iwin.SetSize((300,255))
		iwin.ShowModal()
		#print pnl.RetRev()
		if pnl.RetRev():
                        #pnl.savtit(idata,self.sData)
                        self.ispec = self.iMolk.gSpcy(self.iacc)
                        mdata = pnl.gettit()
                        #print mdata
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
                                
	

###########################################################################
## Class MyPanel5
###########################################################################

class MyPanel5 ( wx.Panel ):
	
	def __init__( self, parent , accod ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 819,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )

		self.iMolk = DG.GetData(u'',u'')
		self.jMolk = DG.SetData(u'',u'')
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

		self.myact = ''
		
		self.SetSizer( Vsz4 )
		self.Layout()
		self.loadata( accod )
		# Connect Events
		#self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_REORDERED, self.ordr, id = wx.ID_ANY )
		#self.Bind( wx.dataview.EVT_DATAVIEW_COLUMN_SORTED, self.Sort, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def loadata( self ,Acod ):
                #print Acod
                data = self.iMolk.Amlak4(" where Molks.Acc = %s "%Acod )
                #self.lstrow = []
                if data == []:
                        mydlg = MyDialog2(self)
                        mydlg.ShowModal()
                        #print 'Archive it',mydlg.Acarv
                        #print 'Delete it',mydlg.Acdel
                        mydlg.Destroy()
                        if mydlg.Acdel:
                                self.myact = 'Delete it'
                                self.delacc(Acod)
                                MessageBox(u'مشتري بکلي حذف شد',u'اعلان',OK | ICON_INFORMATION)
                                
                        if mydlg.Acarv:
                                self.myact = 'Archive it'
                                self.arcacc(Acod)
                                MessageBox(u'اطلاعات مشتري آرشيو و حذف شد',u'اعلان',OK | ICON_INFORMATION)
                                
                        
                else:
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
        def waitit( self ):
                #self.timer = wx.Timer(self)
                #self.timer.Start(5000)
                #self.timer.Stop()
                wx.Yield()
                for indx in xrange(5):
                        wx.MilliSleep(1000)
                
                
        def delacc( self , code):
                #print self.myact
                self.ispec = self.iMolk.gAcsp(code)[0][0]
                self.jMolk.DelAcc("  Acc = '%s' "%code)
                self.jMolk.DelSpec(" Spc = '%s' "%self.ispec)
        def arcacc( self , code):
                self.ispec = self.iMolk.gAcsp(code)[0][0]
                #Sdata = self.iMolk.gASpc(self.ispec)
                if self.iMolk.gAAcod(code) == []:
                        Data = self.iMolk.gAccod2(code)[0]
                        self.jMolk.InAAcc("Acc , name, phone ,Spc ,Res ",Data)
                        Sdata = self.iMolk.gASpc(self.ispec)
                        self.jMolk.ASpecin2('Spc , tit, Spcfy ',Sdata)
                        self.delacc(code)
                else:
                        MessageBox(u'قبلا مشتري بايگاني شده',u'خطا',OK | ICON_WARNING)

                        
                #print self.myact
        
	def ordr( self, event ):
		event.Skip()
	
	def Sort( self, event ):
		event.Skip()

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
	

###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY  )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		self.soal = wx.StaticText( self, wx.ID_ANY, u"...آیا میخواهید مشتری مورد نظر", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.soal.Wrap( -1 )
		self.soal.SetFont( wx.Font( 14, 70, 90, 92, False, "Arial" ) )
		
		Vsz2.Add( self.soal, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		Vsz1.Add( Vsz2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnarc = wx.Button( self, wx.ID_ANY, u"درآرشیو ذخیره شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnarc.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz1.Add( self.btnarc, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btndel = wx.Button( self, wx.ID_ANY, u"بکلی حذف شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btndel.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz1.Add( self.btndel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_button22 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button22.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz1.Add( self.m_button22, 0, wx.ALL, 5 )
		
		
		Vsz1.Add( Hsz1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.SetSizer( Vsz1 )
		self.Layout()
		Vsz1.Fit( self )

		self.Acdel = False
		self.Acarv = False
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnarc.Bind( wx.EVT_BUTTON, self.archit )
		self.btndel.Bind( wx.EVT_BUTTON, self.delit )
		self.m_button22.Bind( wx.EVT_BUTTON, self.cancl )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def archit( self, event ):
		self.Acarv = True
		self.Close()
	
	def delit( self, event ):
		self.Acdel = True
		self.Close()
	
	def cancl( self, event ):
		self.Close()
	
