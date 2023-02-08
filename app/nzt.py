from main import emu
from coord_icon_items import icon

def nzt(name):
    emu.adb_cmd('shell am start -n  com.nztapk/z.adv.EntryActivity',sleep=10) # start app NZT POKER
    while True:
        if not emu.check_img(icon['start_nzt'],name):
            continue
        break
    scroll= 4
    while scroll > 0:
        emu.adb_cmd('shell input swipe 277 622 277 70 1000')  # scroll swipe UP
        scroll-=1
    
    emu.adb_cmd('shell input tap 395 230') # tap in NZT APP Suprema
    emu.adb_cmd('shell input keyevent KEYCODE_BACK') # tap BACK HOME
    
