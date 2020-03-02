import zipfile
import numpy as np

zippath='C:\\Users\\MSI\\Desktop\\攻防\\资料2\\zip.zip'
wordpath='C:\\Users\\MSI\\Desktop\\攻防\\资料2\\password.txt'
newpath='C:\\Users\\MSI\\Desktop\\攻防\\资料2\\password1.txt'

def replas():        #修改文件格式
    f=open(wordpath,'r')
    new=open(newpath,'w')
    word=f.read()
    word=word.replace('\n','    ')
    new.write(word)
    f.close()
    new.close()

replas()
f=open(newpath,'r')
zf = zipfile.ZipFile(zippath, "r")
i=1
while True:
    try:
        tmp=f.read(12)
        tmp=tmp[:8].encode(encoding='UTF-8', errors='strict')
        zf.extractall(pwd=tmp)
    except:
        pass
    else:
        print('password:'+tmp.decode())
        break
