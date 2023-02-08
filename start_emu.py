import subprocess
import time


path_ldcon = 'C:\\XuanZhi\\LDPlayer\\ldconsole.exe'
path_adb = 'C:\\XuanZhi\\LDPlayer\\adb.exe'

class Emulator:
    
    def __init__(self,name) -> None:
        self.name = name
        
        
    @staticmethod
    def list_vms():
        t = {}
        l = subprocess.check_output([path_ldcon, 'list2'],text=True).splitlines()
        for i in l:
            arrs = i.split(',')
            t[arrs[1]] = {'index': int(arrs[0]), 'pid': int(arrs[(-2)])}
        return t



    def adb_cmd(self, cmd:str, sleep = 4):
        time.sleep(sleep)
        out = subprocess.check_output([path_ldcon, 'adb', '--name', self.name, '--command', cmd])
        return out

    def wait_device(self):
            out = subprocess.check_output([path_ldcon, 'shell', '--name', self.name, '--command', "echo 'LOADED'"])
            if 'LOADED' in str(out):
                print('Emulator Loaded +++')
                return True
            return False


    def creat_emu(self):
        output = None
        try:
            subprocess.check_output([path_ldcon, 'copy', '--name', self.name, '--from', 'matka'])
            print('Emulator created +++')
            return True
        except subprocess.CalledProcessError as a:
            output = a.output
            
    def disconnect_dev(self):
        subprocess.check_output([path_ldcon, 'quit', '--name', self.name])
        time.sleep(10)
        off_dev = subprocess.check_output([path_adb, 'devices']).decode('UTF-8').splitlines()
        for i in off_dev:
            if i.startswith('127.0.0.1') and i.endswith('offline'):
                dev = i.split('\t')[0]
                subprocess.check_output([path_adb, 'disconnect', dev])
                time.sleep(10)
                subprocess.check_output([path_ldcon, 'remove', '--name', self.name])
        return True
    
    def remove_dev(self):
        subprocess.check_output([path_ldcon, 'remove', '--name', self.name])
        print('removed old matka')


    def launch_dev(self):
        while not self.wait_device():
            start = self.creat_emu()
            if start:
                subprocess.check_output([path_ldcon, 'launch', '--name', self.name])
            else:
                time.sleep(5)
            

