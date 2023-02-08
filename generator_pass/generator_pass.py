from ntpath import join
import random
import string

path_w_file ='C:\\XuanZhi\\register_cmd\\generator_pass\\nick_and_pass.txt'

c_up = string.ascii_uppercase
c_low = string.ascii_lowercase
c_letter = string.ascii_letters
digit = string.digits

all = c_up + c_low  + digit

for i in range(500):
    temp = random.sample(all,5)
    temp1 = random.sample(all,8)
    password = f'{random.randint(0,9)}'.join(temp)
    nickname = ''.join(temp1)
    f = open(path_w_file,'a')
    f.write(nickname + '\t' + password + '\n')
    f.close()



