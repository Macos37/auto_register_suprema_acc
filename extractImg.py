import cv2
from PIL import Image
import time
import pytesseract as tess

from start_emu import Emulator

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path_screen = r'C:\XuanZhi\register_cmd\screencap'

path_country_img = r'C:\XuanZhi\register_cmd\screencap\brl_v2.png'
screenshot = r'C:\XuanZhi\register_cmd\screencap\screen.png'

class ExtractEmu(Emulator):
    
    def __init__(self, name) -> None:
        super().__init__(name)

    def screen_cap(self):
        super().adb_cmd('shell screencap -p /sdcard/screen.png',0.5)
        super().adb_cmd(f'pull /sdcard/screen.png {path_screen}',0)
        super().adb_cmd('shell rm /sdcard/screen.png',0)


    def check_img_brl(self):
        template = cv2.imread(path_country_img)
        template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
        template_w,template_h = template_gray.shape[::-1]
        x,y,w,h = 537,690,537,690 #coord brl pic
        flag_a = False
        while not flag_a:
            super().adb_cmd('shell input swipe 280 680 280 119 1000')
            self.screen_cap()
            img = cv2.imread(screenshot)
            flag_b = False
            while not flag_b:
                img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                result = cv2.matchTemplate(
                    image = img_gray,
                    templ= template_gray,
                    method=cv2.TM_CCOEFF_NORMED
                )
                min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

                if max_val >= 0.99:
                    x = max_loc[0]
                    y = max_loc[1]
                    flag_b = True
                    flag_a = True
                    return x,y
                else:
                    break

    def check_img(self,pic):
        template = cv2.imread(pic)
        template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
        flag_a = False
        while not flag_a:
            self.screencap()
            img = cv2.imread(screenshot)
            flag_b = False
            while not flag_b:
                img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                result = cv2.matchTemplate(
                    image = img_gray,
                    templ= template_gray,
                    method=cv2.TM_CCOEFF_NORMED
                )
                min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
                if max_val >= 0.99:
                    flag_b = True
                    flag_a = True
                    return True
                else:
                    return False

    def search_text(self,text:str,coord_img:tuple):
        self.screen_cap()
        images = cv2.imread(screenshot)
        gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU |
                                                cv2.THRESH_BINARY_INV)
        cv2.imwrite(screenshot,thresh1)
        result = Image.open(screenshot)
            
        img_obj = result.crop(coord_img)
        text_obj = tess.image_to_string(img_obj,lang='eng',
                                config='--psm 10 --oem 3')

        if text in text_obj:
            return True
        else:
            return False


        




# def converted(file):
#     vidcap = cv2.VideoCapture(file)
#     def getFrame(sec):
#         vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
#         hasFrames,image = vidcap.read()
#         if hasFrames:
#             cv2.imwrite(path_screen + 'screen.png', image)
#         return hasFrames
#     sec = 0
#     frameRate = 1
#     count=0
#     success = getFrame(sec)
#     while success:
#         count = count + 1
#         sec = sec + frameRate
#         sec = round(sec, 1)
#         success = getFrame(sec)

# def screen_cap(name):
#     try:
#         adb_cmd('shell screenrecord --time-limit=1 /sdcard/emuwin.mp4', name)
#         adb_cmd(f'pull /sdcard/emuwin.mp4 {path_screen}', name)
#         adb_cmd('shell rm /sdcard/emuwin.mp4',name)
#         path_scr = 'C:\\XuanZhi\\register_cmd\\screencap\\emuwin.mp4'
#         converted(path_scr)
#         os.remove(path_scr)
#     except RuntimeError as a:
#         print(a)