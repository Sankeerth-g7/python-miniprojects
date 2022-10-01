from tkinter import *
import speedtest
def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3)) +' Mbps '
    up=str(round(sp.upload()/(10**6),3)) +' Mbps '
    do.config(text=down)
    upl.config(text=up) 
sp= Tk()
sp.title('Internet speed tester')
sp.geometry('450x550')
sp.config(bg="Black")
lb=Label(sp,text="Internet speed",font=("Arial Bold",30,"bold"),bg="Black",fg="White")
lb.place(x=85,y=20,height=60,width=270)
lb=Label(sp,text="Download speed",font=("Arial Bold",30,"bold"))
lb.place(x=50,y=100,height=60,width=320)
do=Label(sp,text="00",font=("Arial Bold",30,"bold"))
do.place(x=50,y=180,height=60,width=310)
lb=Label(sp,text="Upload speed",font=("Arial Bold",30,"bold"))
lb.place(x=50,y=260,height=60,width=310)
upl=Label(sp,text="00",font=("Arial Bold",30,"bold"))
upl.place(x=50,y=340,height=60,width=310)
button=Button(text='start test',font=("Arial Bold",30,"bold"),bg='Grey',command=speedcheck)
button.place(x=105,y=420)
sp.mainloop()
