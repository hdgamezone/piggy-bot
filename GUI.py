import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Piggy Tools")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_511=tk.Entry(root)
        GLineEdit_511["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_511["font"] = ft
        GLineEdit_511["fg"] = "#333333"
        GLineEdit_511["justify"] = "center"
        GLineEdit_511["text"] = "user id"
        GLineEdit_511.place(x=60,y=20,width=210,height=30)

        GLabel_729=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_729["font"] = ft
        GLabel_729["fg"] = "#333333"
        GLabel_729["justify"] = "left"
        GLabel_729["text"] = "ID"
        GLabel_729.place(x=10,y=20,width=38,height=32)

        GLabel_870=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_870["font"] = ft
        GLabel_870["fg"] = "#333333"
        GLabel_870["justify"] = "left"
        GLabel_870["text"] = "Token :"
        GLabel_870.place(x=10,y=60,width=59,height=30)

        GLineEdit_178=tk.Entry(root)
        GLineEdit_178["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_178["font"] = ft
        GLineEdit_178["fg"] = "#333333"
        GLineEdit_178["justify"] = "center"
        GLineEdit_178["text"] = "Entry"
        GLineEdit_178.place(x=60,y=60,width=211,height=30)

        GMessage_284 = tk.Text(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_284["font"] = ft
        GMessage_284["fg"] = "#333333"
        GMessage_284["justify"] = "center"
        GMessage_284.insert("1.0", "log")  # เพิ่มข้อความเริ่มต้น
        GMessage_284.place(x=20, y=320, width=562, height=164)

        GListBox_321=tk.Listbox(root)
        GListBox_321["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_321["font"] = ft
        GListBox_321["fg"] = "#333333"
        GListBox_321["justify"] = "center"
        GListBox_321.place(x=410,y=70,width=171,height=227)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
