from oop import *
from tkinter.ttk import Progressbar, Style
from tkinter.tix import Balloon
from tkinter import Button, PhotoImage, Scrollbar,IntVar,StringVar, messagebox,filedialog
from tkinter.font import Font
import os,time,threading
# from queue import Queue
# from multiprocessing import Process
from submain import *

             

def open_SrcFile():
    global srcFile
    srcFile = filedialog.askopenfilename(title="Select File",filetypes=[("txt","*.txt")])
    if srcFile == "" :
        if entry_src_var.get():
            srcFile = entry_src_var.get()
        else:
            srcFile = None
            return
    srcFile = srcFile.replace("/","\\")
    entry_src_var.set(srcFile)

    with open('configuration\\tmp.tmp',mode="w",encoding="utf-8") as f:
        f.write(srcFile)
    # print(srcFile)
    


def open_File():
    global parsingTarget
    global temp_parsingTarget
    parsingTarget = filedialog.askopenfilenames(title="Select Files",filetypes=[types])
    # print(parsingTarget)
    if parsingTarget == "":
        if entry_dst_var.get():
            parsingTarget = temp_parsingTarget 
        else:
            parsingTarget=None
            return
    reformatstr = parsingTarget[0].replace("/","\\")
    if len(parsingTarget) == 1: 
        entry_dst_var.set(reformatstr)
        temp_parsingTarget = parsingTarget
    elif isinstance(parsingTarget,tuple) and len(parsingTarget) > 1 :
        newFileStr = ""
        for i in parsingTarget:
            newFileStr += "["+os.path.basename(i)+"] "
        # entry_dst_var.set(newFileStr)
        entry_dst_var.set(newFileStr)
        temp_parsingTarget = parsingTarget
    else: 
        parsingTarget = temp_parsingTarget


def open_Dir():
    global parsingTarget 
    global temp_parsingTarget
    entry_dst_var.set("")
    parsingTarget = filedialog.askdirectory(title="Select a directory")
    if parsingTarget == "":
        # if entry_dst_var.get():
        #     # parsingTarget = temp_parsingTarget
        #     parsingTarget = entry_dst_var.get().replace(r"\*","")
        # else:
        parsingTarget=None
        return
    temp_parsingTarget = parsingTarget
    reformatstr = parsingTarget.replace("/","\\")
    # statusTextVar_left.set("Dst: "+reformatstr+"\\*")
    entry_dst_var.set(reformatstr+r"\*")

def enable_source_btn():
    global srcFile
    if intVar.get() == 1:
        browser_src.configure(state="disabled")
        entry_src_var.set("")
    else:
        srcFile = None
        browser_src.configure(state="normal")
        # if len(textbox.get(0.0,"end")) >= 2 :
        #     pass
        # elif "Search strings" not in textbox.get(0.0,"end"):
        #     textbox.insert(1.0,"Search strings,\nType an enter to seperate it")


# def enable_Textbox():
#     if intVar.get() == 1:
#         textbox.delete(1.0,"end")
#         textbox.configure(state="disabled",background="#D0D0D0")
#     else:
#         textbox.configure(state="normal",background="white")
#         if len(textbox.get(0.0,"end")) >= 2 :
#             pass
#         elif "Search strings" not in textbox.get(0.0,"end"):
#             textbox.insert(1.0,"Search strings,\nType an enter to seperate it")

# def click_clean_placeholder(event):
#     if "Search strings" in textbox.get(0.0,"end"):
       
#         textbox.delete(0.0,"end")


# def close_toplevel():
#     global single_top
#     single_top.destroy()
#     single_top = None

def clear_treeview_data():
    for i in treeview_01.get_children():
        treeview_01.delete(i)

