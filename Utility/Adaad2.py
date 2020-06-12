# -*- coding: utf-8 -*-
#In the name of God
#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import codecs
import unicodedata 
import string

MAX = 1000000000000000
MIN = 1
Dste = 1000
#C = 4

from Config.Init import *

abjad = {u'ا':1,u'ب':2,u'ج':3,u'د':4,u'ه':5,u'و':6,u'ز':7,u'ح':8,u'ط':9,
        u'ي':10,u'ک':20,u'ل':30,u'م':40,u'ن':50,u'س':60,u'ع':70,u'ف':80,u'ص':90,
        u'ق':100,u'ر':200,u'ش':300,u'ت':400,u'ث':500,u'خ':600,u'ذ':700,u'ض':800,u'ظ':900,
        u'غ':1000,u'ی':10}

Sdays = [u'شنبه',u'يکشنبه',u'دوشنبه',u'سه شنبه',u'چهارشنبه',u'پنجشنبه',u'جمعه']
Smonth = [u'فروردين',u'ارديبهشت',u'خرداد',u'تير',u'مرداد',u'شهريور',
          u'مهر',u'آبان',u'آذر',u'دي',u'بهمن',u'اسفند']

class Adaad:
    def __init__(self, num , txt):
        self.num = num
        self.txt = txt
        self.mytxt = ''
        self.mynum = 0
        self.t = loadadadha()



    def chkDst(self,num , C):
        if C < 0:
            return num
        else:
            return self.chkDst(num%(MAX/Dste),C-1)

    def YektaSad(self,num,txt=''):
        mtxt = ''
        if num > Dste or num < MIN:
            return mtxt
        
        if num < 10 and num > 0:
            return mtxt + self.t.yekan[num]
        if num < 20 and num >= 10 :
            mtxt = mtxt + self.t.dah1[num%10]
            if num  == 10:
                return mtxt 
            else:
                return mtxt + self.t.dah1[0]
            
        if num < 100 and num >= 20 :
            mtxt = mtxt + self.t.dah2[num//10]
            if num % 10 == 0 :
                return mtxt  + self.YektaSad(num%10)
            else:
                return mtxt  + self.t.dah2[0] + self.YektaSad(num%10)
            
        if num < 1000 and num >= 100 :
            if num // 100 == 2 :
                mtxt = mtxt + self.t.sadha[2]
                if num % 100 == 0 :
                    return mtxt 
                else:
                    return mtxt  + self.t.dah2[0] + self.YektaSad(num%100)
            else:
                mtxt = mtxt + self.t.sadha[num//100] + self.t.sadha[0]
                if num % 100 == 0 :
                    return mtxt  + self.YektaSad(num%100)
                else:
                    return mtxt  + self.t.dah2[0] + self.YektaSad(num%100)
                
        return mtxt            
            


    def num2txt(self,num,SBT=MAX):
        mtxt = ''
        
        if num > MAX or num < MIN :
            return mtxt
        elif num // SBT > 0:
            #print SBT
            mtxt = mtxt + self.YektaSad(num//SBT)+' '+self.t.farsi(SBT)
            if num%SBT != 0:
                mtxt = mtxt + self.t.dah2[0]
                
        else:
            if num < Dste :
                return mtxt + self.YektaSad(num)
                     
        return mtxt + self.num2txt(num%SBT,SBT/Dste)   

    def Shifnum(self, num , sh):
        return num / (sh*10)

    def Ril2Tmn(self, num):
        return num / 10
    def Tmn2Ril(self, num):
        return num * 10

    def abjad(self, txt):
        num = 0
        for ch in txt:
            #print unichr(ord(ch))
            if unichr(ord(ch)) in abjad:
                #print num,
                num = num + abjad[unichr(ord(ch))]
        return num

    def txt2num(self, txt):
        #number = 0
        self.n = loadhroof()
        sp = txt.split(' ')
        #print sp,len(sp)
        if len(txt) < 2:
            number = 0
            return 0
        elif len(sp) == 1:
            number = self.checktxt(sp[0])
            return self.checktxt(sp[0])
        else:
            for t in sp:
                if t == u'و':
                    number = number + 0
                    
                if t in self.n.hezar.keys():
                    number = number * self.n.hezar[t]
            return number 
                

    def cntrltxt(self,num , txt):
        pass
    
    def Digigrop(self,num , ch ):
        mtxt = ''
        if num == None:
            num = 0
        if num > MAX :
            return mtxt
        elif num < 0 :
            mtxt = '-' 
            return mtxt + self.Digigrop(abs(num),ch)
        elif num // Dste > 0:
            mtxt = mtxt + ch +  self.ykTsd(num%Dste) 
            return self.Digigrop(num//Dste,ch) + mtxt
        else:
            mtxt = self.e2f(unicode(num))
            return mtxt
       
    def ykTsd(self,num):
        if num == 0:
            return self.e2f(unicode(0))*3
        else:
            return self.e2f(unicode(num//100))+self.e2f(unicode((num%100)/10))+self.e2f(unicode((num%100)%10))
        
    def e2f(self,number):
                s = ''
                adadha = {u'0':1632 , u'1':1633 ,u'2':1634 , u'3':1635 , u'4':1636 ,u'5':1637 ,u'6':1638 ,u'7':1639 ,u'8':1640 ,u'9':1641 }
                #numrha = {0:1632 ,1:1633 ,2:1634 ,3:1635 ,4:1636 ,5:1637 ,6:1638 ,7:1639 ,8:1640 ,9:1641 }
                
                num = unicode(int(number))
                for c in num:
                        if c in string.digits:
                            s = s + unichr(adadha[c])
                        else:
                            s = s + c
                #print s
                return s
    def e2f2(self,number):
                s = ''
                adadha = {u'0':1632 , u'1':1633 ,u'2':1634 , u'3':1635 , u'4':1636 ,u'5':1637 ,u'6':1638 ,u'7':1639 ,u'8':1640 ,u'9':1641 }
                #numrha = {0:1632 ,1:1633 ,2:1634 ,3:1635 ,4:1636 ,5:1637 ,6:1638 ,7:1639 ,8:1640 ,9:1641 }
                
                num = unicode(number)
                for c in num:
                        if c in string.digits:
                            s = s + unichr(adadha[c])
                        else:
                            s = s + c
                #print s
                return s        
    def n2f(self,number):
                s = ''
                adadha = {u'0':1632 , u'1':1633 ,u'2':1634 , u'3':1635 , u'4':1636 ,u'5':1637 ,u'6':1638 ,u'7':1639 ,u'8':1640 ,u'9':1641 }
                #numrha = {0:1632 ,1:1633 ,2:1634 ,3:1635 ,4:1636 ,5:1637 ,6:1638 ,7:1639 ,8:1640 ,9:1641 }
                #num = unicode(number)
                num = unicode(int(number)/100)+unicode((int(number)/10)%10)+unicode(int(number)%10)
                for c in num:
                        #print c
                        s = s + unichr(adadha[c])
                #print s
                return s        

    def f2e(self,number):
                s = ''
                #adadha = {u'1632':u'0' , u'1633':u'1' ,u'1634':u'2' , u'1635':u'3' , u'1636':u'4' ,u'1637':u'5' ,u'1638':u'6' ,u'1639':u'7' ,u'1640':u'8' ,u'1641':u'9' }
                adadha = {u'\u0660':48 , u'\u0661':49 ,u'\u0662':50 , u'\u0663':51 , u'\u0664':52 ,u'\u0665':53
                          ,u'\u0666':54 ,u'\u0667':55 ,u'\u0668':56 ,u'\u0669':57
                          ,u'0':48,u'1':49,u'2':50,u'3':51,u'4':52,u'5':53,u'6':54,u'7':55,u'8':56,u'9':57}

                num = unicode(number)
                for c in num:
                        if c in adadha.keys():
                            #print c
                            s = s + chr(adadha[c])
                        else:
                            s = s
                #print s
                return s
            
    def k2e(self,number):
                s = ''
                #adadha = {u'1632':u'0' , u'1633':u'1' ,u'1634':u'2' , u'1635':u'3' , u'1636':u'4' ,u'1637':u'5' ,u'1638':u'6' ,u'1639':u'7' ,u'1640':u'8' ,u'1641':u'9' }
                adadha = {48:u'\u0660',49:u'\u0661',50:u'\u0662',51:u'\u0663',52:u'\u0664',53:u'\u0665'
                          ,54:u'\u0666',55:u'\u0667' ,56:u'\u0668' ,57:u'\u0669' 
                          ,324:u'\u0660',325:u'\u0661',326:u'\u0662',327:u'\u0663',328:u'\u0664',329:u'\u0665'
                          ,330:u'\u0666',331:u'\u0667' ,332:u'\u0668' ,333:u'\u0669' }
                #print type(number)
                if number in adadha :
                    s = s + adadha[number]
                
                else:
                    s = s
                #print s
                return s               


    def checktxt(self, txt):
        if txt == u'ده':
            return self.n.dah2[txt]
        if u'ده' in txt:
            txt.split(u'ده')
            return self.n.dah1[txt.split(u'ده')[0]]
        if u'صد' in txt:
            txt.split(u'صد')
            return self.n.sadha[txt.split(u'صد')[0]]
        if u'هزار' in txt:
            return self.n.hezar.values()[0]
        if u'ميليون' in txt:
            return self.n.milyoon.values()[0]
        if u'ميليارد' in txt:
            return self.n.milyard.values()[0]
        if u'تريليون' in txt:
            return self.n.trilyoon.values()[0]
        if txt in self.n.yekan.keys():
            return self.n.yekan[txt]
        if txt in self.n.dah2.keys():
            return self.n.dah2[txt]
        return 0
            
    def cntrol_fasele(self, txt):
        pass

    def error_massage(self , n):
        pass

    def Date2txt(self, txt):
        Date = txt.split(u'/')
        itxt = ''
        if int(Date[2]) == 3 :
            Rabt = u'سوم'
            itxt = Rabt
        elif int(Date[2])==23:
            Rabt = u'بيست و سوم'
            itxt = Rabt
        elif int(Date[2])==30:
            Rabt = u' ام'
            itxt = self.num2txt(int(Date[2]))+Rabt
        else:
            Rabt = u'م'
            itxt = self.num2txt(int(Date[2]))+Rabt
        
        itxt = itxt + ' '+Smonth[int(Date[1])-1]+u' '+u'ماه'
        itxt = itxt + ' '+self.num2txt(int(Date[0]))
        
        return itxt

    def Valid_input(self, txt):
        pass
    def Rondtxtnum(self,txt):
        #print txt
        if '.' in txt:
            itxt = txt.split('.')
        else:
            return txt
        #print itxt
        result = ''
        if int(itxt[1][0])>5:
            t = int(itxt[0][-1])+1
            result = itxt[0][:-1]+str(t)
        else:
            result = itxt[0]
        return  result
    def Nxthex(self,xn):
        return hex(int(float.fromhex(xn)+1))
    def txt2hex2(self,s):
        i = 1
        result = 0
        
        for ch in s.strip(' '):
            result = result + ord(ch) * (i)
            if i > 7:
                i = 1
            i = i + 1
            
        return '{0:X}'.format(result)    
    


class loadadadha(object):
    def __init__(self,file_name=UTILITY_PATH+"adadfa1"):
        f = codecs.open(file_name,mode='r',encoding='utf-8')

        lines = f.readlines()
        f.close()

        self.yekan = []
        self.dah1 = []
        self.dah2 = []
        self.sadha = []
        
        for i in range(10):
            self.yekan.append(lines[i+1].rstrip('\r\n'))
            if i == 0:
                self.dah1.append(lines[11].rstrip('\r\n'))
                self.dah2.append(u' و ')
            elif i == 1:
                self.dah1.append(lines[12].rstrip('\r\n'))
                self.dah2.append(lines[11].rstrip('\r\n'))
            else:
                self.dah1.append(lines[i+11].rstrip('\r\n'))
                self.dah2.append(lines[i+19].rstrip('\r\n'))

        for i in range(10):
            if i == 0:
                self.sadha.append(lines[29].rstrip('\r\n'))
            elif i == 2:
                self.sadha.append(lines[30].rstrip('\r\n'))
            elif i == 3:
                self.sadha.append(lines[22].rstrip('\r\n'))
            elif i == 5:
                self.sadha.append(lines[31].rstrip('\r\n'))
            else:
                self.sadha.append(lines[i+1].rstrip('\r\n'))

        self.hezar =lines[32].rstrip('\r\n')
        self.milyoon = lines[33].rstrip('\r\n')
        self.milyard = lines[34].rstrip('\r\n')
        self.trilyoon = lines[35].rstrip('\r\n')
    def farsi(self,SA):
        if SA == 1000:
            return self.hezar
        elif SA == 1000000:
            return self.milyoon
        elif SA == 1000000000:
            return self.milyard
        elif SA == 1000000000000:
            return self.trilyoon
        else:
            return ''
        return ''
    
class loadhroof(object):
    def __init__(self,file_name=UTILITY_PATH+"adadfa1"):
        f = codecs.open(file_name,mode='r',encoding='utf-8')

        lines = f.readlines()
        f.close()

        self.yekan = {}
        self.dah1 = {}
        self.dah2 = {}
        self.sadha = {}
        for i in range(10):
            self.yekan[lines[i+1].rstrip('\r\n')]=i
            if i == 0:
                self.dah1[lines[11].rstrip('\r\n')]=i+10
                self.dah2['و'] = 0
            elif i == 1:
                self.dah1[lines[12].rstrip('\r\n')] = i+10
                self.dah2[lines[11].rstrip('\r\n')] = i*10
            else:
                self.dah1[lines[i+11].rstrip('\r\n')]= i+10
                self.dah2[lines[i+19].rstrip('\r\n')]= i*10

        for i in range(10):
            if i == 0:
                self.sadha[lines[29].rstrip('\r\n')]= 100
            elif i == 2:
                self.sadha[lines[30].rstrip('\r\n')]= i*100
            elif i == 3:
                self.sadha[lines[22].rstrip('\r\n')]= i*100
            elif i == 5:
                self.sadha[lines[31].rstrip('\r\n')]= i*100
            else:
                self.sadha[lines[i+1].rstrip('\r\n')]= i*100

        self.hezar = {lines[32].rstrip('\r\n'):1000}
        self.milyoon = {lines[33].rstrip('\r\n'):1000000}
        self.milyard = {lines[34].rstrip('\r\n'):1000000000}
        self.trilyoon = {lines[35].rstrip('\r\n'):1000000000000}


        '''
        def checkme(s):
            if s in milyard:
                if 'و' in s:
                    return milyard.key()
            elif SA == 1000000:
                return milyoon
            elif SA == 1000000000:
                return milyard
            else:
                return ''
            return ''
        '''


        
        

        
        
