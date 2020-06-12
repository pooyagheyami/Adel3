#In The name of God
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

import wxsq2 as sq


class GetData:
    def __init__(self,send,gets):
        self.send = send
        self.gets = gets
        
        self.SQL3 = """select distinct Molks.Amunt2,Molks.M3,substr(MSpcify.Spcfy,1,1),Molks.M1,Molks.Addrss,
                       Mntgh.Aname,Molks.Mname,Mltype.Type,Molks.Mcode
                       from Molks
                       inner join Mntgh  on Molks.Area = Mntgh.Area 
		       inner join MSpcify  on Molks.MSpc = MSpcify.MSpc
		       inner join Mltype  on Molks.Mtype = Mltype.Mtype
		       """
        self.SQL31 = """select distinct Molks.Amunt1,Molks.M3,substr(MSpcify.Spcfy,1,1),Molks.M1,Molks.Addrss,
                       Mntgh.Aname,Molks.Mname,Mltype.Type,Molks.Mcode
                       from Molks
                       inner join Mntgh  on Molks.Area = Mntgh.Area 
		       inner join MSpcify  on Molks.MSpc = MSpcify.MSpc
		       inner join Mltype  on Molks.Mtype = Mltype.Mtype
		       """
        self.SQL32 = """select distinct Molks.Amunt2,Molks.Amunt1,substr(MSpcify.Spcfy,1,1),Molks.M1,Molks.Addrss,
                       Mntgh.Aname,Molks.Mname,Mltype.Type,Molks.Mcode
                       from Molks
                       inner join Mntgh  on Molks.Area = Mntgh.Area 
		       inner join MSpcify  on Molks.MSpc = MSpcify.MSpc
		       inner join Mltype  on Molks.Mtype = Mltype.Mtype
		       """
        self.SQL1 = """select distinct Molks.Amunt2,Molks.M3,substr(MSpcify.Spcfy,1,1),Molks.M1,Molks.Addrss,
                       Mntgh.Aname,Molks.Mname,Mltype.Type,Molks.Mcode,Respon.Resname
                       from Molks
                       inner join Mntgh  on Molks.Area = Mntgh.Area 
		       inner join Respon on Molks.Res = Respon.Res
		       inner join MSpcify  on Molks.MSpc = MSpcify.MSpc
		       inner join Mltype  on Molks.Mtype = Mltype.Mtype
                       """
        
        self.SQL4 = """select distinct Molks.Amunt2,Molks.Amunt1,substr(MSpcify.Spcfy,1,1),Molks.M3,Molks.M2
                       ,Molks.M1,Molks.Addrss,Mntgh.Aname,Molks.Mname,Molks.Mcode
                       from Molks
                       inner join Mntgh  on Molks.Area = Mntgh.Area 
		       inner join Respon on Molks.Res = Respon.Res
		       inner join MSpcify  on Molks.MSpc = MSpcify.MSpc
		       inner join Mltype  on Molks.Mtype = Mltype.Mtype
                       """   

        self.SQL2 = """select distinct Molks.Amunt2,Molks.Amunt1,Molks.M2,Molks.M1,Molks.Addrss,
                       Mntgh.Aname,Molks.Mname,Mltype.Type,Molks.Mcode,Respon.Resname
                       from Molks,Mntgh,Respon,Mltype
                       where Molks.Area = Mntgh.Area
                       and Molks.Res = Respon.Res
                       and Mltype.Mtype =Molks.Mtype """
    def gMolks(self):
        return sq.wxsqltxt('Molk.db',self.SQL2) 
    def gMolks2(self,newsql):
        sql = self.SQL2 + newsql
        return sq.wxsqltxt('Molk.db',sql)
    
    def Amlak(self):
        return sq.wxsqltxt('Molk.db',self.SQL1)
    def Amlak2(self,newsql = u''):
        return sq.wxsqltxt('Molk.db',self.SQL3+newsql)
    def Amlak21(self,newsql = u''):
        return sq.wxsqltxt('Molk.db',self.SQL31+newsql)
    def Amlak22(self,newsql = u''):
        return sq.wxsqltxt('Molk.db',self.SQL32+newsql)
    def Amlak4(self,newsql = u''):
        sql = self.SQL4 + newsql
        return sq.wxsqltxt('Molk.db',sql)
    def Amlak11(self,newsql):
        sql = self.SQL1 + newsql
        #print sql
        return sq.wxsqltxt('Molk.db',sql)
    
    def ShwMlks(self,code = u''):
        return sq.wxsqltxt('Molk.db',""" select * from Molks where Mcode = %s """%code)
    
    def ShwMlks2(self,code = u''):
        return sq.wxsqltxt('Molk.db',""" select Date,name,phone,Aname,Addrss,Mname,M1,M2,M3,M4,Spcfy,Amunt1,Amunt2,dscrpt
                                         from Molks
                                         inner join MSpcify  on Molks.MSpc = MSpcify.MSpc
                                         inner join Descript on Molks.des = Descript.des
                                         inner join Account on Molks.Acc = Account.Acc
                                         inner join Mntgh  on Molks.Area = Mntgh.Area 
                                         where Mcode = %s """%code)
    def ShwAcc(self):
        return sq.wxsqsel('Molk.db','Account')
    def ShwAcc2(self):
        return sq.wxsqltxt('Molk.db',""" select Account.Acc,Account.name,Account.phone,Respon.Resname
                                         from Account,Respon
                                         where Account.Res = Respon.Res
                                     """)
    def gAccod(self, code = u''):
        return sq.wxsqltxt('Molk.db',""" select Account.Acc,Account.name,Account.phone,Account.Spc
                                         from Account
                                         where Account.Acc = '%s'
                                     """%code)
    def gAccod2(self, code = u''):
        return sq.wxsqltxt('Molk.db',""" select *
                                         from Account
                                         where Account.Acc = '%s'
                                     """%code)    
        
    def ShwRac(self,code = u''):
        return sq.wxsqltxt('Molk.db',""" select *
                                         from Account
                                         where Res = %s 
                                     """%code)
    def ShwRes1(self):
        return sq.wxsqltxt('Molk.db',""" select *
                                         from Respon
                                         where substr(Res ,2,2) = '0' 
                                     """)
    def ShwRes2(self):
        return sq.wxsqltxt('Molk.db',""" select *
                                         from Respon
                                         where substr(Res ,1,1) >= '0'
                                         and substr(Res,2,1) = ''
                                     """)
    def glstMlk(self):
        return sq.wxsqltxt('Molk.db',""" select Mcode
                                         from Molks
                                         order by Mcode
                                     """)
    def gMCods(self,code = u''):
        return sq.wxsqltxt('Molk.db',""" select Molks.Acc,Molks.MSpc,Molks.des
                                         from Molks
                                         where Molks.Mcode = %s
                                     """%code)
    def gDes(self, cdes = u''):
        return sq.wxsqsnd('Molk.db','Descript','dscrpt','des',cdes)
    def gMSpc(self, code = u''):
        return sq.wxsqsnd('Molk.db','MSpcify','Spcfy','MSpc',code)

        
    def gMRes(self, name = u''):
        return sq.wxsqsnd('Molk.db','Respon','Res','Resname',name)
    def gCRes(self, code = u''):
        return sq.wxsqsnd('Molk.db','Respon','Resname','Res',code)
    def gMtyp(self, code = u''):
        return sq.wxsqsnd('Molk.db','Mltype','Type','Mtype',code)
    def glstA( self ):
        return sq.wxsqltxt('Molk.db',"""select Acc
                                        from Account
                                           """)
      
    def gAccn(self, name = u''):
        return sq.wxsqsnd('Molk.db','Account','Acc','name',name)
    def gAccd(self, code = u''):
        return sq.wxsqsnd('Molk.db','Account','name','Acc',code)
    def gAcsp(self, code = u''):
        return sq.wxsqsnd('Molk.db','Account','Spc','Acc',code)
    def gMltype(self):
        return sq.wxsqltxt('Molk.db',""" select Mltype.Mtype,Mltype.Type
                                          from Mltype
                                     """)
    
    def gMntgh(self):
        return sq.wxsqltxt('Molk.db',""" select Mntgh.Area,Mntgh.Aname
                                          from Mntgh
                                     """)
    def gMtgCk( self , name = u''):
        return sq.wxsqltxt('Molk.db',""" select Mntgh.Area,Mntgh.Aname
                                          from Mntgh
                                          where Mntgh.Aname = '%s'
                                     """%name)

    
    def gSpcy(self,code = u''):
        return sq.wxsqltxt('Molk.db',""" select Specify.Spcfy,titels.titel,Specify.tit
                                         from Specify,titels
                                         where Specify.Spc = '%s'
                                         and Specify.tit = titels.tit """%code)
    def gASpc(self,code=u''):
        return sq.wxsqltxt('Molk.db',""" select *
                                         from Specify
                                         where Specify.Spc = '%s' """%code)
    
    def gTitel(self,tit = u''):
        return sq.wxsqseld('Molk.db',"titels"," titel , tit "," substr(titels.tit,1,3) = '%s' "%tit)
    
    def gTitel2(self,tit = u''):
        return sq.wxsqseld('Molk.db',"titels"," titel , tit "," substr(titels.tit,1,3) = '%s' order by titels.tit "%tit)


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
    def gCmpny(self):
        return sq.wxsqsel('ABR.db','Company')
    def gReven(self):
        return sq.wxsqsel('ABR.db','Revenu')
    
    def lCom(self):
        return sq.wxsqsel('Company.db','Company')
    #def lsrev(self,code=u''):
    #    return sq.wxsqltxt('Company.db',"""select distinct Revenue.Reven,Company.Dir
    #                                    from Company,Revenue
    #                                    where Revenue.Rev = Company.Rev
    #                                    and Company.id = '%s'"""%code)
    def lsrev(self,code=u''):
        return sq.wxsqltxt('ABR.db',"""select distinct Revenu.Reven,Company.Dir
                                        from Company,Revenu
                                        where Revenu.Rev = Company.Rev
                                        and Company.id = '%s' """%code)
    def gAMntgh(self):
        return sq.wxsqltxt('Archive.db',""" select Mntgh.Area,Mntgh.Aname
                                          from Mntgh
                                     """)
    def gAMtgCk( self , name = u''):
        return sq.wxsqltxt('Archive.db',""" select Mntgh.Area,Mntgh.Aname
                                          from Mntgh
                                          where Mntgh.Aname = '%s'
                                     """%name)
    def gAlstMlk(self):
        return sq.wxsqltxt('Archive.db',""" select Mcode
                                         from Molks
                                         order by Mcode
                                     """)
    def gAAcod(self, code = u''):
        return sq.wxsqltxt('Archive.db',""" select Account.Acc,Account.name,Account.phone,Account.Spc
                                         from Account
                                         where Account.Acc = '%s'
                                     """%code)
        