def insert_treeview(results):
    global parsingTarget
    
    clear_treeview_data()
    if results is None :
        return
    
    if not results.items() :
        
        treeview_01.insert("","end",text="No Records")
        # messagebox.showinfo("Info","No Records.")
        return
    # if textbox['state'] == 'normal':
    #     orderResults = dict()
    #     # print(get_Custom_string())
    #     for string in get_Custom_string():
    #         for key,value in results.items():
    #             if key == string:
    #                 orderResults.update({key:value})
    #     results = orderResults
    
    if isinstance(parsingTarget,tuple) and len(parsingTarget) == 1:
        for keys,values in results.items():
            position,count,total = values[0][1].items()
            # if len(keys) >= 200:
            #     tmp = keys[:len(keys) // 2] + '\n' +keys[len(keys) // 2:]
            #     idString = treeview_01.insert("","end",text=tmp,values=[total[1]])
            # else:
            idString = treeview_01.insert("","end",text=keys,values=[total[1]])
            for value in values:
                k,v,total = value[1].items()
                # idFile = treeview_01.insert(idString,"end",text="",values=[total[1],"",""])
                for i in range(len(k[1])):
                    treeview_01.insert(idString,"end",values=["",k[1][i],v[1][i]])
    else:
        for keys,values in results.items():  # 10個字串
            # if len(keys) >= 200:
            #     tmp = keys[:len(keys) // 2] + '\n' +keys[len(keys) // 2:]
            #     idString = treeview_01.insert("","end",text=tmp)
            # else:
            #     pass
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
                # print(value[1].items())
                k,v,total = value[1].items()
                # total = sum(value[1]['count'])
                # print(total)
                # basename_plus_total =  os.path.basename(value[0])
                
                # while len(basename_plus_total) <36:
                #     basename_plus_total += " "
                # else:
                #     basename_plus_total += f"{total}"
                # #     print(basename_plus_total,len(basename_plus_total))  
                # print(total)
                idFile = treeview_01.insert(idString,"end",text=os.path.basename(value[0]),values=[total[1],"",""])
                # print(k)
                for i in range(len(k[1])):
                    treeview_01.insert(idFile,"end",values=["",k[1][i],v[1][i]])

    return

def get_Custom_string():
    # return a list of strings
    # strings = textbox.get(1.0,"end-1c")
    if os.path.exists(srcFile) :
        try:
            with open(srcFile,mode="r",encoding="utf-8") as f:
                strings = f.read()
        except:
            messagebox.showwarning("Warning","Please save as a new source file with encoding UTF-8")
            return
    else:
        messagebox.showwarning("Warning","The source file missed.")
        return
    # print(strings)
    arr_string=[]
    temp=r""
    if strings != "":
        for s in strings:
            if s != '\n' :
                temp+=s
            else:
                if temp != "\n" and temp != "" and s != " ":
                    if temp.strip() not in arr_string:
                        arr_string.append(temp.strip())
                temp=""
        else:
            if temp != "\n" and temp != "" and s != " ":
                if temp.strip() not in arr_string:
                    arr_string.append(temp.strip())
    
    arr_string=list(set(arr_string))
    # print(arr_string)
    return arr_string

def sort_main(event):
    global flag_s
    global flag_t
    global flag_l
    global flag_c
    global resultbysort
    column=treeview_01.identify("column",event.x,event.y)
    if treeview_01.get_children() == ():
        return
    if column == "#0":
        if flag_s :
            if resultbysort :
                resultbysort = sort_string(resultbysort,flag_s)
                insert_treeview(resultbysort)
            else:
                resultbysort = sort_string(results,flag_s)
                insert_treeview(resultbysort)
            flag_s -= 1
        else:
            if resultbysort :
                resultbysort = sort_string(resultbysort,flag_s)
                insert_treeview(resultbysort)
            else:
                resultbysort = sort_string(results,flag_s)
                insert_treeview(resultbysort)
            flag_s += 1        
    # print(results)
    elif column == "#1" :
        # print(flag_t)
        if flag_t :
            if resultbysort :
                resultbysort = sort_total(resultbysort,flag_t)
                insert_treeview(resultbysort)
            else:
                resultbysort = sort_total(results,flag_t)
                insert_treeview(resultbysort)
            flag_t -= 1
        else:
            if resultbysort :
                resultbysort = sort_total(resultbysort,flag_t)
                insert_treeview(resultbysort)
            else:
                resultbysort = sort_total(results,flag_t)
                insert_treeview(resultbysort)
            flag_t += 1
        
    elif column == "#2" :
        if flag_l :
            if resultbysort :
                resultbysort = sort_line(resultbysort,flag_l)
                insert_treeview(resultbysort)
            else:
                resultbysort = sort_line(results,flag_l)
                insert_treeview(resultbysort)
            flag_l -= 1
        else:
            if resultbysort :
                resultbysort = sort_line(resultbysort,flag_l)
                insert_treeview(resultbysort)
            else:
                resultbysort = sort_line(results,flag_l)
                insert_treeview(resultbysort)
            flag_l += 1
        
    elif column == "#3" :
        if flag_c :
            if resultbysort :
                resultbysort = sort_count(resultbysort,flag_c)
                insert_treeview(resultbysort)
            else:
                resultbysort = sort_count(results,flag_c)
                insert_treeview(resultbysort)
            flag_c -= 1
        else:
            if resultbysort :
                resultbysort = sort_count(resultbysort,flag_c)
                insert_treeview(resultbysort)
            else:
                resultbysort = sort_count(results,flag_c)
                insert_treeview(resultbysort)
            flag_c += 1
    # print(root.geo)

