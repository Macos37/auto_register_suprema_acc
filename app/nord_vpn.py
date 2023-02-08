from main import emu
from coord_icon_items import icon,coordinates_button,coordinates_text
import time


def nordvpn():
    print('Nord start')
    emu.adb_cmd('shell am start -n  com.nordvpn.android/.MainActivity')
    passwd = 'test9999'
    attemp = 5
    while attemp > 0:
        if emu.check_img(icon['login']):
            emu.adb_cmd('shell input tap 138 537')
            while True:
                if not emu.search_text('Choose an account',coordinates_text['coord_Choose']):
                    continue
                break
            emu.adb_cmd('shell input tap 160 385')
            time.sleep(10)
            if emu.search_text('Hi there!',coordinates_text['coord_Hithere']):
                emu.adb_cmd('shell input tap 118 455')
                emu.adb_cmd(f'shell input text {passwd}')
                emu.adb_cmd('shell input tap 186 523',sleep=5)
                break
            break
        attemp-=1
    emu.adb_cmd(f"shell input tap {coordinates_button['nord-X']}")
    x,y = emu.check_img_brl(icon['brazil_nord'])
    emu.adb_cmd(f'shell input tap {x} {y}')
    emu.adb_cmd(f'shell input tap {coordinates_button["nord_ok"]}')
    while True:
        if not emu.search_text('Connected to Brazil',coordinates_text['brl_coonect']):
            attemp1=3
            while attemp1 > 0:
                emu.adb_cmd('shell input swipe 277 100 277 620 1000')  # scroll swipe
                attemp1-=1
            continue         
        emu.adb_cmd(f'shell input keyevent 3')# tap BACK HOME
        break
    


