from oop import *
from tkinter.ttk import Style
from tkinter.tix import Balloon
from tkinter import Button, PhotoImage, Scrollbar,IntVar,StringVar, messagebox,filedialog
from tkinter.font import Font
import os

from submain import *

def open_File():
    global parsingTarget
    parsingTarget = filedialog.askopenfilenames(title="Select Files",filetypes=[types])
    if parsingTarget == "":
        parsingTarget=None
        return
    reformatstr = parsingTarget[0].replace("/","\\")
    if len(parsingTarget) == 1: 
        statusTextVar_left.set("Dst : "+reformatstr)
    else:
        newFileStr = ""
        for i in parsingTarget:
            newFileStr += "["+os.path.basename(i)+"]   "
        statusTextVar_left.set("Dst: "+newFileStr)

def open_Dir():
    global parsingTarget 
    parsingTarget = filedialog.askdirectory(title="Select a directory")
    if parsingTarget == "":
        parsingTarget=None
        return
    reformatstr = parsingTarget.replace("/","\\")
    statusTextVar_left.set("Dst: "+reformatstr+"\\*")


def enable_Textbox():
    if intVar.get() == 1:
        textbox.delete(1.0,"end")
        textbox.configure(state="disabled",background="#D0D0D0")
    else:
        textbox.configure(state="normal",background="white")
        if len(textbox.get(0.0,"end")) >= 2 :
            pass
        elif "Search strings" not in textbox.get(0.0,"end"):
            textbox.insert(1.0,"Search strings,\nType an enter to seperate it")

def click_clean_placeholder(event):
    if "Search strings" in textbox.get(0.0,"end"):
       
        textbox.delete(0.0,"end")


def close_toplevel():
    global single_top
    single_top.destroy()
    single_top = None

def insert_treeview(results):
    global parsingTarget

    for i in treeview_01.get_children():
        treeview_01.delete(i)

    if not results.items() :
        treeview_01.insert("","end",text="None")
        messagebox.showinfo("Info","No Records.")
        return
    print(results)
    for keys,values in results.items():  # 10個字串
        
        idString = treeview_01.insert("","end",text=keys)
        # print(values)
        # idFolder = treeview_01.insert(idString,"end",text=os.path.dirname(values[0][0]))
        # for value in values: # n個檔案
        #     # k,v = value[1].items()
        #     print(value)
        #     idFile = treeview_01.insert(idFolder,"end",text='')
        #     for k,v in value[1].items():
        #         print(k,v)
        #         treeview_01.insert(idFile,"end",values=[v,v])        
        # print(values)
        for value in values: # n個檔案
            k,v = value[1].items()
            # total = sum(value[1]['count'])
            # print(total)
            # basename_plus_total =  os.path.basename(value[0])
            
            # while len(basename_plus_total) <36:
            #     basename_plus_total += " "
            # else:
            #     basename_plus_total += f"{total}"
            #     print(basename_plus_total,len(basename_plus_total))  
            idFile = treeview_01.insert(idString,"end",text=os.path.basename(value[0]))
            for i in range(len(k[1])):
                treeview_01.insert(idFile,"end",values=[k[1][i],v[1][i]])

    return

def get_Custom_string():
    # return a list of strings
    strings = textbox.get(1.0,"end-1c").strip()
    arr_string=[]
    temp=""
    # print(strings)
    for s in strings:
        # print(s)
        if s != "\n" and s != "":
            temp+=s
        else:
            if temp != "\n" and temp != "":
                # print(temp)
                arr_string.append(temp.strip())
            temp=""
    else:
        if temp != "\n" and temp != "":
            arr_string.append(temp.strip())
    
    arr_string=list(set(arr_string))
    # print(arr_string)
    return arr_string

def sort_main(event):
    global flag
    # global results
    column=treeview_01.identify("column",event.x,event.y)
    if column == "#2" :
        if treeview_01.get_children() == ():
            return
        if flag :
            resultbysort = sort(results,flag)
            insert_treeview(resultbysort)
            flag -= 1
        else:
            resultbysort = sort(results,flag)
            insert_treeview(resultbysort)
            flag += 1

