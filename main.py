from twilio.rest import Client
import twilio
import random
import tkinter


from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("600x500")
root.resizable(False,False)
n=random.randint(1000,9999)


def checkotp():
    try:
        userInput=int(user_name.get(1.0,"end-1c"))
        if userInput==n:
            messagebox.showinfo("showinfo","login successfully")
            n="done"
            
        elif n=="done":
            messagebox.showinfo("showinfo","Already logged In")
        else :
            messagebox.showinfo("showinfo","wrong OTP")
            
            
    except :
        messagebox.showinfo("showinfo","INVALID OTP")
        
    
def resendotp():
    n=random.randint(1000,9999)
    client=Client("PNf3f5b97da748fb53cd5833e0052b3318","7e6ca4a2b86c3ff90303d6c2961ef7d0")
    client.messages.create(to=["+254795326223"],
                                from_="+19126008895",
                                body=n)

client=Client("AC974985e6d9a7509b8157a7c2ac309e35","7e6ca4a2b86c3ff90303d6c2961ef7d0")
client.messages.create(to=["+254795326223"],
                            from_="+19126008895",
                            body=n)
    
    
c=Canvas(root,bg="white",width=400,height=200)
c.place(x=100,y=60)

login_title=Label(root,text="OTP Verification",font="bold, 20",bg="white")
login_title.place(x=210,y=90)
    
    
    
user_name=Text(root,borderwidth=2,wrap="word",width=20,height=2)
user_name.place(x=190,y=160)
    
    

submitbuttonimage=PhotoImage(file='submit.png')
submitbutton=Button(root,image=submitbuttonimage,command=checkotp,border=0)
submitbutton.place(x=200,y=240)

resendbuttonimage=PhotoImage(file='resend.png')
resendbutton=Button(root,image=resendbuttonimage,command=resendotp,border=0)
resendbutton.place(x=200,y=400)
    

        
        
        
        

root.mainloop()
    
