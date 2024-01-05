from tkinter import *   
from tkinter import messagebox 
from jarvisAI2 import TaskExe



r=Tk()   
r.geometry('250x250')    
r.title('HiliX')

SubmitBtn = Button(r,text="Submit",bg='#d1ccc0', fg='black',command=lambda:Task(),font=('Times 13 bold'))    # Create submit button
SubmitBtn.place(relx=0.33,rely=0.5, relwidth=0.30,relheight=0.08)

def Task():
    TaskExe()
r.mainloop()



