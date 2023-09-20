from  tkinter import *
from PIL import ImageTk,Image
from tkinter  import filedialog,messagebox
root=Tk()
root.title("Project")
root.geometry("600x600+0+0")
#root.resizable(False,False)

label1=Label(root,text="Name:",font=("Arial",10,"bold"),padx=10,pady=10)
label1.grid(row=0,column=0)
ent=Entry(root,font=("Arial",10,"bold"))
ent.grid(row=0,column=1)

label2=Label(root,text="Date:",font=("Arial",10,"bold"),padx=10,pady=10)
label2.grid(row=1,column=0)
ent=Entry(root,font=("Arial",10,"bold"))
ent.grid(row=1,column=1)


def openfile():
    op=filedialog.askopenfile(title="select file",filetypes=(("text file ",".txt"),))
    if op!=None:
        label3.config(text="FileName:"+str(op.name.split("/")[-1]))
        var_filename.set(str(op.name))
        for i in op:
            txt1.insert(END ,str(i))
        op.close() 
        messagebox.showinfo ("Save As","File Saved") 



def savefile():
     if var_filename.get()=="":
        saveasfile()
     else:
        op.open(var_filename.get(),"w")
        op.write(txt1.get("1.0",END))
        op.close()
        messagebox.showinfo ("Save File AS","File Saved") 


def saveasfile():
     op=filedialog.asksaveasfile(title="Save AS",filetypes=(("text file ",".txt"),))
     if op!=None:
         op.write(txt1.get("1.0",END))
         op.close()
         messagebox.showinfo ("Save As","File Saved") 
     


btn=Button(root,text="OPEN",command=openfile,font=("Arial",10,"bold"),width=100)
btn.place(x=50,y=100,width=100)
btn1=Button(root,text="SAVE",command=savefile,font=("Arial",10,"bold"),width=100)
btn1.place(x=150,y=100,width=100)
btn2=Button(root,text="SAVE AS",command=saveasfile,font=("Arial",10,"bold"),width=100)
btn2.place(x=250,y=100,width=100)


var_filename=StringVar()

label3=Label(root,text="FileName",font=("Arial",10,"bold"),padx=10,pady=10)
label3.place(x=50,y=130)


txt1=Text(root,font=("Arial",10,"bold"),relief=RIDGE,bd=2,padx=10,pady=10)
txt1.place(x=50,y=170)







root.mainloop()