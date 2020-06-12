# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

try:
    from agw import pycollapsiblepane as PCP
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.pycollapsiblepane as PCP
    
from Config.Init import *
import Database.MDataGet as DG
import Utility.calcu as ca
import Utility.calfar01 as calfar
import Utility.Adaad2 as adad
from wx import MessageBox,OK,YES_NO,ICON_WARNING,ICON_INFORMATION
import wx.lib.agw.pybusyinfo as PBI

import accsrh
import InAcc3 as IA
import Specy

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent, titr,txts,cods ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 660,315 ), style = wx.TAB_TRAVERSAL )

		self.iMolk = DG.GetData(u'',u'')
		self.jMolk = DG.SetData(u'',u'')
		self.inumr = adad.Adaad(1,'')
		self.titr = titr
		self.txts = txts
		TB = self.MRcods( cods )
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		self.SetFont( wx.Font( 11, 74, 90, 92, False, FONT_TYPE ) )
		###################################################
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		self.P1 = MyPanel3(self,titr,TB)
		Vsz2.Add( self.P1, 0,wx.EXPAND |wx.ALL, 5)
		
		Vsz1.Add( Vsz2, 0, wx.EXPAND, 5 )

		##################################################
		Vsz3 = wx.BoxSizer( wx.HORIZONTAL )
		self.lbl1 = u'امکانات'
		self.lbl2 = u'امکانات ملک'

		self.cpStyle = wx.CP_NO_TLW_RESIZE
		self.cp = cp = PCP.PyCollapsiblePane(self, label=self.lbl1,
                                             agwStyle=self.cpStyle)
		self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.OnPaneChanged, cp)
		Vsz3.Add( self.cp, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.cp.SetLayoutDirection(2)
		self.MakePaneContent(cp.GetPane())
		
		Vsz1.Add( Vsz3, 1, wx.EXPAND, 5 )

		##################################################
		Vsz4 = wx.BoxSizer( wx.VERTICAL )

		self.P4 = MyPanel4(self,txts)
		Vsz4.Add( self.P4, 0, wx.EXPAND|wx.ALL, 5)
		
		Vsz1.Add( Vsz4, 0, wx.EXPAND, 5 )
		
		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"ثبت شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn1.SetFont( wx.Font( 12, 74, 90, 92, False, FONT_TYPE ) )
		
		Hsz4.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn2.SetFont( wx.Font( 12, 74, 90, 92, False, FONT_TYPE ) )
		
		Hsz4.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz4, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
	        # Connect Events
	        self.P1.fld9.Bind( wx.EVT_CHAR, self.nxtfld )
	        
	        self.P4.fld10.Bind( wx.EVT_TEXT_ENTER, self.inmmtr )
	        self.P4.fld11.Bind( wx.EVT_TEXT_ENTER, self.inmblg )
		self.btn1.Bind( wx.EVT_BUTTON, self.savit )
		self.btn2.Bind( wx.EVT_BUTTON, self.cancl )
	
	def __del__( self ):
		pass
	
	def inmmtr( self , event ):
                imtry = int( event.GetEventObject().GetValue())
                mtraj = int( self.P1.imetr )
                mblgh = (imtry * mtraj)/1000
                if self.iRes == u'1':
                    self.P4.fld11.SetValue(unicode(mblgh))
        def inmblg( self , event ):
                imblg = int( event.GetEventObject().GetValue())
                mtraj = int( self.P1.imetr )
                mtry = (imblg*1000) / mtraj
                imtry = self.Rondit(mtry)
                #print mtry,imtry
                if self.iRes == u'1':
                    self.P4.fld10.SetValue(unicode(imtry))     
        def Rondit( self , number ):
                if (number%100)/10 >= 5:
                    return ((number/100)+1)*100
                else:
                    return (number/100)*100        
	# Virtual event handlers, overide them in your derived class
	def savit( self, event ):
                if self.Chkdata() == 1 :
                    D = self.Gnrdat()
                    self.SavAcc(D[0])
                    self.SavMlk(D[1])
                    self.SavMsp(D[2])
                    self.SavDes(D[3])
                    MessageBox(u'اطلاعات با موفقيت ثبت شد',u'اعلان',OK | ICON_INFORMATION)
                    self.filnul()
		#event.Skip()
	def Gnrdat( self ):
                D1 = self.P1.Rtdata()
                if self.iMtyp == 2:
                    D2 = self.pnl2.Gnfld()
                elif self.iMtyp == 3:
                    D2 = self.pnl3.Gnfld()  
                else:
                    D2 = self.pnl1.Gnfld()
                D3 = self.P4.Getfld()
                #print D3
                
                if len(D1[0]) > 1:
                    GD1 = [D1[0][0],D1[0][1],D1[0][2],D1[0][3],self.iRes]
                    self.Massage(u"مشتري جديد به ثبت رسيد")
                else:
                    GD1 = []
                    
                if  self.iMolk.glstMlk() == []:
                    Mcod = u'1001'
                else:
                    Mcod = unicode(int(self.iMolk.glstMlk()[-1][0])+1)
                    
                if self.iMolk.gMtgCk(D1[1][0]) == [] :
                    iMgcod = unicode(len(self.iMolk.gMntgh()))
                    self.jMolk.Inmntg(" Area , Aname ",[iMgcod,D1[1][0]])
                    self.Massage(u"منطقه جديد به ثبت رسيد")
                else:
                    iMgcod = self.iMolk.gMtgCk(D1[1][0])[0][0]
                
                #print D1,D2,D3    
                Adrs = hex(int(Mcod))[2:]+'-'+iMgcod+str(self.iMtyp)+self.iRes
                MSpc = hex(int(Mcod))[2:]+'-'+str(self.iMtyp)+self.iRes+iMgcod
                des  = hex(int(Mcod))[2:]+'-'+self.iRes+iMgcod+str(self.iMtyp)
                GD2 = [D1[2][0],Mcod,self.iRes,self.iMtyp,iMgcod,
                       D1[2][1],MSpc,D1[1][1],D1[2][2],D1[2][3],D1[2][5],D1[2][4],
                       D1[0][0],D3[0],D3[1],des]
                GD3 = [MSpc,str(D2)]
                GD4 = [des,D3[2]]
                return GD1,GD2,GD3,GD4

        def SavAcc(self,Data):
                if len(Data) > 1:
                    self.jMolk.InAcc("Acc , name, phone ,Spc ,Res ",Data) 
        def SavMlk(self,Data):
                self.jMolk.InMolk(" Date, Mcode , Res , Mtype , Area \
                                  ,Mname , MSpc , Addrss , M1 , M2 , M3 , M4 \
                                  , Acc , Amunt1 , Amunt2 , des ",Data) 
        def SavMsp(self,Data):
                self.jMolk.Inmspc(" MSpc , Spcfy ",Data) 
        def SavDes(self,Data):
                self.jMolk.InDes(" des , dscrpt ",Data)

        def filnul( self ):
                self.P1.Filnul()
                if self.iMtyp == 2:
                    self.pnl2.fulnul()
                elif self.iMtyp == 3:
                    self.pnl3.fulnul()  
                else:
                    self.pnl1.fulnul()
                self.P4.Filnul()
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
                
        def OnToggle(self, event):
                self.cp.Collapse(self.cp.IsExpanded())
                self.OnPaneChanged()

        def OnPaneChanged(self, event=None):
                # redo the layout
                self.Layout()
                if self.iMtyp == 2:
                    psiz = 250
                elif self.iMtyp == 3:
                    psiz = 80    
                else:
                    psiz = 280
                x = self.GetParent().GetSize()[0]
                y = self.GetParent().GetSize()[1]
                # and also change the labels
                if self.cp.IsExpanded():
                    self.cp.SetLabel(self.lbl2)
                    self.GetParent().SetSize((x,y+psiz))
                else:
                    self.cp.SetLabel(self.lbl1)
                    self.GetParent().SetSize((x,y-psiz))
                self.Refresh()
		self.Layout()
		
	def MakePaneContent(self, pane):
                #Just make for Emkanat pane
                if self.iMtyp == 2:
                    self.pnl2 = MyPanel7(pane)
                elif self.iMtyp == 3:
                    self.pnl3 = MyPanel8(pane)
                elif self.iMtyp == 1:
                    self.pnl1 = MyPanel6(pane)     
                else:
                    self.pnl1 = MyPanel5(pane)
                #pane.SetSizer

        def MRcods(self , cods):
                self.iRes = cods[0]
                if cods[1] in [41,45,47]:
                        self.iMtyp = 0
                        return [u'',u'']
                if cods[1] in [42,46,48]:
                        self.iMtyp = 1
                        return [u'0',u'1']
                if cods[1] in [43,49]:
                        self.iMtyp = 2
                        return [u'-1',u'-1']
                if cods[1] in [44]:
                        self.iMtyp = 3
                        return [u'-1',u'-1']
                #print self.iRes,self.iMtyp
        def Chkdata(self):
                #print self.P1.Chkpnl()
                if self.P1.Chkpnl():
                        itxt = self.P1.myerror
                        MessageBox(itxt,u'خطا',OK | ICON_WARNING)
                        return 0
                if self.P4.Chkpnl():    
                        itxt = self.P4.myerror
                        MessageBox(itxt,u'خطا',OK | ICON_WARNING)
                        return 0
                return 1
            
        def Massage(self, Msg ):
                #busy = PBI.PyBusyInfo(Msg, parent=None, title="Really Busy",
                #                      icon=images.Smiles.GetBitmap())
                busy = PBI.PyBusyInfo(Msg, parent=None, title=u"در حال پردازش")
                wx.Yield()
                for indx in xrange(3):
                    wx.MilliSleep(1000)
                del busy    
                
        def nxtfld( self, event):
            fid =  event.GetEventObject().GetId()
            if event.GetKeyCode() == wx.WXK_RETURN:
                if fid == 312:
                    #print fid
                    self.cp.SetFocus()
            event.Skip()

            
########################################################
## Validator
########################################################
class CharValidator(wx.PyValidator):
    def __init__(self, flag):
         wx.PyValidator.__init__(self)
         self.flag = flag
         self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
         """
         Note that every validator must implement the Clone() method.
         """
         return CharValidator(self.flag)

    def Validate(self, win):
         return True

    def TransferToWindow(self):
         return True 

    def TransferFromWindow(self):
         return True

    def OnChar(self, evt):
         key = chr(evt.GetKeyCode())
         if self.flag == "no-alpha" and key in string.letters:
              return
         if self.flag == "no-digit" and key in string.digits:
              return
         evt.Skip()


         
###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):
	
	def __init__( self, parent,lbls,TB ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 470,175 ), style = wx.RAISED_BORDER )

		self.iMolk = DG.GetData(u'',u'')
		self.jMolk = DG.SetData(u'',u'')
		self.inumr = adad.Adaad(1,'')
		self.lbls = lbls
		self.TB = TB
		#print lbls,TB
		
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.srch = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz1.Add( self.srch, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.iacc = wx.TextCtrl( self, 302, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
		#self.iacc.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		Hsz1.Add( self.iacc, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.txt2 = wx.StaticText( self, wx.ID_ANY, lbls[1], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )
		#self.txt2.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz1.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Hsz1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.don = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz1.Add( self.don, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.idate = wx.TextCtrl( self, 301, NOW, wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		Hsz1.Add( self.idate, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, lbls[0], wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.txt1.Wrap( -1 )
		#self.txt1.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz2.Add( Hsz1, 1, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fld2 = wx.TextCtrl( self, 305, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
		self.fld2.SetToolTipString( u"بلوار-خیابان-کوچه-پلاک" )
		
		Hsz2.Add( self.fld2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		#fld1Choices = []
		self.fld1Chs = self.GetAreaList()
		self.fld1 = wx.ComboBox( self, 304, u"منطقه", wx.DefaultPosition, wx.DefaultSize, self.fld1Chs, wx.CB_DROPDOWN|wx.CB_SORT|wx.TE_PROCESS_ENTER )
		Hsz2.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt4 = wx.StaticText( self, wx.ID_ANY, lbls[3], wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.txt4.Wrap( -1 )
		#self.txt4.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz2.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz2.Add( Hsz2, 1, wx.EXPAND, 5 )
		
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.iphon = wx.TextCtrl( self, 303, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
		Hsz3.Add( self.iphon, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.iphon.SetLayoutDirection(2)
		
		self.txt3 = wx.StaticText( self, wx.ID_ANY, lbls[2], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt3.Wrap( -1 )
		#self.txt3.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz3.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld5 = wx.TextCtrl( self, 308, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
		Hsz3.Add( self.fld5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt5 = wx.StaticText( self, wx.ID_ANY, lbls[4], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt5.Wrap( -1 )
		#self.txt5.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz3.Add( self.txt5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz2.Add( Hsz3, 1, wx.EXPAND, 5 )
		
		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.calcu = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap(UTILITY_PATH+u"calculator.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz4.Add( self.calcu, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Hsz4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.fld9 = wx.TextCtrl( self, 312, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.TE_LEFT|wx.TE_PROCESS_ENTER )
		Hsz4.Add( self.fld9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.fld9.SetLayoutDirection(2)
		
		self.txt9 = wx.StaticText( self, wx.ID_ANY, lbls[8], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt9.Wrap( -1 )
		#self.txt9.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz4.Add( self.txt9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		
                self.fld8 = wx.TextCtrl( self, 311, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.TE_LEFT|wx.TE_PROCESS_ENTER )
		Hsz4.Add( self.fld8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.fld8.SetLayoutDirection(2)
		
		self.txt8 = wx.StaticText( self, wx.ID_ANY, u"طبقات", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt8.Wrap( -1 )
		#self.txt8.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz4.Add( self.txt8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld7 = wx.TextCtrl( self, 310, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.TE_LEFT|wx.TE_PROCESS_ENTER )
		Hsz4.Add( self.fld7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.fld7.SetLayoutDirection(2)
		
		self.txt7 = wx.StaticText( self, wx.ID_ANY, lbls[6], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt7.Wrap( -1 )
		#self.txt7.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz4.Add( self.txt7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld6 = wx.TextCtrl( self, 309, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.TE_LEFT|wx.TE_PROCESS_ENTER )
		Hsz4.Add( self.fld6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.fld6.SetLayoutDirection(2)
		
		self.txt6 = wx.StaticText( self, wx.ID_ANY, lbls[5], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt6.Wrap( -1 )
		#self.txt6.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		
		Hsz4.Add( self.txt6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz2.Add( Hsz4, 1, wx.EXPAND, 5 )
		
		# Initial Panel And Prameter
		self.Pcal1 = wx.PopupTransientWindow(self.GetTopLevelParent(),wx.SIMPLE_BORDER)
                self.pnl = calfar.MyPanel2(self.Pcal1,-1,-1)

                self.pnl.Bind(wx.EVT_BUTTON,self.Onbind,source=None)

                		
		self.Initpn()

		self.imetr = ''
		
		self.myerror = u''

		#Show Hide item
		if TB[0] != u'' :
                    self.txt8.Hide()
                    self.fld8.Hide()
                if lbls[4] == u"نام ويلائي":
                    self.fld5.SetValue(u"شخصي")
                    
		self.SetSizer( Vsz2 )
		self.Layout()
		
		# Connect Events
		
		self.srch.Bind( wx.EVT_BUTTON, self.scracc )
		self.iacc.Bind( wx.EVT_CHAR, self.nxtfld )
		self.iacc.Bind( wx.EVT_TEXT, self.inacc )
		self.don.Bind( wx.EVT_BUTTON, self.Down )
		self.idate.Bind( wx.EVT_TEXT, self.chgdate )
		self.fld2.Bind( wx.EVT_CHAR, self.nxtfld )
		self.fld2.Bind( wx.EVT_TEXT, self.inaddr )
		self.fld1.Bind( wx.EVT_CHAR, self.nxtfld )
		self.fld1.Bind( wx.EVT_COMBOBOX, self.nware )
		self.fld1.Bind( wx.EVT_TEXT, self.inare )
		self.iphon.Bind( wx.EVT_CHAR, self.nxtfld )
		self.iphon.Bind( wx.EVT_TEXT, self.inphn )
		self.fld5.Bind( wx.EVT_CHAR, self.nxtfld )
		self.fld5.Bind( wx.EVT_TEXT, self.mlknam )
		self.calcu.Bind( wx.EVT_BUTTON, self.calc1 )
		self.fld9.Bind( wx.EVT_CHAR, self.nxtfld )
		self.fld9.Bind( wx.EVT_TEXT, self.inyer )
		self.fld7.Bind( wx.EVT_CHAR, self.nxtfld )
		self.fld7.Bind( wx.EVT_TEXT, self.inmfd )
		self.fld6.Bind( wx.EVT_CHAR, self.nxtfld )
		self.fld6.Bind( wx.EVT_TEXT, self.inmtr )
		if self.TB[0] == u'':
                    self.fld8.Bind( wx.EVT_CHAR, self.nxtfld )
                    #self.fld8.Bind( wx.EVT_TEXT, self.inlvl )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Initpn( self ):
                FONT = wx.Font( FONT_SIZE, 70, 90, 92, False, FONT_TYPE )
                self.txt1.SetFont( FONT )
                self.txt2.SetFont( FONT )
                self.txt3.SetFont( FONT )
                self.txt4.SetFont( FONT )
                self.txt5.SetFont( FONT )
                self.txt6.SetFont( FONT )
                self.txt7.SetFont( FONT )
                if self.TB[0] == u'' :
                    self.txt8.SetFont( FONT )
                self.txt9.SetFont( FONT )
                self.iacc.SetFocus()
                #self.fld2.SetMaxLength( 5 )
                self.iphon.SetValidator( CharValidator("no-alpha") )
                self.fld6.SetValidator( CharValidator("no-alpha") )
                self.fld7.SetValidator( CharValidator("no-alpha") )
                self.fld8.SetValidator( CharValidator("no-alpha") )
                self.fld9.SetValidator( CharValidator("no-alpha") )
	
	def scracc( self, event ):
		self.lstmoin = self.iMolk.ShwAcc()
                #print self.lstmoin
		iwin = wx.Dialog(self,-1)
		pnl = accsrh.MyPanel1(iwin,self.lstmoin)
		iwin.SetSize((262,446))
		iwin.ShowModal()

		self.icust = pnl.retdata()
		#print self.icust
		self.iacod = self.icust[0][0]
		self.iacc.SetValue(self.icust[0][1])
		self.iphon.SetValue(self.icust[0][2])
		self.fld1.SetFocus()

		self.Refresh()
		self.Layout() 
		iwin.Destroy()
	
	def nxtfld( self, event ):
                fid =  event.GetEventObject().GetId()
		if event.GetKeyCode() == wx.WXK_RETURN:
                    if fid == 302:
                        self.fld1.SetFocus()
                    if fid == 304:
                        self.fld2.SetFocus()
                    if fid == 305:
                        self.fld5.SetFocus()
                    if fid == 308:
                        self.iphon.SetFocus()
                    if fid == 303:
                        self.fld6.SetFocus()
                    if fid == 309:
                        self.fld7.SetFocus()    
                    if fid == 310:
                        if self.TB[0] == u'' :
                            self.fld8.SetFocus()
                        else:
                            self.fld9.SetFocus()
                    if fid == 311:
                        self.fld9.SetFocus()
		event.Skip()
	
	def inacc( self, event ):
		event.Skip()
	
	def Down( self, event ):
		self.Pcal1.SetSize((280,190))
		btn = event.GetEventObject()
                pos = btn.ClientToScreen( (0,0) )
                sz =  btn.GetSize()
                self.Pcal1.Position(pos, (0, sz[1]))
                
                self.Pcal1.Popup()
        def Onbind(self, event):
                r = event.GetEventObject().GetLabel()
                d = self.pnl.Zdate(event)
                self.idate.SetValue(d) 
	
	def chgdate( self, event ):
		event.Skip()
	
	def Chkpnl( self ):
                if self.iacc.GetValue() == u'':
                    self.myerror = u'نام مشتري را مشخص کنيد'
                    return True
                elif self.iphon.GetValue() == u'':
                    self.myerror = u'تلفن مشتري را ثبت کنيد'
                    return True
                elif self.fld1.GetValue() == u'' or self.fld1.GetValue() == u"منطقه":
                    self.myerror = u'منطقه ملک را مشخص کنيد'
                    return True
                elif self.fld2.GetValue() == u'':
                    self.myerror = u'آدرس ملک را مشخص کنيد'
                    return True
                elif self.fld5.GetValue() == u'':
                    self.myerror = self.lbls[4] + u' را مشخص کنيد '
                    return True
                elif self.fld6.GetValue() == u'':
                    self.myerror = self.lbls[5] + u' را مشخص کنيد '
                    return True
                elif self.fld7.GetValue() == u'':
                    self.myerror = self.lbls[6] + u' را مشخص کنيد '
                    return True
                #elif self.fld8 == u'':
                #    self.myerror = u'تعداد طبقات را مشخص کنيد'
                #    return True
                elif self.fld9.GetValue() == u'':
                    self.myerror = self.lbls[8] + u' را مشخص کنيد '
                    return True
                else:
                    return False
	def inaddr( self, event ):
		event.Skip()
	
	
	def nware( self, event ):
		event.Skip()
	def GetAreaList( self ):
                a = []
                alst = self.iMolk.gMntgh()
                for al in alst:
                    a.append(al[1])
                return a    
	def inare( self, event ):
		event.Skip()
	
	
	def inphn( self, event ):
		#print event.GetEventObject().GetValidator()
		event.Skip()
	
	
	def mlknam( self, event ):
		event.Skip()
	
	def calc1( self, event ):
		dlg = wx.Dialog(self,-1)
                pnl = ca.MyPanel1(dlg)
                dlg.SetSize((176,252))
                
                dlg.ShowModal()
                self.Refresh()
                self.Layout()
                dlg.Destroy()
	
	
	def inyer( self, event ):
                #if self.fld9.AcceptsFocus():
                #    print 'NewAcc'
                    
		event.Skip()
	
	
	def inmfd( self, event ):
		event.Skip()
	
	
	def inmtr( self, event ):
                self.imetr = self.fld6.GetValue()
		event.Skip()
	
        def Rtdata( self ):
                data = self.Getfld()
                if self.iMolk.gAccn(data[1]) == []:
                    data1 = self.newacc()
                else:
                    data1 = [self.iMolk.gAccn(data[1])[0][0]]
                #if self.iMolk.gMtgCk(data[3]) == []:
                #    iMgcod = len(self.fld1Chs)
                #    data2 = [iMgcod,data[3],data[4]]
                #else:
                #    iMgcod = self.iMolk.gMtgCk(data[3])[0][0]
                #    data2 = [iMgcod,data[3],data[4]]
                data2 = [data[3],data[4]]
                data3 = [data[0],data[5],data[6],data[7],data[8],data[9]]
                return data1,data2,data3
        def newacc( self ):
                if self.iMolk.glstA() == []:
                    accod = u'10001'
                else:
                    accod = unicode(int(self.iMolk.glstA()[-1][0])+1)
                acnam = self.iacc.GetValue()
                acphn = self.iphon.GetValue()
                acspc = hex(int(accod))[2:]+'-'+hex(self.inumr.abjad(acnam))[2:]
                return [accod,acnam,acphn,acspc]

	def Setfld( self , data):
                self.idate.SetValue(data[0])
                self.iacc.SetValue(data[1])
                self.iphon.SetValue(data[2])
                self.fld1.SetValue(data[3])
                self.fld2.SetValue(data[4])
                
                self.fld5.SetValue(data[5])
                self.fld6.SetValue(data[6])
                self.fld7.SetValue(data[7])
                
                self.fld8.SetValue(data[8])
                self.fld9.SetValue(data[9])
                               
                self.Refresh()
                self.Layout()
        def Filnul( self ):
                #self.idate.GetValue()
                self.iacc.SetValue(u'')
                self.iphon.SetValue(u'')
                self.fld1.SetValue(u'منطقه')
                self.fld2.SetValue(u'')
                if lbls[4] == u"نام ويلائي":
                    self.fld5.SetValue(u"شخصي")
                else:
                    self.fld5.SetValue(u'')
                self.fld6.SetValue(u'')
                self.fld7.SetValue(u'')
                self.fld8.SetValue(u'')
                self.fld9.SetValue(u'')
                self.Refresh()
                self.Layout()
        def Getfld( self ):
                f1 = self.idate.GetValue()
                f2 = self.iacc.GetValue()
                f3 =self.iphon.GetValue()
                f4 =self.fld1.GetValue()
                f5 =self.fld2.GetValue()
                
                f6 =self.fld5.GetValue()
                f7 =self.fld6.GetValue()
                f8 =self.fld7.GetValue()
                f9 =self.fld8.GetValue()
                f10 =self.fld9.GetValue()
                return [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
               
	
###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):
	
	def __init__( self, parent , txts ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 470,130 ), style = wx.RAISED_BORDER )
		
		Vsz4 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )
		
		Hsz5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.fld11 = wx.TextCtrl( self, 313, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		Hsz5.Add( self.fld11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.fld11.SetLayoutDirection(2)
		
		self.txt11 = wx.StaticText( self, wx.ID_ANY, txts[1], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt11.Wrap( -1 )
		self.txt11.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial" ) )
		
		Hsz5.Add( self.txt11, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

				
		self.fld10 = wx.TextCtrl( self, 312, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		Hsz5.Add( self.fld10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		self.fld10.SetLayoutDirection(2)
		
		self.txt10 = wx.StaticText( self, wx.ID_ANY, txts[0], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt10.Wrap( -1 )
		self.txt10.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial" ) )
		
		Hsz5.Add( self.txt10, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz4.Add( Hsz5, 0, wx.EXPAND, 5 )
		
		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.calc2 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap(UTILITY_PATH+ u"calculator.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz6.Add( self.calc2, 0, wx.ALL, 5 )
		
		self.fld14 = wx.TextCtrl( self, 316, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_RIGHT )
		Hsz6.Add( self.fld14, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.txt14 = wx.StaticText( self, wx.ID_ANY, u"توضیحات", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt14.Wrap( -1 )
		self.txt14.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial" ) )
		
		Hsz6.Add( self.txt14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz4.Add( Hsz6, 1, wx.EXPAND, 5 )

		
		self.myerror = u''

		#Show Hide Item
		if txts[0] == u"رهن کامل" or txts[1] == u'':
                    self.fld11.SetValue(u'0')
                    self.fld11.Hide()
                    
		self.fld10.SetValidator( CharValidator("no-alpha") )
                self.fld11.SetValidator( CharValidator("no-alpha") )
                
		self.SetSizer( Vsz4 )
		self.Layout()
		
		# Connect Events
		self.fld11.Bind( wx.EVT_CHAR, self.nxtfld )
		self.fld11.Bind( wx.EVT_TEXT, self.inmblg )
		self.fld10.Bind( wx.EVT_CHAR, self.nxtfld )
		self.fld10.Bind( wx.EVT_TEXT, self.inmmtr )
		self.calc2.Bind( wx.EVT_BUTTON, self.cacul )
		self.fld14.Bind( wx.EVT_CHAR, self.nxtfld )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def nxtfld( self, event ):
		fid =  event.GetEventObject().GetId()
		if event.GetKeyCode() == wx.WXK_RETURN:
                    if fid == 312:
                        self.fld11.SetFocus()
                    if fid == 313:
                        self.fld14.SetFocus()
                event.Skip()
                
       	
	def inmblg( self, event ):
		event.Skip()
	
	
	def inmmtr( self, event ):
                event.Skip()
                
	def Chkpnl( self ):
                if self.fld10.GetValue() == u'':
                    self.myerror = u'مبلغ را مشخص کنيد'
                    return True
                elif self.fld11.GetValue() == u'' and self.fld11.IsShown():
                    self.myerror = u'مبلغ را مشخص کنيد'
                    return True
                else:
                    return False
            
	def cacul( self, event ):
		dlg = wx.Dialog(self,-1)
                pnl = ca.MyPanel1(dlg)
                dlg.SetSize((176,252))
                
                dlg.ShowModal()
                self.Refresh()
                self.Layout()
                dlg.Destroy()
	def Setfld( self , D ):
                self.fld10.SetValue(D[0])
                self.fld11.SetValue(D[1])
                self.fld14.SetValue(D[2])
                self.Refresh()
                self.Layout()
        def Filnul( self ):
                self.fld10.SetValue(u'')
                self.fld11.SetValue(u'')
                self.fld14.SetValue(u'')
                self.Refresh()
                self.Layout()    
	def Getfld( self ):
                #self.Chkfld()
                f1 =self.fld10.GetValue()
                f2 =self.fld11.GetValue()
                f3 =self.fld14.GetValue()
                #print f1 , f2 
                return [f1,f2,f3]

###########################################################################
## Class MyPanel5
###########################################################################

class MyPanel5 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 470,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetFont( wx.Font( 11, 70, 90, 92, False, "Arial" ) )
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chsb = wx.CheckBox( self, wx.ID_ANY, u"نسقی", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz1.Add( self.chsb, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chsa = wx.CheckBox( self, wx.ID_ANY, u"سنددار", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz1.Add( self.chsa, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chs0 = wx.CheckBox( self, wx.ID_ANY, u"کمد دار", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz1.Add( self.chs0, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		Box1Choices = [u'\u0663', u'\u0662', u'\u0661' ]
		self.Box1 = wx.RadioBox( self, wx.ID_ANY, u"       تعداد اتاق خواب        ", wx.DefaultPosition, wx.DefaultSize, Box1Choices, 1, wx.RA_SPECIFY_ROWS )
		self.Box1.SetSelection( 0 )
		Hsz1.Add( self.Box1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz1, 0, wx.EXPAND, 5 )
		lbls1 = [u"پارکینگ",u"گاز",u"برق",u"آب",u"مستقل"]
		lbls2 = [u"پارکینگ",u"گاز",u"برق",u"آب",u"مشترک"]
		self.bhss = []
		i = 0
		
		gSizer5 = wx.GridSizer( 2, 5, 0, 0 )

		for lb in lbls1:
                    self.bhss.append(  wx.CheckBox( self, wx.ID_ANY, lb, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT ) )
                    gSizer5.Add( self.bhss[i], 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
                    self.bhss[i].Enable( False )
                    if i == 4:
                        self.bhss[i].Enable( True )
                    i = i + 1

                for lb in lbls2:
                    self.bhss.append(  wx.CheckBox( self, wx.ID_ANY, lb, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT ) )
                    gSizer5.Add( self.bhss[i], 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
                    self.bhss[i].Enable( False )
                    if i == 9:
                        self.bhss[i].Enable( True )
                    i = i + 1
    

                
		Vsz1.Add( gSizer5, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		lbls = [u"سرامیک",u"هود",u"گاز رومیزی",u"MDF",u"کابینت فلزی",u"اسپلیت"
                        ,u"کولر",u"نقاشی",u"موکت",u"کاغذ دیواری",u"آسانسور",u"تراس"
                        ,u"انباری",u"فرنگی",u"ایرانی"]
		Gsz1 = wx.GridSizer( 3, 5, 0, 0 )
		self.chss = []
		i = 0

		for lb in lbls:
                    self.chss.append( wx.CheckBox( self, wx.ID_ANY, lb, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT ) )
                    Gsz1.Add( self.chss[i], 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
                    i = i + 1

				
		Vsz1.Add( Gsz1, 0, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chs19 = wx.CheckBox( self, wx.ID_ANY, u"آب چاه", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz2.Add( self.chs19, 1, wx.ALL, 5 )
		
		self.chs18 = wx.CheckBox( self, wx.ID_ANY, u"تلفن", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz2.Add( self.chs18, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chs17 = wx.CheckBox( self, wx.ID_ANY, u"فول امکانات", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz2.Add( self.chs17, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz2, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.bhss[4].Bind( wx.EVT_CHECKBOX, self.most )
		self.bhss[9].Bind( wx.EVT_CHECKBOX, self.mosh )
		self.chs17.Bind( wx.EVT_CHECKBOX, self.fulle )
	
	def __del__( self ):
		pass     
	
        # Virtual event handlers, overide them in your derived class
        def most( self, event ):
		if event.GetEventObject().GetValue():
                    for i in range(4):
                        self.bhss[i].Enable( True )
                else:
                    for i in range(4):
                        self.bhss[i].Enable( False )
	
	def mosh( self, event ):
		if event.GetEventObject().GetValue():
                    for i in range(5,9):
                        self.bhss[i].Enable( True )
                else:
                    for i in range(5,9):
                        self.bhss[i].Enable( False )
	
	def full( self, event ):
		event.Skip()
		
	
	def Gnfld( self ):
                data = self.Getchs()
                #print data
                Rdata = u''
                for d in data:
                    if d == True:
                        Rdata = Rdata+u'T'
                    elif d == False:
                        Rdata = Rdata+u'F'
                    else:
                        Rdata = Rdata+d
                #print Rdata        
                return Rdata        
	def fulle( self, event ):
                
		if event.GetEventObject().GetValue():
                    #print 'full'
                    for i in range(15):
                        self.chss[i].SetValue(True)
                    #D = [1,T,T,T,T,T,T,T,T,T,T,
                    # T,T,T,T,T,T,T,T,T,T,
                    # T,T,T,T,T,T,T,T,T,T,T]
                if not event.GetEventObject().GetValue():
                    for i in range(15):
                        self.chss[i].SetValue(False)
                    #D = [1,F,F,F,F,F,F,F,F,F,F,
                    # F,F,F,F,F,F,F,F,F,F,
                    # F,F,F,F,F,F,F,F,F,F,F]
                #self.Setchs( D )
                self.Refresh()
		self.Layout()
	def fulnul( self ):
                
                D = [1,F,F,F,F,F,F,F,F,F,F,
                     F,F,F,F,F,F,F,F,F,F,
                     F,F,F,F,F,F,F,F,F,F,F]
                self.Setchs( D )
                self.Refresh()
		self.Layout()

	def Setchs( self , D):
                self.Box1.SetSelection(D[0])
                
                self.chs0.SetValue(D[1])
                self.chsa.SetValue(D[2])
                self.chsb.SetValue(D[3])
                j = 4
                for i in range(10):
                    self.bhss[i].SetValue(D[j])
                    j = j + 1
                k = 14    
                for i in range(15):
                    self.chss[i].SetValue(D[k])
                    k = k + 1
                    
                self.chs17.SetValue(D[29])                
                self.chs18.SetValue(D[30])
                self.chs19.SetValue(D[31])

                

        def Getchs( self ):
                D = []
                D.append( unicode(self.Box1.GetSelection()) )
                D.append( self.chs0.GetValue() )
                D.append( self.chsa.GetValue() )
                D.append( self.chsb.GetValue() )

                for i in range(10):
                    D.append( self.bhss[i].GetValue() )

                for i in range(15):
                    D.append( self.chss[i].GetValue() )

                D.append( self.chs17.GetValue() )
                D.append( self.chs18.GetValue() )
                D.append( self.chs19.GetValue() )
                
                return D

###########################################################################
## Class MyPanel6
###########################################################################

class MyPanel6 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 470,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetFont( wx.Font( 11, 70, 90, 92, False, "Arial" ) )
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chsb = wx.CheckBox( self, wx.ID_ANY, u"نسقی", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz1.Add( self.chsb, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chsa = wx.CheckBox( self, wx.ID_ANY, u"سنددار", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz1.Add( self.chsa, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chs0 = wx.CheckBox( self, wx.ID_ANY, u"کمد دار", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz1.Add( self.chs0, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		Box1Choices = [u'\u0663', u'\u0662', u'\u0661' ]
		self.Box1 = wx.RadioBox( self, wx.ID_ANY, u"       تعداد اتاق خواب        ", wx.DefaultPosition, wx.DefaultSize, Box1Choices, 1, wx.RA_SPECIFY_ROWS )
		self.Box1.SetSelection( 0 )
		Hsz1.Add( self.Box1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz1, 0, wx.EXPAND, 5 )
		lbls1 = [u"پارکینگ",u"گاز",u"برق",u"آب",u"تلفن"]
		#lbls2 = [u"پارکینگ",u"گاز",u"برق",u"آب",u"مشترک"]
		self.bhss = []
		i = 0
		
		gSizer5 = wx.GridSizer( 1, 5, 0, 0 )

		for lb in lbls1:
                    self.bhss.append(  wx.CheckBox( self, wx.ID_ANY, lb, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT ) )
                    gSizer5.Add( self.bhss[i], 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
                    i = i + 1

                #for lb in lbls2:
                #    self.bhss.append(  wx.CheckBox( self, wx.ID_ANY, lb, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT ) )
                #    gSizer5.Add( self.bhss[i], 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
                #    self.bhss[i].Enable( False )
                #    if i == 9:
                #        self.bhss[i].Enable( True )
                #    i = i + 1
    

                
		Vsz1.Add( gSizer5, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		lbls = [u"سرامیک",u"هود",u"گاز رومیزی",u"MDF",u"کابینت فلزی",u"اسپلیت"
                        ,u"کولر",u"نقاشی",u"موکت",u"کاغذ دیواری",u"",u""
                        ,u"آب چاه",u"فرنگی",u"ایرانی"]
		Gsz1 = wx.GridSizer( 3, 5, 0, 0 )
		self.chss = []
		i = 0

		for lb in lbls:
                    self.chss.append( wx.CheckBox( self, wx.ID_ANY, lb, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT ) )
                    Gsz1.Add( self.chss[i], 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
                    if lb == u"":
                        self.chss[i].Hide()
                    i = i + 1

				
		Vsz1.Add( Gsz1, 0, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
				
		self.chs17 = wx.CheckBox( self, wx.ID_ANY, u"نو سازی شده", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz2.Add( self.chs17, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz2, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		#self.bhss[4].Bind( wx.EVT_CHECKBOX, self.most )
		#self.bhss[9].Bind( wx.EVT_CHECKBOX, self.mosh )
		#self.chs17.Bind( wx.EVT_CHECKBOX, self.fulle )
	
	def __del__( self ):
		pass     
	
        # Virtual event handlers, overide them in your derived class
        def most( self, event ):
		if event.GetEventObject().GetValue():
                    for i in range(4):
                        self.bhss[i].Enable( True )
                else:
                    for i in range(4):
                        self.bhss[i].Enable( False )
	
	def mosh( self, event ):
		if event.GetEventObject().GetValue():
                    for i in range(5,9):
                        self.bhss[i].Enable( True )
                else:
                    for i in range(5,9):
                        self.bhss[i].Enable( False )
	
	def full( self, event ):
		event.Skip()
		
	
	def Gnfld( self ):
                data = self.Getchs()
                #print data
                Rdata = u''
                for d in data:
                    if d == True:
                        Rdata = Rdata+u'T'
                    elif d == False:
                        Rdata = Rdata+u'F'
                    else:
                        Rdata = Rdata+d
                #print Rdata        
                return Rdata
        '''    
	def fulle( self, event ):
                
		if event.GetEventObject().GetValue():
                    #print 'full'
                    for i in range(15):
                        self.chss[i].SetValue(True)
                    #D = [1,T,T,T,T,T,T,T,T,T,T,
                    # T,T,T,T,T,T,T,T,T,T,
                    # T,T,T,T,T,T,T,T,T,T,T]
                if not event.GetEventObject().GetValue():
                    for i in range(15):
                        self.chss[i].SetValue(False)
                    #D = [1,F,F,F,F,F,F,F,F,F,F,
                    # F,F,F,F,F,F,F,F,F,F,
                    # F,F,F,F,F,F,F,F,F,F,F]
                #self.Setchs( D )
                self.Refresh()
		self.Layout()
	'''	
	def fulnul( self ):
                
                D = [1,F,F,F,F,F,F,F,F,F,F,
                     F,F,F,F,F,F,F,F,F,F,
                     F,F,F,F]
                self.Setchs( D )
                self.Refresh()
		self.Layout()

	def Setchs( self , D):
                self.Box1.SetSelection(D[0])
                
                self.chs0.SetValue(D[1])
                self.chsa.SetValue(D[2])
                self.chsb.SetValue(D[3])
                j = 4
                for i in range(5):
                    self.bhss[i].SetValue(D[j])
                    j = j + 1
                k = 9    
                for i in range(15):
                    self.chss[i].SetValue(D[k])
                    k = k + 1
                    
                self.chs17.SetValue(D[24])                
                
                

        def Getchs( self ):
                D = []
                D.append( unicode(self.Box1.GetSelection()) )
                D.append( self.chs0.GetValue() )
                D.append( self.chsa.GetValue() )
                D.append( self.chsb.GetValue() )

                for i in range(5):
                    D.append( self.bhss[i].GetValue() )

                for i in range(15):
                    D.append( self.chss[i].GetValue() )

                D.append( self.chs17.GetValue() )
                                
                return D
 
###########################################################################
## Class MyPanel7
###########################################################################

class MyPanel7 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 470,250 ), style = wx.TAB_TRAVERSAL )
		
		self.SetFont( wx.Font( 11, 70, 90, 92, False, "Arial" ) )
		
		Vsz3 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chsb = wx.CheckBox( self, wx.ID_ANY, u"سرقفلی", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz3.Add( self.chsb, 1, wx.ALL, 5 )
		
		self.chsa = wx.CheckBox( self, wx.ID_ANY, u"نسقی", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz3.Add( self.chsa, 1, wx.ALL, 5 )
		
		self.chs0 = wx.CheckBox( self, wx.ID_ANY, u"سند دار", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz3.Add( self.chs0, 1, wx.ALL, 5 )
		
		
		Vsz3.Add( Hsz3, 0, wx.EXPAND, 5 )
		
		self.line1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.line1, 0, wx.EXPAND |wx.ALL, 5 )
		
		Gsz1 = wx.GridSizer( 3, 4, 0, 0 )

		lbls = [u"گاز",u"آب",u"تلفن",u"برق",u"سرویس بهداشتی",u"سیکوریت"
                        ,u"سرامیک",u"موزائیک",u"کولر",u"اسپلیت",u"درب برقی",u"ویترین"]
		self.chss = []
		i = 0
		for lb in lbls:
                    self.chss.append( wx.CheckBox( self, wx.ID_ANY, lb, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT ) )
                    Gsz1.Add( self.chss[i], 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
                    i = i + 1

                				
		Vsz3.Add( Gsz1, 0, wx.EXPAND, 5 )
		
		self.line2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.line2, 0, wx.EXPAND |wx.ALL, 5 )
		
		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )
		
		Box14Choices = [ u"نقاشی", u"کنیتکس", u"گچ", u"سرامیک" ]
		self.Box14 = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, Box14Choices, 1, wx.RA_SPECIFY_ROWS )
		self.Box14.SetSelection( 3 )
		Hsz4.Add( self.Box14, 0, wx.ALL, 5 )
		
		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"دیوار", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )
		Hsz4.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Hsz4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.chs15 = wx.CheckBox( self, wx.ID_ANY, u"فول", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		Hsz4.Add( self.chs15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"امکانات", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		Hsz4.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz3.Add( Hsz4, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( Vsz3 )
		self.Layout()
		
		# Connect Events
		self.chs15.Bind( wx.EVT_CHECKBOX, self.fulle )
	
	def __del__( self ):
		pass

	
	
	# Virtual event handlers, overide them in your derived class
	
	def Gnfld( self ):
                data = self.Getchs()
                #print data
                Rdata = u''
                for d in data:
                    if d == True:
                        Rdata = Rdata+u'T'
                    elif d == False:
                        Rdata = Rdata+u'F'
                    else:
                        Rdata = Rdata + d
                return Rdata       
	def fulle( self, event ):
		
		if event.GetEventObject().GetValue():
                    #print 'full'
                    D = [T,F,T,T,T,T,T,T,T,T,T,T,T,T,T,3,T]
                if not event.GetEventObject().GetValue():
                    D = [F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,0,F]
                self.Setchs( D )
                self.Refresh()
		self.Layout()
	def fulnul( self):
                
                D = [F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,0,F]
                self.Setchs( D )
                self.Refresh()
		self.Layout()
	def Setchs( self , D ):
                self.chs0.SetValue(D[0])
                self.chsa.SetValue(D[1])
                self.chsb.SetValue(D[2])

                j = 3
                for i in range(12):
                    self.chss[i].SetValue(D[j])
                    j = j + 1
                    
                self.Box14.SetSelection(D[15])
                
                self.chs15.SetValue(D[16])
                
        def Getchs( self ):
                D = []
                D.append( self.chs0.GetValue() )
                D.append( self.chsa.GetValue() )
                D.append( self.chsb.GetValue() )

                for i in range(12):
                    D.append( self.chss[i].GetValue() )
                                
                D.append( unicode(self.Box14.GetSelection()) )
                                                
                D.append( self.chs15.GetValue() )
                return D



###########################################################################
## Class MyPanel8
###########################################################################

class MyPanel8 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 470,100 ), style = wx.TAB_TRAVERSAL )
		
		self.SetFont( wx.Font( 11, 70, 90, 92, False, "Arial" ) )
		
		Vsz3 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		lbls = [u"موتور",u"برق",u"ساختمان",u"چاه",u"نسقی",u"سند دار"]
		self.chss = []
		i = 0
		for lb in lbls:
                    self.chss.append( wx.CheckBox( self, wx.ID_ANY, lb, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT ) )
                    Hsz1.Add( self.chss[i], 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
                    i = i + 1
		
				
		Vsz3.Add( Hsz1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( Vsz3 )
		self.Layout()
	
	def __del__( self ):
		pass
	def Setchs( self , D ):
                self.chss[0].SetValue(D[0])
                self.chss[1].SetValue(D[1])
                self.chss[2].SetValue(D[2])
                self.chss[3].SetValue(D[3])
                self.chss[4].SetValue(D[4])
                self.chss[5].SetValue(D[5])
        def fulnul( self):
                self.Setchs([False,False,False,False,False,False]) 

        def Getchs( self ):
                D1= self.chss[0].GetValue()
                D2= self.chss[1].GetValue()
                D3= self.chss[2].GetValue()
                D4= self.chss[3].GetValue()
                D5= self.chss[4].GetValue()
                D6= self.chss[5].GetValue()

                return [D1,D2,D3,D4,D5,D6]

        def Gnfld( self ):
                data = self.Getchs()
                Rdata = u''
                for d in data:
                    if d == True:
                        Rdata = Rdata+u'T'
                    if d == False:
                        Rdata = Rdata+u'F'
                #print Rdata    
                return Rdata           