def copy_clipboard(event):
    if treeview_01.get_children() == ():
        return
    selected=treeview_01.selection()
    root.clipboard_clear()
    for sel in selected:
        root.clipboard_append(treeview_01.item(sel,'text')+"\n")
    
def warning_src_target_exist():
    global srcFile
    global parsingTarget
    run_button.config(state="normal")
    if srcFile is None and intVar.get() != 1 :
        messagebox.showwarning("Reminder","Please select a Source file.")    
        return 1
    if parsingTarget is None :
        messagebox.showwarning("Reminder","Please select a Target file or directory.")
        return 1


def progress_start():
    progress_bar.grid(row=2,column=0,sticky="we")
    threading.Thread(target=progress_bar.start,args=(10,)).start()
def progress_stop():
    time.sleep(0.5)
    threading.Thread(target=progress_bar.stop).start()
    progress_bar.grid_forget()
    
    
def thread_start():

    thread =  threading.Thread(target=start)
    thread.start()
    root.update_idletasks()
    run_button.config(state="disabled")
    # thread.join()
    

def start():
    
    global error_records
    global parsingTarget
    global results
    global resultbysort
    resultbysort = None
    keep = 0
    do_option = intVar.get()
    
    if warning_src_target_exist():
        return
    if do_option == 1 :
        clear_treeview_data()
        progress_start()
        results = constant_Option.get_Records(parsingTarget,error_records)

        for key,value in error_records.items():
            if not keep :
                keep = messagebox.askokcancel('Info',"Found :\n"+key+'\n\n'+value+'\n\nClick OK to ignore about this message')
        results = sort_string(results,0)
        insert_treeview(results)
        progress_stop()
        run_button.config(state="normal")
        error_records = dict()
        return
    if do_option == 2:
        clear_treeview_data()
        progress_start()
        results = custom_Option.get_Records(parsingTarget,get_Custom_string(),error_records)
        for key,value in error_records.items():
            if not keep :
                keep = messagebox.askokcancel('Info',"Found :\n"+key+'\n'+value+'\n\nClick OK to ignore about this message')
        results = sort_string(results,0)
        insert_treeview(results)
        progress_stop()
        run_button.config(state="normal")
        error_records = dict()
        return

#"(SHA|MD)-\d*\:\s\w*\/\w*\:\w*[\[\w*\]]*$"
constant_Option = ConstantOption(pattern = r"(SHA|MD)-\d*\:\s\w*\/\w*\:\w*([\[\w*\]])*$")
custom_Option = CustomOption()

recovery_image()

root = Window(width=640,height=540)

# Style ---------------------------------
style = Style()
Font_forText = Font(family="Consolas",size=12)
style.configure('TLabelframe.Label', font=("Consolas",11),background="#FFFAF0")
style.configure('Treeview', font=("Consolas",10),background="#FFFAF0",rowheight=24)
style.configure('Treeview.Heading', font=("Consolas",9),background="#FFFAF0")
style.configure('TLabelframe',background="#FFFAF0")
style.configure('TNotebook', font=Font_forText)
style.configure('TNotebook.Tab', font=("Consolas",9))
style.configure('TLabelframe')

# Variable ------------------------------
entry_src_var = StringVar()
entry_dst_var = StringVar()
statusTextVar_left = StringVar()
statusTextVar_right = StringVar()
# statusTextVar_left.set("Ready. ")
intVar = IntVar(value=2)
global flag_t
global flag_l
global flag_c
global flag_s
flag_s = 1
flag_t = 1
flag_l = 1
flag_c = 1
global parsingTarget 
global srcFile
global temp_parsingTarget
global resultbysort
resultbysort = None
global error_records
error_records = dict()
parsingTarget = None
srcFile = None
temp_parsingTarget = parsingTarget
# Menu bar -------------------------------

menubar = Menubar(root)
file_menu = MenuOption(menubar)
# file_menu.add_command(label="Open file",command=open_File)
file_menu.add_command(label="Open Target directory",command=open_Dir)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)
menubar.add_cascade(label="File",menu=file_menu)
menubar.add_cascade(label="Help",command=lambda:messagebox.showinfo("Get Started",help_exlaination))
root.config(menu=menubar)

# Text Frame -----------------------------

text_frame = CustFrame(root,450,290)
text_frame.grid(row=0,column=0,columnspan=2,sticky="wens",pady=5,padx=3)

