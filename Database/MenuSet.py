#In The name of God
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

import wxsq2 as sq


class GetData:
    def __init__(self,send,gets):
        self.send = send
        self.gets = gets

    def ShowItem(self, ibar = 1):
        return sq.wxsqltxt('Menu.db',"""select mitem.id,mitem.itemid,mitem.mbarid,mitem.itemname,mitem.handler
                                        from mitem
                                        where mitem.mbarid = %d
                                        """%ibar)
    
    def gItem( self, mbar = 1):
        return sq.wxsqltxt("Menu.db","""select mitem.itemname,mitem.itemid
                                        from mitem
                                        where mitem.mbarid = %d
                                        """%mbar)
                                      









        
class SetData:
    def __init__(self,send,data):
        self.send = send
        self.data = data

    def Additem(self,send,data):
        return sq.wxsqins('Menu.db','mitem',send,data)
    def Additem2(self,send,data):
        return sq.wxsqins2('Menu.db','mitem',send,data)
    
        
        