def copy_clipboard(event):
    if treeview_01.get_children() == ():
        return
    selected=treeview_01.selection()
    root.clipboard_clear()
    for sel in selected:
        root.clipboard_append(treeview_01.item(sel,'text')+"\n")
    


def start():
    global parsingTarget
    global results
    do_option = intVar.get()
    #print(parsingTarget)
    if parsingTarget is None :
        messagebox.showwarning("Reminder","Please select a file or directory first.")
        return
    if do_option == 1 :
        results = constant_Option.get_Records(parsingTarget)
        insert_treeview(results)
        # parsingTarget = None
        return
    if do_option == 2:
        results = custom_Option.get_Records(parsingTarget,get_Custom_string())
        insert_treeview(results)
        # parsingTarget = None
        return

#"(SHA|MD)-\d*\:\s\w*\/\w*\:\w*[\[\w*\]]*$"
constant_Option = ConstantOption(pattern = r"(SHA|MD)-\d*\:\s\w*\/\w*\:\w*([\[\w*\]])*$")
custom_Option = CustomOption()

recovery_image()

root = Window(width=600,height=540)

# Style ---------------------------------
style = Style()
Font_forText = Font(family="Consolas",size=12)
style.configure('TLabelframe.Label', font=("Consolas",11),background="#FFFAF0")
style.configure('TLabelframe',background="#FFFAF0")
style.configure('TNotebook', font=Font_forText)
style.configure('TLabelframe')

# Variable ------------------------------
statusTextVar_left = StringVar()
statusTextVar_right = StringVar()
statusTextVar_left.set("Ready. ")
intVar = IntVar(value=2)
flag = 1 # for sorting use
global parsingTarget 
parsingTarget = None

# Menu bar -------------------------------

menubar = Menubar(root)
file_menu = MenuOption(menubar)
file_menu.add_command(label="Open file",command=open_File)
file_menu.add_command(label="Open directory",command=open_Dir)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)
menubar.add_cascade(label="File",menu=file_menu)
menubar.add_cascade(label="Help",command=lambda:messagebox.showinfo("Get Started",help_exlaination))
root.config(menu=menubar)

# Text Frame -----------------------------

text_frame = CustFrame(root,450,180)
text_frame.grid(row=0,column=0,columnspan=2,sticky="wens",pady=5,padx=3)

labelFrame_option = LabelFrame_(text_frame,"Option",120,140)
labelFrame_option.grid(row=0,column=0,rowspan=2,sticky="n",pady=2,padx=5)
labelFrame_option.grid_propagate(0)

radiobtn_01 = RadioBtn(labelFrame_option,"Default",intVar,1,7)
radiobtn_02 = RadioBtn(labelFrame_option,"Custom",intVar,2,7)
radiobtn_01.config(command=enable_Textbox)

radiobtn_02.config(command=enable_Textbox)
radiobtn_01.grid(row=0,column=0,sticky="we",pady=3)
radiobtn_02.grid(row=1,column=0,sticky="we")


labelFrame_input = LabelFrame_(text_frame,"Input Pane",400,height=200)
labelFrame_input.grid(row=0,column=1,rowspan=3,columnspan=2,sticky="wens",pady=2)
labelFrame_input.grid_rowconfigure(0,weight=1)
labelFrame_input.grid_columnconfigure((0),weight=1)

textbox = TextBox(labelFrame_input,43,10,Font=Font_forText)
textbox.grid(row=0,column=0,sticky="wens",pady=3,padx=3)
textbox.bind("<Button-1>",click_clean_placeholder)
# textbox.bind("<Leave>",leave_showplaceholder)
text_scrollbar = Scrollbar(labelFrame_input,orient="vertical")
text_scrollbar.grid(row=0,column=1,rowspan=2,sticky="wns",pady=3)

