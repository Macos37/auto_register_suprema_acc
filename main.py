import time

from extractImg import ExtractEmu
from app import nord_vpn,nzt
from app.suprem import suprema_poker,login_acc

emu = ExtractEmu('matka-reg')


def main(num:int,interval:int):
    while num > 0:
        if emu.name in emu.list_vms():
            emu.remove_dev()
        
        emu.launch_dev()
        nord_vpn()
        print('Nord connected')
        nzt()
        print('NZT connected.!')
        suprema_poker()
        login_acc()
        time.sleep(15)
        emu.disconnect_dev()
        time.sleep(interval)
        num-=1

if __name__ == '__main__':
    interval= input('What is the registration interval between accounts?: ')
    num = input('How many accounts to register?: ')
    if num > 0 and interval > 0:
        main(num,interval)
    else:
        print('Number must be greater than 0')
