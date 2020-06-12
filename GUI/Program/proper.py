# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import codecs
import string
from  Config.Init import *

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 525,387 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.MaxImageSize = 200
		m=self.readfile(CONFIG_PATH+'program.ini')
		self.rps = int(m[0])
		self.sps = int(m[1])
		self.bps = int(m[2])
		self.tps = int(m[3])
		if self.bps == 1 :
                        #self.bitpath = PICS_PATH+m[4]
                        self.bitpath = m[4]
                else:
                        self.bitpath = 'None'
		#print self.bitpath

		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,150 ), 0 )
		bSizer2.Add( self.m_bitmap1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
                        
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"انتخاب عکس پیش زمینه", u"*.jpg;*.bmp;*.png", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		bSizer2.Add( self.m_filePicker1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"انتخاب پشت زمینه", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_checkBox1.SetValue(True) 
		bSizer2.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		if self.bps == 1:
                        self.m_filePicker1.SetPath(PICS_PATH)
                        #self.Onphoto(self.bitpath)
                        #self.m_bitmap1.SetBitmap(wx.BitmapFromImage(self.setpic(self.bitpath)))
                        
                        self.m_checkBox1.SetValue(True)
                else:
                        #self.m_filePicker1.SetPath(m[3])
                        self.m_checkBox1.SetValue(False)
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"پنل ورود اطلاعات در سمت راست", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
                if self.rps == 1:
                        self.m_checkBox2.SetValue(True)
                else:
                        self.m_checkBox2.SetValue(False)
		bSizer3.Add( self.m_checkBox2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"پنل گزارش عملکرد در پائین صفحه", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
                if self.sps == 1:
                        self.m_checkBox3.SetValue(True)
                else:
                        self.m_checkBox3.SetValue(False)
		bSizer4.Add( self.m_checkBox3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

                bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.Enable( False )
		
		bSizer7.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"مختصات", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.Enable( False )
		
		bSizer7.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"نمایش ساعت و تقویم", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		#self.m_checkBox4.SetValue(True)
		if self.tps == 1:
                        self.m_checkBox4.SetValue(True)
                else:
                        self.m_checkBox4.SetValue(False)
		bSizer7.Add( self.m_checkBox4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )



		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"توجه!: لطفا بعد از  انتخاب موارد ، برنامه را بسته و مجدد باز کنید تا تغییرات اعمال شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer5.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"اعمال شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.Onphoto )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.Onbackg )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.Onpanel1 )
		self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.Onpanel2 )
		self.m_checkBox4.Bind( wx.EVT_CHECKBOX, self.Onpanel3 )
		self.m_button1.Bind( wx.EVT_BUTTON, self.Onapply )
		self.m_button2.Bind( wx.EVT_BUTTON, self.Oncancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Onphoto( self, event ):
                #print event.GetPath().split(PICS_PATH)
		self.Img = wx.Image(unicode(event.GetPath()), wx.BITMAP_TYPE_JPEG)
		#self.bitpath = event.GetPath().split(PICS_PATH)[1]
		#self.bitpath = event.GetPath()
		#print self.bitpath,event.GetPath()
		#print self.GetGrandParent()
		self.GetGrandParent().bmpwin.m_bitmap4.SetBitmap(wx.BitmapFromImage(self.Img))
		self.GetGrandParent().bmpwin.Refresh()
		self.GetGrandParent().bmpwin.Layout()
		
		W = self.Img.GetWidth()
		H = self.Img.GetHeight()
		if W > H:
                    NewW = self.MaxImageSize
                    NewH = self.MaxImageSize * H / W
                else:
                    NewH = self.MaxImageSize
                    NewW = self.MaxImageSize * W / H

                self.Img = self.Img.Scale(NewW,NewH)
                #print NewW,NewH,self.Img
		self.m_bitmap1.SetBitmap(wx.BitmapFromImage(self.Img))

		#self.GetGrandParent().bmpwin.m_bitmap4.SetBitmap(wx.BitmapFromImage(self.Img))


	        self.Refresh()
		self.Layout()

	def setpic(self,picfile):
                #print picfile[:-9]
                #p = self.bitpath
                #img =  wx.Image(unicode(p), wx.BITMAP_TYPE_JPEG)
                img = self.m_bitmap1.GetBitmap()
                #W = img.GetWidth()
                #H = img.GetHeight()
                W = 1550
                H = 900
                if W > H:
                        NewW = 200
                        NewH = 200 * H / W
                else:
                        NewH = 200
                        NewW = 200 * W / H
                #print img,NewW,NewH        
                #img = img.Scale(NewW,NewH)
                return img

	def Onbackg( self, event ):
		if self.m_checkBox1.GetValue():
                    self.bps = 1
                else:
                    self.bps = 0
	
	def Onpanel1( self, event ):
		if self.m_checkBox2.GetValue():
                    self.rps = 1
                else:
                    self.rps = 0
	
	def Onpanel2( self, event ):
		if self.m_checkBox3.GetValue():
                    self.sps = 1
                else:
                    self.sps = 0
	def Onpanel3( self, event ):
		if self.m_checkBox4.GetValue():
                    self.tps = 1
                else:
                    self.tps = 0
	def Onapply( self, event ):
                mydata = [self.rps,self.sps,self.tps,self.bps,self.bitpath]
                #print mydata
                self.changfile(CONFIG_PATH+'program.ini')
                       
                              
		q = self.GetParent()
		q.Close()
	
	def Oncancel( self, event ):
		q = self.GetParent()
		q.Close()

	def changfile(self,filename):
                fp = codecs.open(filename)
                writit = []
                lines = fp.readlines()
                self.bitpath = self.m_filePicker1.GetTextCtrlValue().split('\\')[-1]
                #print self.bitpath
                for line in lines:
                        if 'rps =' in line:
                                l=line.split('\r\n')
                                writit.append(string.replace(l[0],l[0][6],str(self.rps))+'\n')
                        elif 'sps =' in line:
                                l=line.split('\r\n')
                                writit.append(string.replace(l[0],l[0][6],str(self.sps))+'\n')
                        elif 'bps =' in line:
                                l=line.split('\r\n')
                                writit.append(string.replace(l[0],l[0][6],str(self.bps))+'\n')
                        elif 'tps =' in line:
                                l=line.split('\r\n')
                                writit.append(string.replace(l[0],l[0][6],str(self.tps))+'\n')        
                        elif 'BGF =' in line:
                                l=line.split('\r\n')
                                writit.append(string.replace(l[0],l[0][6::],str(self.bitpath))+'\r\n')
                                
                        else:
                                l=line.split('\r\n')
                                writit.append(l[0]+'\n')
                #print writit                
                fp = codecs.open(filename,'w')
                fp.writelines(writit)
                fp.close()

                
        def readfile(self,filename):
                fp = codecs.open(filename)
                lines = fp.readlines()
                backit = []
                for l in lines:
                        if 'rps =' in l:
                                backit.append(l[6])
                        if 'sps =' in l:
                                backit.append(l[6])
                        if 'bps =' in l:
                                backit.append(l[6])
                        if 'tps =' in l:
                                backit.append(l[6])
                        if 'BGF =' in l:
                                backit.append(l[6::])
                                
                #print backit
                return backit
                                
                
        

        
                                
                
	

