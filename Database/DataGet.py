#In The name of God
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

import wxsq2 as sq


class GetData:
    def __init__(self,send,gets):
        self.send = send
        self.gets = gets

    def ShowDoc(self,date = u''):
        return sq.wxsqltxt('Main.db',"""select distinct Document.date,Document.no,Account.name,Descript.Descrpt,Document.Cr,Document.Dr
                                        from Document,Descript,Account
                                        where Document.date = '%s'
                                        and Document.Acc = Account.Acc
                                        and Document.Des = Descript.Des
                                        """%date )
    def ShwDoc(self,num = u''):
        return sq.wxsqltxt('Main.db',"""select distinct Document.no,Document.date,Document.Acc,Account.name,Descript.Descrpt,Document.Cr,Document.Dr
                                        from Document,Descript,Account
                                        where Document.no = '%s'
                                        and Document.Acc = Account.Acc
                                        and Document.Des = Descript.Des
                                        order by Document.Cr desc """%num)
    
    def ShwBil(self,code = u''):
        return sq.wxsqltxt('Main.db',"""select distinct Document.no,Document.date,Document.Cr,Document.Dr
                                        from Document
                                        where Document.Acc = '%s' """%code)
    def ShwBil2(self,code = u'',no = u''):
        return sq.wxsqltxt('Main.db',"""select distinct Document.no,Document.date,Document.Cr,Document.Dr
                                        from Document
                                        where Document.Acc = '%s'
                                        and Document.no = '%s'  """%(code,no))
    def SumBil(self,code = u''):
        return sq.wxsqltxt('Main.db',"""select distinct Document.Acc,Account.name,sum(Document.Cr),sum(Document.Dr)
                                        from Document,Account
                                        where Document.Acc = '%s'
                                        and Document.Acc = Account.Acc  """%code)
    
    def ShwKol(self,code = u''):
        return sq.wxsqltxt('Main.db',"""select distinct Document.no,Document.date,Account.name,Document.Cr,Document.Dr
                                        from Document,Account
                                        where substr( Document.Acc,1,2) = '%s'
                                        and Document.Acc = Account.Acc
                                        """%code)
    def ShwKol2(self,code = u'',no = u''):
        return sq.wxsqltxt('Main.db',"""select distinct Document.no,Document.date,Account.name,Document.Cr,Document.Dr
                                        from Document,Account
                                        where substr( Document.Acc,1,2) = '%s'
                                        and Document.Acc = Account.Acc
                                        and Document.no = '%s' """%(code,no))

    def RowDoc(self):
        return sq.wxsqsel('Main.db','Document',' no ')
    def toDDoc(self,date = u''):
        return sq.wxsqltxt('Main.db',"""select distinct Descript.Descrpt,Document.date,Document.no
                                         from Document,Descript
                                         where Document.date <= '%s'
                                         and Document.Des = Descript.Des
                                         order by Document.date """%date )
    def ShwAcc(self):
        return sq.wxsqsel('Main.db','Account')
    def gDesCd(self,num = u''):
        return sq.wxsqsnd('Main.db','Document','Des','no',num)
    def ShwGrp(self,code = u''):
        return sq.wxsqsnd('Main.db','Account','Acg','Acc',code)
    def BakGrp(self,code = u''):
        return sq.wxsqsnd('Main.db','Account','Acc','Acg',code)
    def ShwSpc(self,code = u''):
        return sq.wxsqsnd('Main.db','Account','Spc','Acc',code)
    def gTitSp(self,code = u''):
        return sq.wxsqsnd('Main.db','Specify','tit','Spc',code)
    def gLstac(self,code = u''):
        return sq.wxsqltxt('Main.db',"""select Account.Acc
                                        from Account
                                        where Account.Acg = '%s'
                                        """%code )
    def gCmpny(self):
        return sq.wxsqsel('Main.db','Company')
    
    def gLstRv(self,code = u''):
        return sq.wxsqltxt('Main.db',"""select distinct Revenue.Reven,Company.Dir
                                        from Company,Revenue
                                        where Revenue.Rev = Company.Rev
                                        and Company.id = '%s'"""%code)
    def gRevnu(self,code = u''):
        return sq.wxsqltxt('Main.db',"""select Revenue.Reven ,Revenue.fdate,Revenue.ldate
                                        from Revenue
                                        where Revenue.Rev = '%s'"""%code)
    def gRevnm(self,name = u''):
        return sq.wxsqltxt('Main.db',"""select Revenue.Reven ,Revenue.fdate,Revenue.ldate
                                        from Revenue
                                        where Revenue.Reven = '%s'"""%name)
    def gKlist(self):
        return sq.wxsqsel('Main.db','Accgroup')
    def gKcods(self,name = u''):
        return sq.wxsqseld('Main.db',"Accgroup"," cod1 , cod2 "," name = '%s' "%name)
    
    def gSpcy(self,code = u''):
        return sq.wxsqltxt('Main.db',""" select Specify.Spcfy,Titels.titel,Specify.tit
                                         from Specify,Titels
                                         where Specify.Spc = '%s'
                                         and Specify.tit = Titels.tit """%code)
    def gTitel(self,tit = u''):
        return sq.wxsqseld('Main.db',"Titels"," titel , tit "," substr(Titels.tit,1,3) = '%s' "%tit)
    
    
    def gLBac(self):
        return sq.wxsqltxt('ABR.db',""" select distinct B.Rev,Backup.Bacfile,Backup.Bacdir,Backup.Bacdate,Backup.Bactime
                                        from B,Backup
                                        where B.Bac = Backup.Bac
                                    """)
    def gLRes(self):
        return sq.wxsqltxt('ABR.db',""" select distinct R.Rev,Restor.Resfile,Restor.Resdir,Restor.Resdate,Restor.Restime
                                        from R,Restor
                                        where R.Res = Restor.Res
                                    """)
    def lCom(self):
        return sq.wxsqsel('Company.db','Company')
    def lsrev(self,code=u''):
        return sq.wxsqltxt('Company.db',"""select distinct Revenue.Reven,Company.Dir
                                        from Company,Revenue
                                        where Revenue.Rev = Company.Rev
                                        and Company.id = '%s'"""%code)
        





