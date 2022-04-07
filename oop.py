from tkinter import Label,Entry, Menu, Radiobutton, Text,Frame, Toplevel
from tkinter.ttk import Labelframe, Notebook, Treeview
from tkinter.tix import Tk

# Font ---------------------------------


class Window(Tk):
    def __init__(self,width,height):
        Tk.__init__(self)
        self.title("Search")
        self.width=width
        self.height=height
        x = (self.winfo_screenwidth() - self.width)//2
        y = (self.winfo_screenheight() - self.height)//2 
        # self.resizable(width=0,height=0) # not allow modify window
        self.geometry("{0}x{1}+{2}+{3}".format(self.width,self.height,x,y))
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.config(bg="#FFFAF0")
        self.iconbitmap(r".\ui_img\search.ico")
        # self.columnconfigure(0,weight=1)
        # self.columnconfigure(1,weight=1)
        # Grid.rowconfigure(self,0,weight=1)
        # Grid.columnconfigure(self,0,weight=1)
        # Grid.rowconfigure(self,1,weight=1)
        # Grid.rowconfigure(self,2,weight=0)


class Menubar(Menu):
    def __init__(self,master):
        Menu.__init__(self,master)

class MenuOption(Menu):
    def __init__(self,master):
        Menu.__init__(self,master,tearoff=False)

        
    


class CustFrame(Frame):
    def __init__(self,master,width=0,height=0):
        Frame.__init__(self,master,width=width,height=height)
        self.config(highlightbackground="black",highlightthickness=0)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.config(bg="#FFFAF0")
        # self.grid_rowconfigure(1,weight=1)

class RadioBtn(Radiobutton):
    def __init__(self,master,textName,Var,value,width,Font=None):
        Radiobutton.__init__(self,master,\
            text=textName,variable=Var,value=value,width=width,anchor="w",\
            highlightthickness=1,highlightbackground="black")
        self.config(font=("Consolas",12),bg="#FFFAF0",activebackground="#FFFAF0",takefocus="")
    

class TextBox(Text):
    def __init__(self,master,width=0,height=0,Font=None):
        Text.__init__(self,master,font=Font,\
        width=width,height=height)
        self.insert(1.0,"Search strings,\nType an enter to seperate")




class TreeFrame(Frame):
    def __init__(self,width,height):
        Frame.__init__(self,width=width,height=height)
        self.config(highlightbackground="black",highlightthickness=0,bg="#FFFAF0")
        # self.rowconfigure(0,weight=1)
        # self.columnconfigure(0,weight=1)        


# # tr_notebook = Notebook(root)
class TreeNotebook(Notebook):
    def __init__(self,master):
        Notebook.__init__(self,master)
        # self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        



class TreeTable(Treeview):
    # File={"a":{2:[1,2,23,214,41244,25555,511111]},"b":{2:[1,2]},"c":{2:[1,2]},"d":{2:[1,2]}}
    def __init__(self,master,scrollbarObj):
        Treeview.__init__(self,master)
        self.config(columns=("Position","Count"),show="tree headings",\
            selectmode="extended",height=14,yscrollcommand=scrollbarObj.set)
        self.heading("#0",text="Strings / Files")
        self.heading("#1",text="Line")
        self.heading("#2",text="Count")
        self.column("#0",anchor="w",width=430,minwidth=430,stretch=1)
        self.column("#1",anchor="center",width=70,minwidth=70,stretch=1)
        self.column("#2",anchor="center",width=70,minwidth=70,stretch=1)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        



class StatusBar(Label):
    def __init__(self,master,Var):
        Label.__init__(self,master,\
            textvariable=Var,anchor="w",bg="white",\
            font=("Consolas",10,"bold"),\
            )
        #self.columnconfigure(0,weight=0)

class Status_Entry(Entry):
    def __init__(self,master,var):
        Entry.__init__(self,master,\
            textvariable=var,font=("Consolas",10,"bold"),
            state="readonly",border=0,bg="white",readonlybackground="white")


class LabelFrame_(Labelframe):
    def __init__(self,master,text,width=None,height=None,Font=None):
        Labelframe.__init__(self,master,text=text,width=width,height=height)

        

class TopLevel(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        width = 120
        height =200
        x = self.winfo_screenwidth() //2 -width//2
        y = self.winfo_screenheight() //2 - width //2
        
        self.geometry("{0}x{1}+{2}+{3}".format(width,height,x,y))
        

