import os
#二分法求零点-py
# By lym12321
# 2020
#给定一个直线 y=x+1
n=1 #精度
def f(x):
    return x+1

a=eval(input("区间左标记："))
b=eval(input("区间右标记："))
if b<=a:
    print("输入错误")
    os.system("pause>nul")
    sys.exit()
elif f(a)*f(b)>0:
    print("给定区间内无零点或有多个零点")
    os.system("pause>nul")
    sys.exit()
elif f(a)==0:
    print("零点为",round(a,n))
    os.system("pause>nul")
    sys.exit()
elif f(b)==0:
    print("零点为",round(b,n))
    os.system("pause>nul")
    sys.exit()
while(1):
    print("[%f,%f]"%(round(a,n),round(b,n)))
    if round(a,n)==round(b,n):
        print("零点约为:",round(a,n))
        break
    c=(a+b)*0.5
    if f(a)*f(c)<0:
        b=c
    elif f(b)*f(c)<0:
        a=c
    elif f(c)==0:
        print("零点为",round(c,n)) 
        break
os.system("pause>nul")