class SetData:
    def __init__(self,send,data):
        self.send = send
        self.data = data
    def Incmpny(self,send,data):
        return sq.wxsqins('Main.db',send[0],send[1],data)
    def kinsert(self,send,data):
        return sq.wxsqins2('Main.db',send[0],send[1],data)
    def kdelall(self,send):
        return sq.wxsqdall('Main.db',send)
    def Specin(self,send,data):
        return sq.wxsqins('Main.db','Specify',send,data)
    def Specin2(self,send,data):
        return sq.wxsqins2('Main.db','Specify',send,data)
    def Specup(self,send,data):
        return sq.wxsqlup('Main.db','Specify',send,data)
    def Specup2(self,send,data):
        return sq.wxsqlup2('Main.db','Specify',send,data)
    def Accin2(self,send,data):
        return sq.wxsqins('Main.db','Account',send,data)
    def Accup2(self,send,data):
        return sq.wxsqlup('Main.db','Account',send,data)
    def Documnt(self,send,data):
        return sq.wxsqins('Main.db','Document',send,data)
    def Descrpt(self,send,data):
        return sq.wxsqins('Main.db','Descript',send,data)
    def Docupdt(self,send,data):
        return sq.wxsqlup('Main.db','Document',send,data)
    def Docupdt2(self,send,data):
        return sq.wxsqlup2('Main.db','Document',send,data)
    def Desupdt(self,send,data):
        return sq.wxsqlup('Main.db','Descript',send,data)
    def DeltDoc(self,data):
        return sq.wxsqdel('Main.db','Document',data)
    def DeltDes(self,data):
        return sq.wxsqdel('Main.db','Descript',data)

    def InBack(self,send,data):
        #sq.wxsqins('ABR.db','B',send,data)
        sq.wxsqins('ABR.db','Backup',send,data)
        return 1
    def InRest(self,send,data):
        #sq.wxsqins('ABR.db','R',send,data)
        sq.wxsqins('ABR.db','Restor',send,data)
        return 1
    def Incomp(self,send,data):
        sq.wxsqins('Company.db','Company',send[0],data[0])
        sq.wxsqins('Company.db','Revenue',send[1],data[1])
        return 1
        