labelFrame_option = LabelFrame_(text_frame,"Option",120,140,Font=("Consolas",12))
labelFrame_option.grid(row=0,column=0,rowspan=3,sticky="wens",pady=2,padx=5)
labelFrame_option.grid_propagate(0)

radiobtn_01 = RadioBtn(labelFrame_option,"Default",intVar,1,7)
radiobtn_02 = RadioBtn(labelFrame_option,"Custom",intVar,2,7)
radiobtn_01.config(command=enable_source_btn)

radiobtn_02.config(command=enable_source_btn)
radiobtn_01.grid(row=0,column=0,sticky="we",pady=3)
radiobtn_02.grid(row=1,column=0,sticky="we")


labelFrame_input = LabelFrame_(text_frame,"Src-Target",width=400,height=140,Font=("Consolas",12))
labelFrame_input.grid(row=0,column=1,rowspan=3,columnspan=2,sticky="wens",pady=2)
labelFrame_input.grid_propagate(0)
# labelFrame_input.grid_rowconfigure(0,weight=0)
labelFrame_input.grid_columnconfigure((1),weight=1)

browser_src = Button(labelFrame_input,text="Source",width=8,command=open_SrcFile,font=('Consolas',10))
browser_src.grid(row=0,column=0,padx=3,pady=5)

entry_src = Entry_FS(labelFrame_input,entry_src_var)
entry_src.grid(row=0,column=1,sticky="wens",padx=3,pady=5,ipady=2)

browser_dst = Button(labelFrame_input,text="Target",width=8,command=open_File,font=('Consolas',10))
browser_dst.grid(row=1,column=0,padx=3,pady=5)

entry_dst = Entry_FS(labelFrame_input,entry_dst_var)
entry_dst.grid(row=1,column=1,sticky="wens",padx=3,pady=5,ipady=2)

# textbox = TextBox(labelFrame_input,43,10,Font=Font_forText)
# textbox.grid(row=0,column=0,sticky="wens",pady=3,padx=3)
# textbox.bind("<Button-1>",click_clean_placeholder)
# textbox.bind("<Leave>",leave_showplaceholder)
# text_scrollbar = Scrollbar(labelFrame_input,orient="vertical")
# text_scrollbar.grid(row=0,column=1,rowspan=2,sticky="wns",pady=3)

# textbox.config(yscrollcommand=text_scrollbar.set)
# text_scrollbar.config(command=textbox.yview)

# Button ----------------------------

def button_hover(e):
    statusTextVar_right.set("Search")
def button_hover_leave(e):
    statusTextVar_right.set("")

# thread_start = Thread(target=start)

img = PhotoImage(file=r".\img\start.png")
run_button = Button(labelFrame_input,height=30,width=70,image=img,relief="flat",border=0,cursor="target",command=thread_start)
run_button.config(image=img,bg="#FFFAF0",activebackground="#FFFAF0")
run_button.bind("<Enter>",button_hover)
run_button.bind("<Leave>",button_hover_leave)
run_button.grid(row=2,column=1,pady=5)

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
treeview_01.bind("<Button-3>",sort_main)
treeview_01.bind("<Control-c>",copy_clipboard)
# # Status bar ----------------------------------------

# statusbar_left=StatusBar(root,statusTextVar_left)
# statusbar_left.grid(row=2,column=0,columnspan=2,sticky="w",padx=5)
# statusbar_left.bind("<Control-c>",statusbar_copy_clipboard)

# statusbar_left = Status_Entry(root,statusTextVar_left)
# statusbar_left.grid(row=2,column=0,columnspan=2,sticky="we",padx=5)

# statusbar_right=StatusBar(root,statusTextVar_right)
# statusbar_right.grid(row=2,column=1,columnspan=2,sticky="e",padx=5)


progress_bar = Progressbar(root,orient="horizontal",mode="indeterminate",length=600)
# progress_bar.grid(row=2,column=0,sticky="we")

# Tool Tips -------------------

tip = Balloon(root)
for sub in tip.subwidgets_all():
  sub.config(bg='#FFFAF0')
tip.bind_widget(run_button,balloonmsg="Search")
tip.bind_widget(radiobtn_01,balloonmsg="Default definaiton")
tip.bind_widget(radiobtn_02,balloonmsg="Custom the strings from a source file")
# tip.bind_widget(labelFrame_input,balloonmsg="Input Pane")


chk_necessary_file()

if os.path.exists("configuration\\tmp.tmp"):
    with open("configuration\\tmp.tmp",mode="r",encoding="utf-8") as f:
        strPath = f.read()
    srcFile = strPath
    entry_src_var.set(strPath)


root.mainloop()


