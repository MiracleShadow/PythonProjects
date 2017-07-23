#用open创建文件
# fout = open ('oops.txt','wt')
# print('hello',file=fout)
# fout.close()

#用exists检查文件是否存在
#import os
#print(os.path.exists('oops.txt'))

#用isfile（）检查是否为文件**文件名要加后缀**
# name = 'oops.txt'
# print(os.path.isfile(name))#判断是不是文件
# print(os.path.isdir(name))#判断是否是目录
# print(os.path.isdir('.idea'))
# print(os.path.isabs('D:\Projects'))

#用copy()复制文件
# import shutil
# shutil.copy('oops.txt','ohno.txt')#自动建立了ohno文件
# shutil.move('ohno.txt','aatt.txt')#删除了原始文件

#用rename()重命名文件
# import os
# os.rename('aatt.txt','ohwell.txt')

#print('\n'.join([''.join([('TTybTTyb'[(x-y)%7]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

import os
os.makedirs(os.path.join("D:\\News"))
os.chdir(os.path.join("D:\\News"))  ##切换到目录
file=open('data.txt','w')
file.write('hello file world!\n')
file.write('Bye file world.\n')
file.close()
