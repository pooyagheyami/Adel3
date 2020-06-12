# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Config.Init import *
import Database.MDataGet as DG
#import define3 as df
import zipfile
from wx import MessageBox,OK,YES_NO,ICON_WARNING,ICON_INFORMATION
import tarfile

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,210 ), style = wx.TAB_TRAVERSAL )

		day = JalaliDatetime.now().strftime('%x')
		time = JalaliDatetime.now().strftime('%X')
		self.comp = DG.GetData(u'',u'')
		self.iabr = DG.SetData(u'',u'')
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.icomp = self.comp.gCmpny()
		if self.icomp == []:
                        self.icomp = [('','','','')]
		
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"نام بنگاه", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, self.icomp[0][1], wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		Hsz1.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"عملکرد", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )
		Hsz1.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		Hsz1.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz1.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt3 = wx.StaticText( self, wx.ID_ANY, u"تاریخ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt3.Wrap( -1 )
		Hsz2.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld3 = wx.TextCtrl( self, wx.ID_ANY, day, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT  )
		Hsz2.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt4 = wx.StaticText( self, wx.ID_ANY, u"ساعت", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt4.Wrap( -1 )
		Hsz2.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld4 = wx.TextCtrl( self, wx.ID_ANY, time, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.fld4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt5 = wx.StaticText( self, wx.ID_ANY, u"حجم فایل", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt5.Wrap( -1 )
		Hsz2.Add( self.txt5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		Hsz2.Add( self.fld5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )
		
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt6 = wx.StaticText( self, wx.ID_ANY, u"مسیر پشتیبانی", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt6.Wrap( -1 )
		Hsz3.Add( self.txt6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.file1 = wx.DirPickerCtrl( self, wx.ID_ANY,DATABASE_PATH, u"مسیر پشتیبانی را مشخص کنید",
                                               wx.DefaultPosition, wx.DefaultSize,
                                               wx.DIRP_CHANGE_DIR|wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST
                                               |wx.DIRP_SMALL|wx.DIRP_USE_TEXTCTRL )
		Hsz3.Add( self.file1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz3, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbtm = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_REPORT_VIEW, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz4.Add( self.lbtm, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		
		Hsz4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"گرفته شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz4, 1, wx.EXPAND, 5 )
		
		self.fld5.SetValue(str(os.stat(DATABASE_PATH+"Molk.db").st_size))
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.Revlst )
		self.file1.Bind( wx.EVT_DIRPICKER_CHANGED, self.gtpath )
		self.lbtm.Bind( wx.EVT_BUTTON, self.lstarc )
		self.btn2.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn3.Bind( wx.EVT_BUTTON, self.bakup )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Revlst( self, event ):
		rlst = self.comp.lsrev(self.icomp[0][0])
		#iwin = wx.Dialog(self,-1)
		#lrev = []
		#for i in range(len(rlst)):
                #    lrev.append(rlst[i][0])
                #pnl = df.MyPanel3(iwin,u"ليست عملکرد",lrev)
                #iwin.SetSize((168,300))
                #iwin.ShowModal()
                #rnm = pnl.Redata()
                #thsrev = self.comp.gRevnm(unicode(rnm))
                thsrev = self.comp.lsrev(self.icomp[0][0])
                self.fld2.SetValue(thsrev[0][0])
                #for i in range(len(rlst)):
                #    if rnm in rlst[i][0]:
                        #print rlst[i][1]
                #        self.file1.SetPath(DATABASE_PATH+rlst[i][1])
                #iwin.Destroy()
	def lodrev( self ):
               self.rlst = self.comp.gLstRv(self.icomp[0][0]) 
	
	def gtpath( self, event ):
		
		self.fld5.SetValue(os.stat(DATABASE_PATH+"Molk.db").st_size)

	def lstarc( self, event ):
                ldata = self.comp.gLBac()
                txt = u"ليست دفعات پشتيباني گرفته شده"
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel3(iwin,txt,ldata)
		iwin.SetSize((520,300))
		iwin.ShowModal()
		iwin.Destroy()
	
	def cancl( self, event ):
		q = self.GetParent()
		q.Close()
	
	def bakup( self, event ):
                d =  JalaliDatetime().now()
                self.s = str(d.year)+str(d.month)+str(d.day)+str(d.hour)+str(d.minute)+str(d.second)
                
                Path = self.file1.GetPath()
                with zipfile.ZipFile(Path+SLASH+"bac"+self.s+".zip","w") as izip:
                        izip.write(DATABASE_PATH+"Molk.db")
                        izip.write(DATABASE_PATH+"ABR.db")
                        izip.write(DATABASE_PATH+"Company.db")
                        
		tar = tarfile.open(TEMPS_PATH+"bac"+self.s+".tar","w")
		tar.add(DATABASE_PATH+"Molk.db")
		tar.add(DATABASE_PATH+"ABR.db")
		tar.add(DATABASE_PATH+"Company.db")
		tar.close()
		
		self.getdata()
                self.recdb()
                MessageBox(u'پشتيباني با موفقيت انجام شد',u'اعلان',OK | ICON_INFORMATION)

		q = self.GetParent()
		q.Close()
	def getdata( self ):
                                       
                ldata = self.comp.gLBac()
                n = len(ldata)+1
                f1 = self.fld1.GetValue()
                f2 = self.fld2.GetValue()
                f3 = self.fld3.GetValue()
                f4 = self.fld4.GetValue()
                f5 = self.fld5.GetValue()
                fil = self.file1.GetPath()
                self.data1 = [NOW,n,f2,f1]
                self.data2 = [n,"bac"+self.s+".zip",f3,f4,fil,f5]
                
	def recdb( self ):
                DG.sq.wxsqins('ABR.db','B',u'Bdate , Bac , Rev , Comp',self.data1)
                self.iabr.InBack(u'Bac , Bacfile , Bacdate , Bactime , Bacdir , Filsize',self.data2)
	

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,210 ), style = wx.TAB_TRAVERSAL )

		self.comp = DG.GetData(u'',u'')
		self.iabr = DG.SetData(u'',u'')
		self.icomp = self.comp.gCmpny()
		if self.icomp == []:
                        self.icomp = [('','','','')]
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"موسسه جاری", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, self.icomp[0][1], wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		Hsz1.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"فایل بازیابی اطلاعات", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )
		Hsz2.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.file1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"فایل بازیابی را مشخص کنید", u"*.zip;*.tar",
                                                wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		Hsz2.Add( self.file1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt3 = wx.StaticText( self, wx.ID_ANY, u"عملکرد", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt3.Wrap( -1 )
		Hsz2.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		Hsz2.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )
		
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt4 = wx.StaticText( self, wx.ID_ANY, u"تاریخ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt4.Wrap( -1 )
		Hsz3.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,wx.TE_RIGHT )
		Hsz3.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt5 = wx.StaticText( self, wx.ID_ANY, u"ساعت", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt5.Wrap( -1 )
		Hsz3.Add( self.txt5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.fld4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt6 = wx.StaticText( self, wx.ID_ANY, u"حجم فایل", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt6.Wrap( -1 )
		Hsz3.Add( self.txt6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		Hsz3.Add( self.fld5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )
		
		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbtm = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_REPORT_VIEW, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz4.Add( self.lbtm, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		Hsz4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"بازیابی شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.file1.Bind( wx.EVT_FILEPICKER_CHANGED, self.gtfile )
		self.lbtm.Bind( wx.EVT_BUTTON, self.lstres )
		self.btn1.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn2.Bind( wx.EVT_BUTTON, self.rstor )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def gtfile( self, event ):
		back =  event.GetEventObject().GetPath()
		fil = event.GetEventObject().GetTextCtrlValue()
		#print back,fil
		self.ifil = fil.split("\\")[-1]
		self.chkbac(self.ifil)
		with zipfile.ZipFile(self.ifil,"r") as izip:
                        info = izip.NameToInfo.keys()
                        zise  = izip.getinfo(info[0]).file_size
                        self.fld5.SetValue(unicode(zise))
		#print event.GetEventObject().GetInternalMargin()
		#tar = tarfile.open(back,"r")
		#for tarinfo in t2ar:
                #    print tarinfo.name
                #    print tarinfo.size
                #    print tarinfo.mtime
        def chkbac( self , fil):
                #print fil
                ifils = self.comp.gLBac()
                for fl in ifils:
                        if fil in fl:
                                self.setflds(fl)
                                #print fil
        def setflds(self,data):
                self.fld2.SetValue(data[0])
                self.fld3.SetValue(data[3])
                self.fld4.SetValue(data[4])
                #self.fld5.SetValue(data[])
                #self.fld5.SetValue(os.stat(DATABASE_PATH+"Main.db").st_size)
                
        def lstres( self, event ):
                ldata = self.comp.gLRes()
		txt = u"ليست دفعات بازيابي اطلاعات"
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel3(iwin,txt,ldata)
		iwin.SetSize((520,300))
		iwin.ShowModal()
		iwin.Destroy()           
	
	def cancl( self, event ):
		q = self.GetParent()
		q.Close()
	
	def rstor( self, event ):
		#print event.GetEventObject()
		self.unpack(self.ifil)
		self.recdb()
		MessageBox(u'بازيابي اطلاعات با موفقيت انجام شد',u'اعلان',OK | ICON_INFORMATION)
		p= wx.GetApp()
		p.Exit()
		wx.App_CleanUp()

	def unpack(self,fil):
                #print fil
                if fil[-4:] == '.zip':
                        with zipfile.ZipFile(fil,"r") as izip:
                                unpak = izip.namelist()
                                print MAP.split(SLASH)[0]
                                driv = MAP.split(SLASH)[0]+SLASH
                                izip.extractall(driv)
        def getdata( self ):
                                      
                ldata = self.comp.gLRes()
                n = len(ldata)+1
                f1 = self.fld1.GetValue()
                f2 = self.fld2.GetValue()
                f3 = self.fld3.GetValue()
                f4 = self.fld4.GetValue()
                f5 = self.fld5.GetValue()
                fil = self.file1.GetPath()
                self.data1 = [NOW,n,f2,f1]
                self.data2 = [n,self.ifil,f3,f4,fil,f5]                
	def recdb( self ):
                self.getdata()
                DG.sq.wxsqins('ABR.db','R',u'Rdate , Res , Rev , Comp',self.data1)
                self.iabr.InRest(u'Res , Resfile , Resdate , Restime , Resdir , Filsize',self.data2)

###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):
	
	def __init__( self, parent , txt , data ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 510,300 ), style = wx.TAB_TRAVERSAL )
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		self.titr = wx.StaticText( self, wx.ID_ANY, txt, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr.Wrap( -1 )
		Vsz2.Add( self.titr, 0, wx.ALL, 5 )
		
		
		Vsz1.Add( Vsz2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		Vsz3 = wx.BoxSizer( wx.VERTICAL )
		
		self.DVLC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
				
		self.col5 = self.DVLC1.AppendTextColumn( u"عملکرد" ,width = 50 )
		self.col4 = self.DVLC1.AppendTextColumn( u"نام فایل",width = 70 )
		self.col3 = self.DVLC1.AppendTextColumn( u"مسیر فایل",width = 200 )
		self.col2 = self.DVLC1.AppendTextColumn( u"تاریخ",width = 120 )
		self.Col1 = self.DVLC1.AppendTextColumn( u"ساعت" ,width = 70)
		
		Vsz3.Add( self.DVLC1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		Vsz1.Add( Vsz3, 1, wx.EXPAND, 5 )
		
		Vsz4 = wx.BoxSizer( wx.VERTICAL )
		
		self.btn = wx.Button( self, wx.ID_ANY, u"برگشت", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.btn, 0, wx.ALL, 5 )

		for item in data:
                        self.DVLC1.AppendItem(item)
		
		Vsz1.Add( Vsz4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.btn.Bind( wx.EVT_BUTTON, self.retn )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def retn( self, event ):
		q = self.GetParent()
		q.Close()
	