class SetData:
    def __init__(self,send,data):
        self.send = send
        self.data = data

    def InMolk(self,send,data):
        sq.wxsqins('Molk.db','Molks',send,data)
    def InDes(self,send,data):
        sq.wxsqins('Molk.db','Descript',send,data)

    def UpMolk(self,send,data):
        sq.wxsqlup('Molk.db','Molks',send,data)
    def UpMolk2(self,send,data):
        sq.wxsqlup2('Molk.db','Molks',send,data)

    def UpDes(self,snd,data):
        sq.wxsqlup('Molk.db','Descript',snd,data)
    def UpDes2(self,snd,data):
        sq.wxsqlup2('Molk.db','Descript',snd,data)

    def Inmntg(self,send,data):
        sq.wxsqins('Molk.db','Mntgh',send,data)
    def Inmtyp(self,send,data):
        sq.wxsqins('Molk.db','Mltype',send,data)

    def Inmres(self,send,data):
        sq.wxsqins('Molk.db','Respon',send,data)
        
    def Inmspc(self,send,data):
        sq.wxsqins('Molk.db','MSpcify',send,data)
    def Upmspc(self,send,data):
        sq.wxsqlup('Molk.db','MSpcify',send,data)

    def Intit1(self,send,data):
        sq.wxsqins('Molk.db','titels',send,data)

    def InAcc(self,send,data):
        sq.wxsqins('Molk.db','Account',send,data)
    def UpAcc(self,send,data):
        sq.wxsqlup('Molk.db','Account',send,data)
    def UpAcc2(self,send,data):
        sq.wxsqlup2('Molk.db','Account',send,data)    
        
    def Specin(self,send,data):
        return sq.wxsqins('Molk.db','Specify',send,data)
    def Specin2(self,send,data):
        return sq.wxsqins2('Molk.db','Specify',send,data)
    def Specup(self,send,data):
        return sq.wxsqlup('Molk.db','Specify',send,data)
    def Specup2(self,send,data):
        return sq.wxsqlup2('Molk.db','Specify',send,data)

    def DelMolk(self,data):
        return sq.wxsqdel('Molk.db','Molks',data)
    def DelAcc(self,data):
        return sq.wxsqdel('Molk.db','Account',data)
    def DelMsp(self,data):
        return sq.wxsqdel('Molk.db','MSpcify',data)
    def DelDes(self,data):
        return sq.wxsqdel('Molk.db','Descript',data)
    def DelSpec(self,data):
        return sq.wxsqdel('Molk.db','Specify',data)
    


    def InBack(self,send,data):
        #sq.wxsqins('ABR.db','B',send,data)
        sq.wxsqins('ABR.db','Backup',send,data)
        return 1
    def InRest(self,send,data):
        #sq.wxsqins('ABR.db','R',send,data)
        sq.wxsqins('ABR.db','Restor',send,data)
        return 1
    def InABRc(self,send,data):
        sq.wxsqins('ABR.db','Company',send[0],data[0])
        sq.wxsqins('ABR.db','Revenu',send[1],data[1])
    def Incomp(self,send,data):
        sq.wxsqins('Company.db','Company',send[0],data[0])
        sq.wxsqins('Company.db','Revenue',send[1],data[1])
        return 1
    def InAmntg(self,send,data):
        sq.wxsqins('Archive.db','Mntgh',send,data)
    def InAAcc(self,send,data):
        sq.wxsqins('Archive.db','Account',send,data)
    def InAMolk(self,send,data):
        sq.wxsqins('Archive.db','Molks',send,data)
    def InAmspc(self,send,data):
        sq.wxsqins('Archive.db','MSpcify',send,data)    
    def InADes(self,send,data):
        sq.wxsqins('Archive.db','Descript',send,data)
        
    def ASpecin(self,send,data):
        return sq.wxsqins('Archive.db','Specify',send,data)
    def ASpecin2(self,send,data):
        return sq.wxsqins2('Archive.db','Specify',send,data)
    def ASpecup(self,send,data):
        return sq.wxsqlup('Archive.db','Specify',send,data)
    def ASpecup2(self,send,data):
        return sq.wxsqlup2('Archive.db','Specify',send,data)    
