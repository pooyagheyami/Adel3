# -*- coding: cp1256 -*-
# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wx
import wx.aui
import wx.html
import time

import GUI.MainMenu as MM

import GUI.AuiPanel.Rev as RP
import GUI.AuiPanel.Stat as SP
import GUI.BG as BG

import Config.config as bs
#import Utility.massage as ms
import Utility.clacal3 as C1
#import Utility.user as user
from Config.Init import * 
import wx.dataview

import GUI.proman as pro

  
class MainWin(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title=u'اصلي',size=(800,600))

        self.SetLayoutDirection(2)
        

        #Check config for first start prgram===============
        
        C = bs.BaseCheck()
        #print C
        #C = 0
        D = bs.Getprogini()
        #print D
        
        BGF = D[5]
        #print BGF 
        
        

        #Check config for show or hide aui panels=========
        rps = int(D[0])
        sps = int(D[1])
        cps = int(D[2])
        bps = int(D[3])
        tps = int(D[4])
        #rps = 1
        #sps = 1
        #bps = 1
        #tps = 1
        #BGF = "Mypic3.jpg"


        #Menu of Program============== 
        menu = MM.MainMenu()
        statusBar = self.CreateStatusBar(3)
        imenu=menu.createMenuBar()
        
        self.SetMenuBar(imenu)
        h= menu.GetItemId()
        h1 = menu.mid
        self.Bind(wx.EVT_MENU_RANGE,self.OnMenu,id =h1, id2=h.GetId())

        #Set The Status Windows in MainWin
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(1000)
        self.Notify()

        
        #Show aui panels============== 

        #Aui Panels of Program==================
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow( self )
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        #panel revnue======================

        
        self.Repnl(rps)

        #Panel report=======================
        

        self.Stpnl(sps)    

        #set background in frame ==================
        
        self.BGrnd(bps,BGF)

          
               
        self.m_mgr.Update()
        self.Centre( wx.BOTH )

        #if user.Checkpass() != 'OK':
        #    print 'quit'

        #Show other win in main windows==============
        '''
        if C == 1:
            wino = wx.Frame(self,-1,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
            
            txt = bs.Startpro()
            Startp = ms.MyPanel1(wino,txt)

            wino.SetSize((600,400))
            wino.SetPosition((100,100))
            wino.Show()

                
        
        '''
        self.SetStatusText(u"نام بنگاه :"+C[0]+u" نام عملکرد : "+C[1],1)

        self.Clock(tps)

        
        self.Update()    
        
    def Notify( self ):
        t = time.localtime(time.time())
        #st = time.strftime("%d-%b-%Y   %I:%M:%S", t)
        #stf = JalaliDatetime.now().strftime('%h:%r:%s')
        stf = JalaliDatetime.now().strftime('%X')
        self.SetStatusText(u" تاريخ :"+JalaliDatetime.now().strftime('%x')+u" ساعت :  "+stf,2)

    def OnMenu(self,event):
        
        self.mid = event.GetId()
        #print self.mid
        a = pro.DoProgram(self.mid)
        #print dir(a)
        s = a.size() if 'size' in dir(a) else ()
        
        win1 = wx.Frame(self,-1)
        win1.SetSize(s)
        a.main(win1)
    
    def OnShow(self,event):
        #print event
        
        self.Stap.refresh()
        self.Stap.showitem() 
        #self.Stap.Layout()
        #self.m_mgr.Update()
	#self.Centre( wx.BOTH )

    def Repnl(self,RPS):
        self.Rpanel = RP.MyPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_mgr.AddPane( self.Rpanel, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 37,54 ) ).Layer( 1 ) )
        self.m_mgr.Bind(wx.EVT_BUTTON,self.OnMenu)
        if RPS == 1 :
            self.m_mgr.GetPane(self.Rpanel).Show()
        elif RPS == 0:
            self.m_mgr.GetPane(self.Rpanel).Hide()
            
    def Stpnl(self,SPS):
        lbel = [u'مبلغ دريافتي',u'مورد معامله',u'نام مشتري',u'شماره معامله',u'تاريخ']
        
        self.Stap = SP.MyPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), wx.TAB_TRAVERSAL, lbel )
        self.m_mgr.AddPane( self.Stap, wx.aui.AuiPaneInfo() .Bottom() .PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 37,54 ) ).Layer( 2 ) )
        
        self.m_mgr.Bind(wx.EVT_TEXT,self.OnShow)
        #self.m_mgr.Bind(wx.EVT_WINDOW_DESTROY,self.OnShow) 
        
        if SPS == 1 :
            self.m_mgr.GetPane(self.Stap).Show()
        elif SPS == 0:
            self.m_mgr.GetPane(self.Stap).Hide()

    def Clock(self,TPS):
        #self.owin = wx.Frame(self,-1,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.owin = C1.MyFrame1(self)
	#clockpanel = C1.ClockPanel(self.owin)
        self.owin.SetSize((250,250))
        self.owin.SetPosition((20,50))
        if TPS == 1:
            self.owin.Show()
        elif TPS == 0:
            self.owin.Hide()


    def BGrnd(self,BPS,BGF):
        self.bmpwin = BG.MyHtmlPanel(self,wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL , BGF)    
        #self.htmlwin = BG.MyHtmlPanel(self,wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
        self.m_mgr.AddPane( self.bmpwin, wx.aui.AuiPaneInfo() .Right() .Center() .CloseButton( False ).Dock().Resizable().FloatingSize( wx.Size( 800,600 )) )
        #print self.bmpwin.GetSize()
        if BPS == 1 :
            self.m_mgr.GetPane(self.bmpwin).Show()
        elif BPS == 0:
            self.m_mgr.GetPane(self.bmpwin).Hide()
        #self.m_mgr.GetPane(self.htmlwin).Show()
        self.m_mgr.Bind(wx.EVT_CONTEXT_MENU,self.printit)
        #self.bmpwin.Bind(wx.EVT_CONTEXT_MENU,self.printit)
        #self.m_mgr.Bind(wx.EVT_MOUSE_EVENTS,self.printit)
        self.bmpwin.Bind(wx.EVT_MOUSE_EVENTS,self.printit)

    def printit(self,event):
        #print self.bmpwin.showhide()
                    
        if self.bmpwin.showhide()[0]:
            tps = 1
            try :
                self.owin.Show()
                tps = 1
            except:
                self.Clock(tps)
                

        elif not self.bmpwin.showhide()[0]:
            tps = 0
            try :
                self.owin.Hide()
                tps = 0
            except:
                self.Clock(tps)
            
        if self.bmpwin.showhide()[1]:
            rps = 1
            self.m_mgr.GetPane(self.Rpanel).Show()
        elif not self.bmpwin.showhide()[1]:
            rps = 0
            self.m_mgr.GetPane(self.Rpanel).Hide()
            
        if self.bmpwin.showhide()[2]:
            sps = 1
            self.m_mgr.GetPane(self.Stap).Show()
        elif not self.bmpwin.showhide()[2]:
            sps = 0
            self.m_mgr.GetPane(self.Stap).Hide()
        self.m_mgr.Update()
        
            
            

    
    
                               
                               
    
