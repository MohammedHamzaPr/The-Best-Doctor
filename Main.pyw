from Library import *
c = False
class Main:
    global Closed
    Closed = False
    def check():
        global Check
        while True:
            sleep(0.7)
            if Closed == True:
                break
            if c == True:
                exit()
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            global Closed
            Closed = True
            w.destroy()
    Thread(target=check).start()
    def window_settings(window):
        global w 
        w = window
        window.state('zoomed')
        window.resizable(False, False)
        window.geometry('1144x1000+0+0')
        window.title('The Best Docktir')
        window.config(background='silver')
        window.iconbitmap(os.getcwd()+'/src/tooth.ico')

    def mohm():
        if os.path.exists('C:/Users/{0}/Documents/Databases'.format(os.getlogin())) == False:
            os.mkdir('C:/Users/{0}/Documents/Databases'.format(os.getlogin()))
        if len(Id_Entry.get()) < 1:
            messagebox.showerror('Check','Please check the ID field')
        elif len(Name_Entry.get()) < 1:
            messagebox.showerror('Check','Please check the Name field')
        elif len(Address_Entry.get()) < 1:
            messagebox.showerror('Check','Please check the Address field')
        elif len(Number_Entry.get()) < 1:
            messagebox.showerror('Check','Please check the Number field')
        elif len(booking_date_Entry.get()) < 1:
            messagebox.showerror('Check','Please check the History field')
        elif len(Old_Entry.get()) < 1:
            messagebox.showerror('Check','Please check the Age field')
        else:
            file = open(f'C:/Users/{os.getlogin()}/Documents/Databases/{Id_Entry.get()}.txt','w')
            file.write(f'''{Id_Entry.get()}
{Name_Entry.get()}
{Address_Entry.get()}
{Number_Entry.get()}
{booking_date_Entry.get()}
{Old_Entry.get()}''')
            Id_Entry.delete(0,END)
            Name_Entry.delete(0,END)
            Old_Entry.delete(0,END)
            Address_Entry.delete(0,END)
            Number_Entry.delete(0,END)
            ID_Text.config(text='ID')
            ID_Text.place_configure(x=1160, y=233)
            Name_Text.config(text='Full Name')
            Name_Text.place_configure(x=1130, y=307)
            Number_Text.config(text='Phone Number')
            Number_Text.place_configure(x=1115, y=457)
            Address_Text.config(text='Address')
            Address_Text.place_configure(x=1135, y=382)
            Old_Text.config(text='patient\'s age')
            Old_Text.place_configure(x=1123, y=607)
            CUID_Text.config(text='Delete a patient using an ID')
            CUID_Text.place_configure(x=70, y=520)
            file.close()
    def Logo(window, Logo_Image):
        Logo = Label(window, image=Logo_Image, bg='silver', border=0)
        Logo.pack(pady=20)
    def remove():
        if len(Id_Entry.get()) >= 1:
            ID_Text.config(text='')
            ID_Text.place_configure(x=0,y=0)
        else :
            ID_Text.config(text='ID')
            ID_Text.place_configure(x=1160, y=233)
        if len(Name_Entry.get()) >= 1:
            Name_Text.config(text='')
            Name_Text.place_configure(x=0,y=0)
        else :
            Name_Text.config(text='Full Name')
            Name_Text.place_configure(x=1133, y=307)
        if len(Number_Entry.get()) >= 1:
            Number_Text.config(text='')
            Number_Text.place_configure(x=0,y=0)
        else :
            Number_Text.config(text='Phone Number')
            Number_Text.place_configure(x=1115, y=457)
        if len(Address_Entry.get()) >= 1:
            Address_Text.config(text='')
            Address_Text.place_configure(x=0, y=0)
        else:
            Address_Text.config(text='Address')
            Address_Text.place_configure(x=1135, y=382)
        if len(Old_Entry.get()) >= 1:
            Old_Text.config(text='')
            Old_Text.place_configure(x=0, y=0)
        else:
            Old_Text.config(text='patient\'s age')
            Old_Text.place_configure(x=1123, y=607)
        if len(CUID_Entry.get()) >= 1:
            CUID_Text.config(text='')
            CUID_Text.place_configure(x=0, y=0)
        else:
            CUID_Text.config(text='Delete a patient using an ID')
            CUID_Text.place_configure(x=70, y=520)
        if len(Entry_Search.get()) >= 1:
            Search_Text.config(text='')
            Search_Text.place_configure(x=0,y=0)
        else:
            Search_Text.config(text='Search ID')
            Search_Text.place_configure(x=130,y=388)
    def Del():
        file = CUID_Entry.get()+'.txt'
        try:
            os.remove(f'C:/Users/{os.getlogin()}/Documents/Databases/{file}')
            CUID_Entry.delete(0,END)
            CUID_Text.config(text='Delete a patient using an ID')
            CUID_Text.place_configure(x=70, y=520)
        except FileNotFoundError:
            messagebox.showerror('Not Found','We sorry i can\'t found the ID')
    def Se():
        #Window Data
        ID = Entry_Search.get()+'.txt'
        Entry_Search.delete(0,END)
        Search_Text.config(text='Search ID')
        Search_Text.place_configure(x=130,y=388)
        path = 'C:/Users/{0}/Documents/Databases/'.format(os.getlogin())
        opened = False
        try:
            data = open(path+ID,'r').read().splitlines()
            opened = True
        except FileNotFoundError:
            messagebox.showerror('Toxic Code','Not Found ID')
            opened = False
        if opened == True:
            Window = Tk()
            Window.geometry('550x200')
            Window.minsize(550,200)
            ###############################################################################################
            widthWindow = Window.winfo_width()
            heightWindow = Window.winfo_height()
            print(widthWindow)
            #Window.resizable(False, False)
            Window.title('The Best Docktir')
            Window.config(background='silver')
            Window.iconbitmap(os.getcwd()+'\\src\\tooth.ico')
            tr = ttk.Treeview(Window,columns=('ID','Name','Addr','Num','time','Old'))
            tr.place(x=0,width=550,y=0,height=200)
            tr['show']='headings'
            tr.heading(column='ID',text='ID',anchor='center')
            tr.heading('Name',text='Name',anchor='center')
            tr.heading('Addr',text='Address',anchor='center')
            tr.heading('Num',text='Number',anchor='center')
            tr.heading('time',text='Histry',anchor='center')
            tr.heading('Old',text='Age',anchor='center')
            ################################################################################
            tr.column('ID',width=5,anchor='center')
            tr.column('Name',width=33,anchor='center')
            tr.column('Addr',width=40,anchor='center')
            tr.column('Num',width=30,anchor='center')
            tr.column('time',width=50,anchor='center')
            tr.column('Old',width=10,anchor='center')
            tr.delete(*tr.get_children())
            tr.insert("",END,values=data)
            Window.mainloop()
    def Buttons(window,ad,Del=Del,Se=Se):
        add = Button(window,image=Add_Image,border=0,bg='silver',activebackground='silver',command=ad)
        add.place(x=1110, y=678)
        add.bind("<Enter>",addF[0])
        add.bind("<Leave>",addF[1])
        search = Button(window,image=Search_Image,border=0,bg='silver',activebackground='silver',command=Se)
        search.place(x=123,y=310)
        search.bind("<Enter>",searchF[0])
        search.bind("<Leave>",searchF[1])
        delete = Button(window,image=Delete_Image,border=0,bg='silver',activebackground='silver',command=Del)
        delete.place(x=125, y=610)
        delete.bind("<Enter>",deleteF[0])
        delete.bind("<Leave>",deleteF[1])


    def Entrys_Searchs(window,Entry_Image,remove=remove):
        global Entry_Search
        Entry_image = Label(window, image=Entry_Image, bg='silver', border=0)
        Entry_Search = Entry(window,bg='silver',border=0,font='bold',justify='center')
        Entry_Search.place(x=104,y=385,width=125,height=26)
        Entry_Search.bind('<KeyRelease>',lambda e: remove())
        Entry_image.place(x=100,y=380)
    def Liabels(window,remove=remove):
        global ID_Text
        global Name_Text
        global Address_Text
        global Number_Text
        global Old_Text
        global CUID_Text
        global Search_Text
        ID_Text = Label(window,text='ID',fg='grey',bg='silver',border=0,font=5)
        ID_Text.place(x=1160, y=233)
        ID_Text.bind("<Button-1>",lambda e:Id_Entry.focus())
        Name_Text = Label(window,text='Full Name',fg='gray',bg='silver',font=5,border=0)
        Name_Text.place(x=1133, y=307)
        Name_Text.bind('<Button-1>',lambda e: Name_Entry.focus())
        Address_Text = Label(window,text='Address',fg='gray',bg='silver',font=5,border=0)
        Address_Text.place(x=1135, y=382)
        Address_Text.bind('<Button-1>',lambda e: Address_Entry.focus())
        Number_Text = Label(window,text='Phone Number',fg='gray',bg='silver',font=5,border=0)
        Number_Text.place(x=1115, y=457)
        Number_Text.bind('<Button-1>',lambda e: Number_Entry.focus())
        Old_Text = Label(window,text='patient\'s age',fg='grey',bg='silver',border=0,font=5,) 
        Old_Text.place(x=1123, y=607)
        Old_Text.bind('<Button-1>',lambda e: Old_Entry.focus())
        CUID_Text = Label(window,text='Delete a patient using an ID',fg='grey',bg='silver',border=0,font=5,)
        CUID_Text.place(x=70, y=520)
        CUID_Text.bind('<Button-1>',lambda e: CUID_Entry.focus())
        Search_Text = Label(window,text='Search ID',fg='grey',bg='silver',border=0,font=5,)
        Search_Text.place(x=130,y=388)
        Search_Text.bind('<Button-1>',lambda e:Entry_Search.focus())
    def Entrys_CAD(window,Entry_Image,remove=remove):
        #CUID
        #Close Using ID
        global CUID_Entry
        global Mony_Entry
        CUID_Image = Label(window, image=Entry_Image, bg='silver', border=0)
        CUID_Entry = Entry(window,bg='silver',justify='center',border=0)
        Mony_Entry = Entry(window,bg='silver',justify='center')
        #Show
        CUID_Image.place(x=100,y=550)
        CUID_Entry.place(x=106,y=553,width=121,height=30)
        CUID_Entry.bind('<KeyRelease>',lambda e: remove())
    def Entrys_Add(window,Entry_Image,remove=remove):
        now = datetime.now()
        global Id_Entry
        global Name_Entry
        global Number_Entry
        global booking_date_Entry
        global Old_Entry
        global Address_Entry
        Id_Image = Label(window, image=Entry_Image, bg='silver', border=0)
        Id_Entry = Entry(window,border=0,bg='silver',justify='center')
        Name_Image = Label(window, image=Entry_Image, bg='silver', border=0)
        Name_Entry = Entry(window,bg='silver',border=0)
        Address_Image = Label(window, image=Entry_Image, bg='silver', border=0)
        Address_Entry = Entry(window,bg='silver',border=0)
        Number_Image = Label(window, image=Entry_Image, bg='silver', border=0)
        Number_Entry = Entry(window,bg='silver',border=0,justify='center')
        booking_date_Image = Label(window, image=Entry_Image, bg='silver', border=0)
        booking_date_Entry = Entry(window,bg='silver',border=0,justify=CENTER)
        hour = now.hour
        if hour > 12:
            hour = hour %12
            booking_date_Entry.insert(0,f'{str(now.year)}/{now.month}/{str(now.day)}/{str(now.hour%12)}:{str(now.minute)} PM')
        else:
            booking_date_Entry.insert(0,f'{str(now.year)}/{now.month}/{str(now.day)}/{str(now.hour%12)}:{str(now.minute)} AM')
        
        Old_Image = Label(window, image=Entry_Image, bg='silver', border=0)
        Old_Entry = Entry(window,bg='silver',border=0,justify='center')
        #Show
        Id_Image.place(x=1100, y=225)
        Id_Entry.place(x=1106, y=228,width=121,height=30)
        Id_Entry.bind("<KeyRelease>",lambda e: remove())
        Name_Image.place(x=1100, y=300)
        Name_Entry.place(x=1106, y=303,width=121,height=30)
        Name_Entry.bind("<KeyRelease>",lambda e: remove())
        Address_Image.place(x=1100, y=375)
        Address_Entry.place(x=1106, y=378,width=121,height=30)
        Address_Entry.bind('<KeyRelease>',lambda e:remove())
        Number_Image.place(x=1100, y=450)
        Number_Entry.place(x=1106, y=453,width=121,height=30)
        Number_Entry.bind("<KeyRelease>",lambda e: remove())
        booking_date_Image.place(x=1100, y=525)
        booking_date_Entry.place(x=1106, y=528,width=121,height=30)
        Old_Image.place(x=1100, y=600)
        Old_Entry.place(x=1106, y=603,width=121,height=30)
        Old_Entry.bind("<KeyRelease>",lambda e: remove())
        
        
        
        
        
        
    def TreeViews(window):
        global ViewData
        Data_Frame = Frame(background='red')
        Scrolly = Scrollbar(Data_Frame,orient='vertical')
        Scrollx = Scrollbar(Data_Frame,orient='horizontal')
        Data_Frame.place(x=300,y=225,height=500,width=750)
        ViewData = ttk.Treeview(Data_Frame,columns=('ID','Name','Addr','Num','time','Old'),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        ViewData.place(x=17,y=0,width=733,height=483)
        Scrollx.config(command=ViewData.xview)
        Scrolly.config(command=ViewData.yview)
        ViewData['show']='headings'
        ViewData.heading('ID',text='ID',anchor='sw')
        ViewData.heading('Name',text='Name',anchor='center')
        ViewData.heading('Addr',text='Address',anchor='center')
        ViewData.heading('Num',text='Number',anchor='center')
        ViewData.heading('time',text='Histry',anchor='center')
        ViewData.heading('Old',text='Age')
        #######################################################
        ViewData.column('ID',width= 120)
        ViewData.column('Name',width=120)
        ViewData.column('Addr',width=120)
        ViewData.column('Num',width=120)
        ViewData.column('time',width=120)
        ViewData.column('Old',width=120)
        Scrollx.pack(side='bottom',fill='x')
        Scrolly.pack(side='left',fill='y')
        
        









    def View():
        f = ''
        path = 'C:/Users/{0}/Documents/Databases/'.format(os.getlogin())
        while True:
            for path,dirs,files in os.walk(path):
                if files == f:
                    pass
                else:
                    ViewData.delete(*ViewData.get_children())
                    for data in files:
                        data = open(f"{path}\\{data}",'r').read().splitlines()
                        ViewData.insert("",END,values=data)
                    f = files
            sleep(0.7)
            if Closed == True:
                break
            if c == True:
                exit()
            
        
        
        
        
        
        
        
        
    def __init__(self,on_closing=on_closing,View=View,Search_Enrtys=Entrys_Searchs,TreeViews=TreeViews,Entrys_CAD=Entrys_CAD, window_settings=window_settings, Logo=Logo, Entrys_Add=Entrys_Add, Buttons=Buttons, mohm=mohm,Liabels=Liabels):
        '''p = "C:/Users/{0}/Documents/time.tc"
        name = os.getlogin()
        patht = p.format(name)
        if os.path.exists(patht):
            file = open(patht,'r').read()
            global Closed
            try:
                if int(file) < datetime.now().day:
                    messagebox.showwarning('Shop','Please purchase the program from the developer to continue using it')
                    open_new_tab('https://t.me/Toxic_Code')
                    open_new_tab('https://www.facebook.com/toxiccode12')
                    Closed = True
                    exit()
            except ValueError:
                messagebox.showwarning('Shop','Please purchase the program from the developer to continue using it')
                open_new_tab('https://t.me/Toxic_Code')
                open_new_tab('https://www.facebook.com/toxiccode12')
                Closed = True
                exit()
        elif not os.path.exists(patht):
            mainpath = os.getcwd()
            os.chdir('C:/Users/{0}/Documents'.format(getlogin()))
            File = open(patht,'w')
            File.write(str(datetime.now().day))
            os.system("attrib +h time.tc")
            os.chdir(mainpath)
            File.close()'''
        self.window = Tk()
        path = os.getcwd()
        #Logo The Window
        Logo_Image = PhotoImage(file=path+'/src/tooth.png')
        Logo_Image =Logo_Image.subsample(4,4)
        Logo(self.window, Logo_Image)
        

        #Public varibales
        global Add_Image
        global Search_Image
        global Delete_Image
        global addF
        global searchF
        global deleteF
        global WindowMain
        WindowMain = self.window
        #Import Buttons Image
        Add_Image =PhotoImage(file=os.getcwd()+'\\src/Buttons/Add_Leave.png')
        Search_Image =PhotoImage(file=os.getcwd()+'\\src/Buttons/Search_Leave.png')
        Delete_Image =PhotoImage(file=os.getcwd()+'\\src/Buttons/Delete_Leave.png')
        #ADD BUTTON ANIMTION
        def Active_Add(e):
            Add_Image.configure(file='src/Buttons/Add_Activd.png')
        def Leave_Add(e):
            Add_Image.configure(file='src/Buttons/Add_Leave.png')
        addF = Active_Add,Leave_Add
        def Active_Search(e):
            Search_Image.configure(file='src/Buttons/Search_Active.png')
        def Leave_Search(E):
            Search_Image.configure(file='src/Buttons/Search_Leave.png')
        searchF = Active_Search,Leave_Search
        def Active_Delete(e):
            Delete_Image.configure(file='src/Buttons/Delete_Active.png')
        def Leave_Delete(E):
            Delete_Image.configure(file='src/Buttons/Delete_Leave.png')
        deleteF = Active_Delete,Leave_Delete
        #Window Propratez
        window_settings(self.window)
        Entry_Image =PhotoImage(file=os.getcwd()+'\\src/Entrys/Entry.png')
        Search_Enrtys(self.window,Entry_Image)
        #Entrys Adds
        Entrys_Add(self.window,Entry_Image)
        Buttons(self.window,mohm)
        Entrys_CAD(self.window,Entry_Image)
        Liabels(self.window)
        TreeViews(self.window)
        
        V = Thread(target=View,args=())
        V.start()
        self.window.protocol("WM_DELETE_WINDOW", on_closing)
        self.window.mainloop()
root = Main()
c = True
