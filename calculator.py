from decimal import DefaultContext
from email.policy import default
from tkinter import *
top= Tk()
top.geometry("349x600")
top.title("Celculator")

##text
t=Text(top,width=50,height=1,font=("Times New Roman ",60))
t.pack()


b1=Button(top,text="%",width=12,height=6,bg="light gray")
b1.place(x=0,y=85)

b2=Button(top,text="_/",width=12,height=6,bg="light gray")
b2.place(x=85,y=85)

b3=Button(top,text="x*2",width=12,height=6,bg="light gray")
b3.place(x=170,y=85)

b4=Button(top,text="1/x",width=12,height=6,bg="light gray")
b4.place(x=255,y=85)

## buttons
b1=Button(top,text="CE",width=12,height=6,bg="light gray")
b1.place(x=0,y=170)

b2=Button(top,text="C",width=12,height=6,bg="light gray")
b2.place(x=85,y=170)

b3=Button(top,text="<x",width=12,height=6,bg="light gray")
b3.place(x=170,y=170)

b4=Button(top,text="/",width=12,height=6,bg="light gray")
b4.place(x=255,y=170)
### number
n1=Button(top,text="7",width=12,height=6,bg="white",fg="black")
n1.place(x=0,y=255)

n1=Button(top,text="8",width=12,height=6,bg="white",fg="black")
n1.place(x=85,y=255)


n1=Button(top,text="9",width=12,height=6,bg="white",fg="black")
n1.place(x=170,y=255)


n1=Button(top,text="*",width=12,height=6,bg="light gray")
n1.place(x=255,y=255)

### number 2


n1=Button(top,text="4",width=12,height=6,bg="white",fg="black")
n1.place(x=0,y=340)


n1=Button(top,text="5",width=12,height=6,bg="white",fg="black")
n1.place(x=85,y=340)

n1=Button(top,text="6",width=12,height=6,bg="white",fg="black")
n1.place(x=170,y=340)

n1=Button(top,text="-",width=12,height=6,bg="light gray")
n1.place(x=255,y=340)

### number 3
n1=Button(top,text="1",width=12,height=6,bg="white",fg="black")
n1.place(x=0,y=425)

n1=Button(top,text="2",width=12,height=6,bg="white",fg="black")
n1.place(x=85,y=425)

n1=Button(top,text="3",width=12,height=6,bg="white",fg="black")
n1.place(x=170,y=425)

n1=Button(top,text="+",width=12,height=6,bg="light gray")
n1.place(x=255,y=425)

### number 4
n1=Button(top,text="+/-",width=12,height=6,bg="light gray")
n1.place(x=0,y=510)

n1=Button(top,text="0",width=12,height=6,bg="white",fg="black")
n1.place(x=85,y=510)

n1=Button(top,text=".",width=12,height=6,bg="light gray")
n1.place(x=170,y=510)

n1=Button(top,text="=",width=12,height=6,bg="light gray")
n1.place(x=255,y=510)


top.mainloop()
    
