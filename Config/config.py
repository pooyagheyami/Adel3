# -*- coding: cp1256 -*-
#In the name of God
# -*- coding: utf-8 -*- 

import sys
import codecs
import os
from  Config.Init import *
from wx import MessageBox,OK,ICON_WARNING,ICON_INFORMATION

#from khayyam import *
import Database.MDataGet as DG

def BaseCheck():
    #Check Main file is
    try:
        s = os.fstat(os.open(DATABASE_PATH+'Main.db',os.O_RDONLY))
        #print 'ok'
    except:
        
        MessageBox(u'بانک اطلاعاتي پيدا نمي شود يا تخريب شده به بخش بازيابي اطلاعات برويد',u'خطا',OK | ICON_WARNING)
    finally:
        ichk = DG.GetData(u'',u'')
        Dcheck = ichk.gCmpny()
        
        #print Dcheck
        if Dcheck == []:
            #Startpro()
            return ['','']
        else:
            irev = ichk.lsrev(Dcheck[0][0])
            #print irev
            #lrev = []
            #for i in range(len(irev)):
            #    lrev.append(irev[i][0])
            #Checkdatatime(Dcheck,now)
            return [Dcheck[0][1],irev[0][0]]
       


def Startpro():
    f = codecs.open(CONFIG_PATH+'file1.txt',mode='r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    txt = ''
    for t in range(len(lines)):
            txt = txt + '\n' + lines[t]
    #print txt
    return txt
'''

def Checkdatatime(date,now):
    if date[0][0] == now:
        print 'yes'
        return 11
    else:
        print 'no'
        return 12
'''        
    
def Getprogini():
    f = codecs.open(CONFIG_PATH+'program.ini',mode='r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    parametr = []
    for t in range(len(lines)):
        #print lines[t][:3]
        if lines[t][:3]=='rps':
            parametr.append(lines[t][6:7])
        if lines[t][:3]=='sps':
            parametr.append(lines[t][6:7])
        if lines[t][:3]=='cps':
            parametr.append(lines[t][6:7])    
        if lines[t][:3]=='bps':
            parametr.append(lines[t][6:7])
        if lines[t][:3]=='tps':
            parametr.append(lines[t][6:7])    
        if lines[t][:3]=='BGF':
            #print lines[t][6:].split('\r')
            parametr.append(lines[t][6:].split('\r')[0])


    #print parametr
    return parametr
