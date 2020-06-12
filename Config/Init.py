#In the name of God

import sys
import os
import random
import codecs
import string
from khayyam import *

from wx import MessageBox,OK,ICON_WARNING,ICON_INFORMATION

NOW = JalaliDatetime.now().strftime('%N/%P/%K')
MAP = os.getcwd()

if MAP.find(u'\\') > 0:
    SLASH = u'\\'
else:
    SLASH = u'/'
    


def opj(path):
    """Convert paths to the platform-specific separator"""
    st = apply(os.path.join, tuple(path.split('/')))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        st = '/' + st
    #print st    
    return st



DATABASE_PATH = os.path.join(MAP,opj(u'Database')+SLASH)

GUI_PATH      = os.path.join(MAP,opj(u'GUI')+SLASH)
RES_PATH      = os.path.join(MAP,opj(u'Res')+SLASH)

ICONS_PATH    = os.path.join(RES_PATH,opj(u'Icons')+SLASH)
PICS_PATH     = os.path.join(RES_PATH,opj(u'Pics')+SLASH)
SPALSH_PATH   = os.path.join(RES_PATH,opj(u'Splash')+SLASH)

UTILITY_PATH  = os.path.join(MAP,opj(u'Utility')+SLASH)
CONFIG_PATH   = os.path.join(MAP,opj(u'Config')+SLASH)
LOGS_PATH     = os.path.join(MAP,opj(u'Logs')+SLASH)

TEMPS_PATH    = os.path.join(MAP,opj(u'Temps')+SLASH)

GUI_HELP      = os.path.join(GUI_PATH,opj(u'Help')+SLASH)


def thistxt(filename):
    f = codecs.open(LOGS_PATH+filename,mode='r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    txt = ''
    for t in range(len(lines)):
            txt = txt + '\n' + lines[t]
    #print txt
    return txt

FONT_SIZE = 12
FONT_TYPE = "Arial"
T = True
F = False
SIZE = (1024,768)
StringLetter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\x81\x83\x8a\x8c\x8d\x8e\x8f\x90\x98\x9a\x9c\x9f\xaa\xb5\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd8\xd9\xda\xdb\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf8\xf9\xfa\xfb\xfc\xff'


def getregkey():
    access = win32con.KEY_READ | win32con.KEY_ENUMERATE_SUB_KEYS | win32con.KEY_QUERY_VALUE
    keypath = "SYSTEM\\CurrentControlSet\\Services\\disk\\Enum"

    try:
        hkey = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,keypath,0,access)
    except Exception , e:
        MessageBox(e,u'error',OK | ICON_WARNING)
        return ''

    i = win32api.RegQueryValueEx(hkey,'Count')[0]
    for l in range(int(i)):
        srialit =  win32api.RegQueryValueEx(hkey,str(l))[0].split('\\')[-1]


