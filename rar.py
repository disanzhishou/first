from unrar import rarfile

rarpath='C:\\Users\\MSI\\Desktop\\攻防\\YU\\zip\\password.rar'
wordpath='C:\\Users\\MSI\\Desktop\\攻防\\YU\\password.txt'
newpath='C:\\Users\\MSI\\Desktop\\攻防\\YU\\password1.txt'

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
rf = rarfile.RarFile(rarpath,'r')
while True:
    try:
        tmp=f.read(12)
        tmp=tmp[:8]
        rf.setpassword(tmp)
        rf.extractall()
    except:
        pass
    else:
        print('password:'+tmp)
        break
