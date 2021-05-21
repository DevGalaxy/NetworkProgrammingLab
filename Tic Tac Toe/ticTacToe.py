from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("tik tak toe")
window.geometry("400x300")
lb=Label(window,text="player 1:x ",font =('Helvetica','15'))
lb.grid(column=0,row=0)
lb2=Label(window,text="player 2:O ",font =('Helvetica','15'))
lb2.grid(column=0,row=1)

term=1

def clicked1():
 global term 
 if bt1["text"]=="  ":
  if term==1:
   term=2
   bt1["text"]="x"
  else:
   term=1
   bt1["text"]="O"
  check()

def clicked2():
 global term 
 if bt2["text"]=="  ":
  if term==1:
   term=2
   bt2["text"]="x"
  else:
   term=1
   bt2["text"]="O"
  check()

def clicked3():
 global term 
 if bt3["text"]=="  ":
  if term==1:
   term=2
   bt3["text"]="x"
  else:
   term=1
   bt3["text"]="O"
  check()

def clicked4():
 global term 
 if bt4["text"]=="  ":
  if term==1:
   term=2
   bt4["text"]="x"
  else:
   term=1
   bt4["text"]="O"
  check()

def clicked5():
 global term 
 if bt5["text"]=="  ":
  if term==1:
   term=2
   bt5["text"]="x"
  else:
   term=1
   bt5["text"]="O"
  check()

def clicked6():
 global term 
 if bt6["text"]=="  ":
  if term==1:
   term=2
   bt6["text"]="x"
  else:
   term=1
   bt6["text"]="O"
  check()

def clicked7():
 global term 
 if bt7["text"]=="  ":
  if term==1:
   term=2
   bt7["text"]="x"
  else:
   term=1
   bt7["text"]="O"
  check()

def clicked8():
 global term 
 if bt8["text"]=="  ":
  if term==1:
   term=2
   bt8["text"]="x"
  else:
   term=1
   bt8["text"]="O"
  check()

def clicked9():
 global term 
 if bt9["text"]=="  ":
  if term==1:
   term=2
   bt9["text"]="x"
  else:
   term=1
   bt9["text"]="O"
  check()

flag=1

def check():
 global flag
 flag=flag+1
 b1=bt1["text"]
 b2=bt2["text"]
 b3=bt3["text"]
 b4=bt4["text"]
 b5=bt5["text"]
 b6=bt6["text"]
 b7=bt7["text"]
 b8=bt8["text"]
 b9=bt9["text"]
 if (b1==b2 and b2==b3 and b3=="O") or (b1==b2 and b2==b3 and b1=="x"):
  win(b1)
 if (b4==b5 and b5==b6 and b4=="O") or (b4==b5 and b5==b6 and b4=="x"):
  win(b4)
 if (b7==b8 and b8==b9 and b7=="O") or (b7==b8 and b8==b9 and b7=="x"):
  win(b7)
 if (b1==b4 and b4==b7 and b1=="O") or (b1==b4 and b4==b7 and b1=="x"):
  win(b1)
 if (b2==b5 and b5==b8 and b2=="O") or (b2==b5 and b5==b8 and b2=="x"):
  win(b2) 
 if (b3==b6 and b6==b9 and b3=="O") or (b3==b6 and b6==b9 and b3=="x"):
  win(b3)
 if (b1==b5 and b5==b9 and b1=="O") or (b1==b5 and b5==b9 and b1=="x"):
  win(b1)
 if (b3==b5 and b5==b7 and b3=="O") or (b3==b5 and b5==b7 and b3=="x"):
  win(b3)
 if flag==10:
  messagebox.showinfo("closed try again :)")
  wind.destroy()
def win(player):
 messagebox.showinfo("congratulation", player)
 

bt1=Button(window,text="  ",bg="red",fg="black",width=3,height=1,font=("Helvetica",15),command = clicked1) 
bt1.grid(row=0,column=1)
bt2=Button(window,text="  ",bg="red",fg="black",width=3,height=1,font=("Helvetica",15),command = clicked2) 
bt2.grid(row=0,column=2)
bt3=Button(window,text="  ",bg="red",fg="black",width=3,height=1,font=("Helvetica",15),command = clicked3) 
bt3.grid(row=0,column=3)
bt4=Button(window,text="  ",bg="red",fg="black",width=3,height=1,font=("Helvetica",15),command = clicked4) 
bt4.grid(row=1,column=1)
bt5=Button(window,text="  ",bg="red",fg="black",width=3,height=1,font=("Helvetica",15),command = clicked5) 
bt5.grid(row=1,column=2)
bt6=Button(window,text="  ",bg="red",fg="black",width=3,height=1,font=("Helvetica",15),command = clicked6) 
bt6.grid(row=1,column=3)
bt7=Button(window,text="  ",bg="red",fg="black",width=3,height=1,font=("Helvetica",15),command = clicked7) 
bt7.grid(row=2,column=1)
bt8=Button(window,text="  ",bg="red",fg="black",width=3,height=1,font=("Helvetica",15),command = clicked8) 
bt8.grid(row=2,column=2)
bt9=Button(window,text="  ",bg="red",fg="black",width=3,height=1,font=("Helvetica",15),command = clicked9) 
bt9.grid(row=2,column=3)

window.mainloop()






