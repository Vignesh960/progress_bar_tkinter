from tkinter import *

root=Tk()
root.title("ProgressBar")
root.geometry("200x200+100+50")
root.configure(bg="#2F6C60")
root.resizable(0,0)
per=StringVar()
count=StringVar()
def start():
    
    tasks=10
    x=0
    bar['value']=0
    while x<tasks:
        time.sleep(0.5)
        bar['value']+=10
        x+=1
        per.set(str((x/tasks)*100)+"%")
        count.set(str(x)+"/"+str(tasks)+" Completed")
        bar.update()

bar=ttk.Progressbar(root,length=300,orient=HORIZONTAL)
bar.pack(padx=10)
'''for updating percent of totals'''
per_label=Label(root,textvariable=per,bg="#2F6C60",fg="#FFFFFF").pack()
'''for updating count of totals'''
count_label=Label(root,textvariable=count,width=20,background="#2F6C60",fg="#FFFFFF").pack()

Button(root,text="Download",command=start).pack(padx=10,pady=10)
root.mainloop()
