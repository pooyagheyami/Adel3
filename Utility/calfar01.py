# -*- coding: utf-8 -*- 
#In the name of God
#!/usr/bin/env python

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import khayyam 
from datetime import timedelta
import  wx.lib.buttons  as  buttons

#----------------------------------------------------------------------
# This file was generated by C:\Portable Python 2.7.6.1\App\Lib\site-packages\wx-3.0-msw\wx\tools\img2py.py
#
from wx.lib.embeddedimage import PyEmbeddedImage

L = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAIAAADZrBkAAAAAA3NCSVQICAjb4U/gAAAASUlE"
    "QVQokdXTyw0AMAgC0NL9d8YFED9JD/X+ghoFyTOvuzDPGIAxy4xjxqTMG81KI1jH6LQNax6N"
    "SOtI3WQp09m8dCsxEj88TgDTyhUg3Ky0GgAAAABJRU5ErkJggg==")


R = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAIAAADZrBkAAAAAA3NCSVQICAjb4U/gAAAATElE"
    "QVQokdXTyREAIAgDQGP/PccCgEQZfeh/R44AkuP8zYa5zQA0f9NSFSmk6a2SfiSp3JpklC/3"
    "FpPkWZo+w6rEKiZSXjJ9GfjhcBZM5RUgzLJUOgAAAABJRU5ErkJggg==")


