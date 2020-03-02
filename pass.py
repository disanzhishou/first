def getlist():
    min=input("请输入最短长度")
    max=input("请输入最长长度")
    str=input("请输入字符集")
    name=input("请输入文件名")
    data=[int(min),int(max)+1,str,name]
    return data

def write(num,data,name,long):
    f=open(name,'a')
    str=''
    for s in range(long):
        str=str+data[num[s]]
    f.write(str+'\n')

def main():
    data=getlist()
    long=len(data[2])
    for l in range(data[1]-data[0]):#changdu
        i=l+data[0]
        str=[0 for n in range(i)]
        write(str, data[2], data[3], i)
        for j in range(long**i-1):    #dijici
            for k in range(i):
                if (j%(long**(i-k-1)))==0:
                    str[k-1]=(str[k-1]+1)%long
            write(str,data[2],data[3],i)
    print("finish")

main()



