# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python
# -*- codnig: utf-8 -*-
import wx
import wx.html
from Config.Init import *



class MyHtmlPanel(wx.Panel):
    def __init__( self,parent,id,pos,siz,style,bgfile ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TAB_TRAVERSAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		self.SetLayoutDirection(2)

		mi = wx.Bitmap( PICS_PATH+bgfile, wx.BITMAP_TYPE_ANY )
		mi.SetSize((1440,900))
		#print mi.GetWidth()
		#print mi.GetHeight()

                               
                self.m1 = wx.Menu()

                	
		self.itm2 = wx.MenuItem( self.m1, wx.ID_ANY, u"نمایش ساعت و تقویم", wx.EmptyString, wx.ITEM_CHECK )
		self.m1.AppendItem( self.itm2 )
		self.itm2.Check( False )
		
		self.itm3 = wx.MenuItem( self.m1, wx.ID_ANY, u"نمایش پن ورود اطلاعات", wx.EmptyString, wx.ITEM_CHECK )
		self.m1.AppendItem( self.itm3 )
		self.itm3.Check( False )
		
		self.itm4 = wx.MenuItem( self.m1, wx.ID_ANY, u"نمایش پن وضعیت عملکرد", wx.EmptyString, wx.ITEM_CHECK )
		self.m1.AppendItem( self.itm4 )
		self.itm4.Check( False )

		
		#self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( bgfile , wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, mi, wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizer2.Add( self.m_bitmap4, 5, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap4.SetBitmap(mi)
		
		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.m_bitmap4.Bind( wx.EVT_RIGHT_DOWN, self.m_bitmap4OnContextMenu )
		
	
    def __del__( self ):
        	pass
            
    # Virtual event handlers, overide them in your derived class
    

    def m_bitmap4OnContextMenu( self, event ):
		self.m_bitmap4.PopupMenu( self.m1, event.GetPosition() )
		#print self.itm1.IsChecked(),self.itm2.IsChecked()
		#print self.itm3.IsChecked(),self.itm4.IsChecked()
    def showhide(self):
                return [self.itm2.IsChecked(),self.itm3.IsChecked(),self.itm4.IsChecked()]
