from tkinter import *
from tkinter import ttk
from API import Send_msg
from tkinter import messagebox

class Window:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x800")
        self.root.title("Sms sender")
        self.root.resizable(0,0)
        self.root.tk.call("source", "sun-valley.tcl")
        self.root.tk.call("set_theme", "dark")
        self.main()
        self.root.mainloop()

    def main(self):
        head = Label(text="SMS sender")
        head.pack()
        body_lbl = Label(text="BODY")
        body_lbl.place(x=10, y=50)
        self.body = Text(width=141,height=10)
        self.body.place(x=3, y=90)
        to_lbl = Label(text="To")
        to_lbl.place(x=10,y=290)
        self.to_ent = ttk.Entry(width=40)
        self.to_ent.place(x=10,y=340)
        from_lbl = Label(text="From")
        from_lbl.place(x=10,y=390)
        self.from_ent =ttk.Entry(width=40)
        self.from_ent.place(x=10,y=420)
        send = ttk.Button(text="Send",style="Accent.TButton", width=20,command=self.send)
        send.place(x=800,y=700)

    def send(self):
        try:
            Send_msg(self.body.get('1.0','end'),self.to_ent.get(),self.from_ent.get())
            messagebox.showinfo("Success","Message sent successfully")
        except:
            messagebox.showerror("Error","Error occured in API.py")

window = Window()