textbox.config(yscrollcommand=text_scrollbar.set)
text_scrollbar.config(command=textbox.yview)

# Button ----------------------------

def button_hover(e):
    statusTextVar_right.set("Search")
def button_hover_leave(e):
    statusTextVar_right.set("")



img = PhotoImage(file=r".\ui_img\start.png")
run_button = Button(text_frame,height=30,width=70,image=img,relief="flat",border=0,cursor="target",command=start)
run_button.config(image=img,bg="#FFFAF0",activebackground="#FFFAF0")
run_button.bind("<Enter>",button_hover)
run_button.bind("<Leave>",button_hover_leave)
run_button.grid(row=1,column=0,pady=5)

# # # Tree view Frame -------------------------

tree_notebook = TreeNotebook(root)
tree_frame = TreeFrame(450,200)

tree_notebook.add(tree_frame,text = "Records")
tree_notebook.grid(row=1,column=0,columnspan=2,sticky="wens")

tree_frame.grid_columnconfigure(0,weight=1)
tree_frame.grid_rowconfigure(0,weight=1)

tree_scrollbar = Scrollbar(tree_frame,orient="vertical")
tree_scrollbar.grid(row=0,column=1,sticky="ns")

treeview_01 = TreeTable(tree_frame,tree_scrollbar)
treeview_01.grid(row=0,column=0,sticky="news",padx=3)

tree_scrollbar.config(command=treeview_01.yview)

def add_toplevel(event,a):
    pass
    #print(treeview_01.get_children())
    # global single_top
    #data = treeview_01.item(a)
    # print(treeview_01.get_children())
    # print(treeview_01.selection()[0])
    # print(treeview_01.item(a,'text'))
    # if single_top is not None :
    #     return
    # if treeview_01.focus() in treeview_01.get_children(): 
    #     #print(treeview_01.focus(),data)
    #     return 
    # single_top = TopLevel()
    # single_top.grid_rowconfigure(0,weight=1)
    # single_top.grid_columnconfigure(0,weight=1)
    # single_top.protocol("WM_DELETE_WINDOW",close_toplevel)
    # single_top.title(data['text'])
    # single_top.grab_set() # force focus this toplevel until close
    # single_top.focus()

    # treeview_toplevel = Treeview(single_top,show="headings",columns=("Table"))
    # treeview_toplevel.grid(sticky="wens",padx=3,pady=3)
    # treeview_toplevel.heading("#1",text="Line",anchor="w")
    # treeview_toplevel.column("#1",width=20)

single_top = None

#treeview_01.event_add("<<TreeviewItemSelect>>","<Double-Button-1>")
# treeview_01.bind("<Double-Button-1>",lambda event:add_toplevel(event,\
#     treeview_01.focus()))
treeview_01.bind("<Button-1>",sort_main)
treeview_01.bind("<Control-c>",copy_clipboard)
# # Status bar ----------------------------------------

# statusbar_left=StatusBar(root,statusTextVar_left)
# statusbar_left.grid(row=2,column=0,columnspan=2,sticky="w",padx=5)
# statusbar_left.bind("<Control-c>",statusbar_copy_clipboard)

statusbar_left = Status_Entry(root,statusTextVar_left)
statusbar_left.grid(row=2,column=0,columnspan=2,sticky="we",padx=5)

statusbar_right=StatusBar(root,statusTextVar_right)
statusbar_right.grid(row=2,column=1,columnspan=2,sticky="e",padx=5)


# Tool Tips -------------------

tip = Balloon(root)
for sub in tip.subwidgets_all():
  sub.config(bg='#FFFAF0')
tip.bind_widget(run_button,balloonmsg="Search")
tip.bind_widget(radiobtn_01,balloonmsg="Default definaiton")
tip.bind_widget(radiobtn_02,balloonmsg="Custom strings, type an <Enter> to seperate strings to search")
tip.bind_widget(labelFrame_input,balloonmsg="Input Pane")

root.mainloop()