Y = int(khayyam.JalaliDate.today().strftime('%Y'))
M = int(khayyam.JalaliDate.today().strftime('%m'))

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel  ):
    
    
    def __init__( self, parent , year=Y , month=M ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 280,190 ), style = wx.TAB_TRAVERSAL )

        self.SetLayoutDirection(2)
        VSz1 = wx.BoxSizer( wx.VERTICAL )
        
        Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

        self.year = year
        self.month = month

        if year==-1:
            sal=khayyam.JalaliDate.today().strftime('%N')
            self.sallat = int(khayyam.JalaliDate.today().strftime('%Y'))
        else:
            sal = khayyam.JalaliDate(year=year).strftime('%N')
            self.sallat = int(khayyam.JalaliDate(year=year).strftime('%Y'))
        if month==-1:
            mah=khayyam.JalaliDate.today().strftime('%B')
            self.mahlat = int(khayyam.JalaliDate.today().strftime('%m'))
        else:
            mah = khayyam.JalaliDate(month=month).strftime('%B')
            self.mahlat = int(khayyam.JalaliDate(month=month).strftime('%m'))
        self.w = self.firstweekofmonth(self.sallat,self.mahlat)

        
        self.nxtbm = wx.BitmapButton( self, wx.ID_ANY, R.GetBitmap(), wx.DefaultPosition, wx.Size( 10,10 ), 0|wx.NO_BORDER )
        self.nxtbm.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        Hsz1.Add( self.nxtbm, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )
        
        self.hedbt = wx.Button( self, wx.ID_ANY, mah+' '+sal, wx.DefaultPosition, wx.Size( -1,20 ), wx.NO_BORDER )
        self.hedbt.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        Hsz1.Add( self.hedbt, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.bakbm = wx.BitmapButton( self, wx.ID_ANY, L.GetBitmap(), wx.DefaultPosition, wx.Size( 10,10 ), 0|wx.NO_BORDER )
        self.bakbm.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        Hsz1.Add( self.bakbm, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )
        
        
        VSz1.Add( Hsz1, 0, wx.EXPAND, 5 )
        
        VBz = wx.BoxSizer( wx.VERTICAL )
        
        self.pbdy = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER )
        VPz = wx.BoxSizer( wx.VERTICAL )

        
        
        Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

        haft = khayyam.jalali_date.PERSIAN_WEEKDAY_ABBRS

        for i in range(7):
                    self.m_staticText23 = wx.StaticText( self.pbdy, wx.ID_ANY, haft[i], wx.DefaultPosition, wx.Size( 9,-1 ), wx.ALIGN_CENTRE )
                    self.m_staticText23.Wrap( -1 )
                    Hsz2.Add( self.m_staticText23, 1, 0, 5 )
        
        
        VPz.Add( Hsz2, 0, wx.EXPAND, 5 )
        
        gSizer2 = wx.GridSizer( 6, 7, 2, 2 )

        labl=self.calntxt(self.sallat,self.mahlat)
        i = 0
        self.caltext=[]

        for row in range(6):
                    for clm in range(7):
                        self.caltext.append(buttons.GenButton( self.pbdy, wx.ID_ANY, e2f(labl[i]), wx.DefaultPosition, wx.Size( -1,-1 ), style=wx.BORDER_NONE ))
                        gSizer2.Add( self.caltext[i], 0, wx.EXPAND, 0 )
                        self.caltext[i].SetLayoutDirection(1)
                        #self.caltext[i].Bind(wx.EVT_BUTTON,self.Zdate)
                        #print labl[i],type(labl[i])
                        self.forbakgrnd( i , row , clm , labl[i])
                        i = i + 1
        
        
        VPz.Add( gSizer2, 1, wx.EXPAND, 5 )
        
        
        self.pbdy.SetSizer( VPz )
        self.pbdy.Layout()
        VPz.Fit( self.pbdy )
        VBz.Add( self.pbdy, 1, 0, 0 )
        
        
        VSz1.Add( VBz, 1, wx.EXPAND, 5 )
        
        VFz = wx.BoxSizer( wx.VERTICAL )

        self.rooz = int(khayyam.JalaliDate.today().strftime('%d'))
        self.irooz = self.rooz

        a = self.calnom(self.sallat,self.mahlat,self.rooz)

        if a > 0:
            self.caltext[a].SetBackgroundColour( wx.Colour( 70, 170, 240 ) )

        now =  khayyam.JalaliDate.today().strftime('%x')
        txt = u'امروز'
        
        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, now+':'+txt, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )
        VFz.Add( self.m_staticText22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        VSz1.Add( VFz, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.SetSizer( VSz1 )
        self.Layout()
        
        # Connect Events
        self.bakbm.Bind( wx.EVT_BUTTON, self.left )
        self.nxtbm.Bind( wx.EVT_BUTTON, self.right )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def firstweekofmonth(self,year,month):
        #print int(khayyam.JalaliDate(year,month,1).strftime('%w'))
        return int(khayyam.JalaliDate(year,month,1).strftime('%w'))
        
    def left( self, event ):
        self.mahlat=self.mahlat+1
        if self.mahlat>12:
            self.sallat=self.sallat+1
            self.mahlat=1

        mah=khayyam.JalaliDate(self.sallat,self.mahlat).monthname()
        self.hedbt.SetLabel(mah+' '+str(self.sallat))
        self.Refresh()
        self.Layout()

        #self.calntxt(self.sallat,self.mahlat)
        self.calgrid()

        self.pbdy.HideWithEffect(5,200)
        self.pbdy.Show()
        self.pbdy.Refresh()
        self.pbdy.Layout()
    
        
    def right( self, event ):
        self.mahlat=self.mahlat-1
        if self.mahlat<=0:
            self.sallat=self.sallat-1
            self.mahlat=12

        mah=khayyam.JalaliDate(self.sallat,self.mahlat).monthname()
        self.hedbt.SetLabel(mah+' '+str(self.sallat))
        self.Refresh()
        self.Layout()
        #self.calntxt(self.sallat,self.mahlat)
        self.calgrid()
        self.pbdy.HideWithEffect(6,200)
        self.pbdy.Show()
        self.pbdy.Refresh()
        self.pbdy.Layout()
    
    def forbakgrnd( self , i , row , clm , labl ):
        if clm == 6:
            self.caltext[i].SetBackgroundColour(wx.Colour( 0, 238, 0 ) )

        else:
            self.caltext[i].SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW  ) )

        if row == 0  and int(labl) > 7 or row >=  4 and int(labl) < 13:
            self.caltext[i].SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ))
            #self.caltext[i].Bind(wx.EVT_BUTTON,self.Zdate)
        else:
            self.caltext[i].SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ))

    def calgrid(self):
        labl=self.calntxt(self.sallat,self.mahlat)
        i=0
        #print self.m_textCtrl17.GetParent()

        for row in range(6):
            for clm in range(7):
                self.caltext[i].SetLabel(e2f(labl[i]))
                if row == 0  and int(labl[i]) > 7 or row >=  4 and int(labl[i]) < 13:
                    self.caltext[i].SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
                    #self.caltext[i].Bind(wx.EVT_BUTTON,self.Zdate)
                else:
                    self.caltext[i].SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
                                      
                i = i+1

    def calntxt(self,sal,mah):
        label = []
        a=0
        c=1
        b=1
        for d in range(42):
            if d < self.firstweekofmonth(sal,mah):
                label.append((khayyam.JalaliDate(sal,mah,1)-
                              timedelta(days=
                                        (self.firstweekofmonth(sal,mah)-d))).strftime('%d'))
            if d >= self.firstweekofmonth(sal,mah):
                if c > khayyam.JalaliDate(sal,mah).daysinmonth:
                    a=a+1
                    label.append(str(a))
                else:
                    label.append(str(c))
                    c=c+1
        return label

    def calnom(self,sal,mah,rooz):
        #a=self.firstweekofmonth(sal,mah)
        i = -1
        if sal == int(khayyam.JalaliDate.today().strftime("%Y")) and mah == int(khayyam.JalaliDate.today().strftime("%m")) and rooz == int(khayyam.JalaliDate.today().strftime("%d")):
           #h = int(khayyam.JalaliDate.today().strftime("%w"))
           i = rooz + (self.w-1)
        return i

    
    def Zdate(self , event ):
        r = event.GetEventObject().GetLabel()
        c = event.GetEventObject().GetForegroundColour()
        #print c,'Zdate',event.GetEventObject().GetPosition()[1]
        if c == (180, 180, 180, 255):
            p= event.GetEventObject().GetPosition()[1]
            if p == 16:
                self.right(event)
            if p >= 100:
                self.left(event)
        else:
            self.Rdate(r)
        return self.Rdate(r)    
      
    def Rdate(self,irooz):
        self.irooz = irooz
        
        return khayyam.JalaliDatetime(year=self.sallat,month=self.mahlat,day=self.irooz).strftime('%N/%P/%K')




def e2f(number):
    s = ''
    adadha = {u'0':1632 , u'1':1633 ,u'2':1634 , u'3':1635 , u'4':1636 ,u'5':1637 ,u'6':1638 ,u'7':1639 ,u'8':1640 ,u'9':1641 }
    for c in number:
        #print c
        s = s + unichr(adadha[c])
        #print s
    #print s
    return s      
        
