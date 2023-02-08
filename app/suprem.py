import datetime
import subprocess

from main import emu
from coord_icon_items import coordinates_button

reg_now = r'C:\XuanZhi\register_cmd\registered.txt'
reg_not_now = r'C:\XuanZhi\register_cmd\not_registered.txt'

def login_passwd():

    with open(reg_not_now, 'r') as f:
        lines = f.readlines()
        login = lines[0].split()[0]
        passwrd = lines[0].split()[1]       
    with open(reg_now,'a+') as f:
        date_time = datetime.now()
        f.write('====REGISTRATED USERS======' + str(date_time) + '\n')
        f.write(login + '\t' + passwrd + '\n')
    with open(reg_not_now, 'w') as f:
        f.writelines(lines[1:])
    return login,passwrd


def suprema_poker():
    
    emu.adb_cmd('push C:\suprema.apk /sdcard/')
    print('Install Suprema Poker...')
    emu.adb_cmd('shell pm install /sdcard/suprema.apk')
    print('Start app Suprema Poker')
    emu.adb_cmd('shell am start -n com.opt.supremapoker/org.cocos2dx.javascript.AppActivity',sleep=10)
    


def login_acc():
    nickname = login_passwd()
    while True:
        if not emu.search_text('Register',coordinates_button['Register']):
            continue
        break
    print('Register Account ... ')
    list_command = ['shell input tap 239 525','shell input tap 183 308',f'shell input text {nickname[0]}',
                    'shell input tap 204 405',f'shell input text {nickname[1]}','shell input tap 224 497',
                    f'shell input text {nickname[1]}','shell input tap 239 600']
    for acc in list_command:
        emu.adb_cmd(acc)

# List command
# 0 button 'Register'
# 1 letter Username
# 2 enter New nickname
# 3 letter  New password
# 4 enter New passwrd
# 5 letter  re-enter password
# 6 button Register(END)
    print('Register done. exit..')