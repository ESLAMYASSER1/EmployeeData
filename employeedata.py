from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.font import Font


root= Tk()
root.geometry("1000x540")
root.title("Employee Data")
root.iconbitmap("resourses/man.ico")
#vars
my_font = Font(
    family = 'Times',
    size = 20,
    weight = 'bold',
    slant = 'roman',
    underline = 0,
    overstrike = 0
)

age=IntVar()
phonecountry=StringVar()
#two classes for right frame 
class addemployee():
    def __init__(self):
        #clear rightframe
        try:
            rightframe.destroy()
        except:
            pass
        #add right frame
        rightframe = Frame(root,width=720,height=505,bg="#b8b9b9")
        rightframe.place(x=270,y=20)


        #create widgets 
        self.mlabel=Label(rightframe,text="Emplyee Data",font=("verdana bold",25),fg="#0e377b",bg="#b8b9b9")
        self.namelbl=Label(rightframe,text="Full Name:",font=my_font, bg="#b8b9b9")
        self.namein=Entry(rightframe,width=25,font=("new roman",15),bg="#73c9d4",fg="white",justify=CENTER)
        self.addresslbl=Label(rightframe,text="Address:",font=my_font,bg="#b8b9b9")
        self.addressin=Entry(rightframe,width=25,font=("new roman",15),bg="#73c9d4",fg="white",justify=CENTER)
        self.agelbl=Label(rightframe,text="Age:",font=my_font,bg="#b8b9b9")
        self.agevlbl=Label(rightframe,text=str(age.get()),font=my_font,bg="#b8b9b9",fg="#0044ff")
        self.agebar=Scale(rightframe,orient=HORIZONTAL,variable=age,command=self.ageview,bg="#ff5a5f")
        self.phonelbl=Label(rightframe,text="Phone Number:",font=my_font,bg="#b8b9b9")
        self.phonecountrycombo=ttk.Combobox(rightframe,width=27,textvariable=phonecountry,)
        self.phonecountrycombo["values"]=("AE","BH","EG","FR","IQ","JP","LB","RU","SA","US")
        self.phonecountrycombo.current(2)
        self.phonecountrycombo.bind("<<ComboboxSelected>>",self.changelabel)
        self.phonecodelbl=Label(rightframe,text="+20",font=my_font,bg="#b8b9b9")
        self.phonein=Entry(rightframe,width=15,font=("new roman",15),bg="#73c9d4",fg="white",justify=CENTER)
        self.idlbl=Label(rightframe,text="ID:",font=my_font,bg="#b8b9b9")
        self.idin=Entry(rightframe,width=15,font=("new roman",15),bg="#73c9d4",fg="white",justify=CENTER)
        self.addbttn=Button(rightframe,text="ADD",bg="#0e377b",font=("verdana bold",18),fg="white",command=self.addemployeedata)
        self.resetbtn=Button(rightframe,text="RESET",bg="#0e377b",font=("verdana bold",18),fg="white",command=addemployee)


        #add widgets to rightframe
        self.mlabel.place(x=230,y=10)
        self.namelbl.place(x=45,y=70)
        self.namein.place(x=50,y=110)
        self.addresslbl.place(x=380,y=70)
        self.addressin.place(x=390,y=110)
        self.agelbl.place(x=45,y=150)
        self.agevlbl.place(x=120,y=150)
        self.agebar.place(x=50,y=190,width=282)
        self.phonelbl.place(x=45,y=250)
        self.phonecountrycombo.place(x=240,y=260,width=40)
        self.phonecodelbl.place(x=280,y=250)
        self.phonein.place(x=340,y=255)
        self.idlbl.place(x=45,y=300)
        self.idin.place(x=90,y=305)
        self.addbttn.place(x=584,y=360)
        self.resetbtn.place(x=572,y=420)
#functions for command
    def ageview(self,age):
        self.agevlbl.config(text=str(age))

    def changelabel(self,event):
        selected = self.phonecountrycombo.get()
        if(selected=="EG"):
            self.phonecodelbl.config(text="+20")
        elif(selected=="SA"):
            self.phonecodelbl.config(text="+966")
        elif(selected=="AE"):
            self.phonecodelbl.config(text="+971")
        elif(selected=="US"):
            self.phonecodelbl.config(text="+1")
        elif(selected=="RU"):
            self.phonecodelbl.config(text="+7")
        elif(selected=="BH"):
            self.phonecodelbl.config(text="+973")
        elif(selected=="FR"):
            self.phonecodelbl.config(text="+33")
        elif(selected=="IQ"):
            self.phonecodelbl.config(text="+964")
        elif(selected=="JP"):
            self.phonecodelbl.config(text="+81")
        elif(selected=="LB"):
            self.phonecodelbl.config(text="+961")

    
    def addemployeedata(self):
        fullname=self.namein.get()
        address=self.addressin.get()
        nage=age.get()
        phonecodelbltxt=self.phonecodelbl["text"]
        phonenumber=self.phonein.get()
        id=self.idin.get()
        if fullname!="" and address!="" and age.get()!=0:
            try:
                int(phonenumber)
                int(id)
                try:
                    datafile=open("database/employeesdata.txt", "x")
                except:
                    pass
                datafile = open("database/employeesdata.txt", "r+")
                if phonecodelbltxt == "+20" and phonenumber[0] == "0":
                    nphonenumber = phonenumber[1:]
                else:
                    nphonenumber = phonenumber
                linelist = datafile.readlines()
                if linelist == []:
                    datafile.write(
                        f"{fullname} | {address} | {nage}  | {phonecodelbltxt}{nphonenumber or phonenumber} | {id}\n")
                else:
                    for line in linelist:
                        broken = False
                        for line in linelist:
                            if (line[:(line.index("|"))]).strip() == fullname.strip():
                                broken = True
                    if broken:
                        messagebox.showerror("Data Already Exist", f"{fullname}: Data is alrady added")
                    else:
                        datafile.write(
                            f"{fullname} | {address} | {nage}  | {phonecodelbltxt}{nphonenumber or phonenumber} | {id}\n")
            except Exception as e:
                print(e)
                messagebox.showerror("Not Valid INPUT","Please enter valid data")
        else:
            messagebox.showerror("fill all fields","Please enter data in all fields:\n-enter your age")
        addemployee()


class removeemployee():
    def __init__(self):
        #clear rightframe
        try:
            rightframe.destroy()
        except:
            pass
        #add right frame
        rightframe = Frame(root,width=720,height=505,bg="#b8b9b9")
        rightframe.place(x=270,y=20)


        #create widgets 
        self.namelbl=Label(rightframe,text="Search for Employee",font=("verdana bold",25),fg="#0e377b",bg="#b8b9b9")
        self.namesearchlbl=Label(rightframe,text="Enter Employee Name: ",font=my_font,bg="#b8b9b9")
        self.namesearchin=Entry(rightframe,width=25,font=("new roman",15),bg="#73c9d4",fg="white",justify=CENTER)
        self.searchbtn=Button(rightframe,text="Search",bg="#0e377b",font=("verdana bold",18),fg="white",command=self.searchemployee)
        self.employeedatalbl=Label(rightframe,text="Employee Data:",font=my_font,bg="#b8b9b9")
        self.viewnamelbl=Label(rightframe,text="Name:",font=my_font,bg="#b8b9b9")
        self.viewaddresslbl=Label(rightframe,text="Address:",font=my_font,bg="#b8b9b9")
        self.viewagelbl=Label(rightframe,text="Age:",font=my_font,bg="#b8b9b9")
        self.viewphonelbl=Label(rightframe,text="Phone Number:",font=my_font,bg="#b8b9b9")
        self.viewidlbl=Label(rightframe,text="ID:",font=my_font,bg="#b8b9b9")
        self.datanamelbl=Entry(rightframe,font=my_font,bg="#b8b9b9",fg="#0044ff",borderwidth=0)
        self.dataaddresslbl=Entry(rightframe,font=my_font,bg="#b8b9b9",fg="#0044ff",borderwidth=0)
        self.dataagelbl=Entry(rightframe,font=my_font,bg="#b8b9b9",fg="#0044ff",borderwidth=0)
        self.dataphonelbl=Entry(rightframe,font=my_font,bg="#b8b9b9",fg="#0044ff",borderwidth=0)
        self.dataidlbl=Entry(rightframe,font=my_font,bg="#b8b9b9",fg="#0044ff",borderwidth=0)

        self.editbtn=Button(rightframe,text="Edit",bg="#0e377b",font=("verdana bold",18),fg="white",command=self.editemployeedata)
        self.removebtn=Button(rightframe,text="Remove",bg="#0e377b",font=("verdana bold",18),fg="white",command=self.removeemployees)
        #add widgets to rightframe
        self.namelbl.place(x=180,y=10)
        self.namesearchlbl.place(x=45,y=70)
        self.namesearchin.place(x=50,y=110)
        self.searchbtn.place(x=550,y=88)
        self.employeedatalbl.place(x=45,y=252)
        self.viewnamelbl.place(x=320,y=170)
        self.viewaddresslbl.place(x=320,y=210)
        self.viewagelbl.place(x=320,y=250)
        self.viewphonelbl.place(x=320,y=290)
        self.viewidlbl.place(x=320,y=330)
        self.datanamelbl.place(x=400,y=170)
        self.dataaddresslbl.place(x=430,y=210)
        self.dataagelbl.place(x=380,y=250)
        self.dataphonelbl.place(x=510,y=290)
        self.dataidlbl.place(x=365,y=330)

        self.editbtn.place(x=580,y=370)
        self.removebtn.place(x=555,y=430)

        #function for Buttons
    def searchemployee(self):   #search function
        try:
            name = self.namesearchin.get()
            datafile = open("database/employeesdata.txt", "r")
            linelist = datafile.readlines()
            for line in linelist:
                try:
                    if line[:(line.index("|"))].strip() == name.strip():
                        wantedemployee = line
                except:
                    pass
            datalist = wantedemployee.split("|")
            wname = datalist[0].strip()
            waddress = datalist[1].strip()
            wage = datalist[2].strip()
            wphonenumber = datalist[3].strip()
            wid = datalist[4]
            self.datanamelbl.delete(0,END)
            self.dataaddresslbl.delete(0,END)
            self.dataagelbl.delete(0,END)
            self.dataphonelbl.delete(0,END)
            self.dataidlbl.delete(0,END)
            self.datanamelbl.insert(0,wname)
            self.dataaddresslbl.insert(0,waddress)
            self.dataagelbl.insert(0,wage )
            self.dataphonelbl.insert(0,wphonenumber)
            self.dataidlbl.insert(0,wid)
        except:
            messagebox.showerror("NOT Exist","Employee Data Not Exist in our information\nPlease Add them first")


    def removeemployees(self):
        try:
            with open("database/employeesdata.txt", "r") as f:
                lines = f.readlines()
                name = self.namesearchin.get()
                for line in lines:
                    if line[:(line.index("|"))].strip() == name.strip():
                        wantedemployee = line
            with open("database/employeesdata.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != wantedemployee.strip("\n"):
                        f.write(line)
            removeemployee()
        except:
            messagebox.showerror("Not Exist","Make sure data is exist by using 'search'")

    def editemployeedata(self):
        with open("database/employeesdata.txt", "r") as f:
            lines = f.readlines()
            name = self.namesearchin.get()
            for line in lines:
                if line[:(line.index("|"))].strip() == name.strip():
                    wantedemployee = line
        with open("database/employeesdata.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != wantedemployee.strip("\n"):
                    f.write(line)
            editable_data = wantedemployee.split("|")
            editable_name = self.datanamelbl.get().strip()
            editable_adress = self.dataaddresslbl.get().strip()
            editable_age = self.dataagelbl.get().strip()
            editable_phone = self.dataphonelbl.get().strip()
            editable_id = self.dataidlbl.get().strip("\n")
            self.namesearchin.delete(0,END)
            self.namesearchin.insert(0,editable_name)
            f.write(
                f"{editable_name} | {editable_adress} | {editable_age}  | {editable_phone} | {editable_id}\n")



#start with add employee
addemployee()
# create main widgets
leftframe = Frame(root,width=250,height=505,bg="#181b1e")

# create buttons to move between to classes
addbtn = Button(leftframe,width=15,height=1,text="Add Employee",fg="#434647",bg="#181b1e",borderwidth=0,font=("Arial",15),cursor="tcross",command=addemployee)
addiconimg=ImageTk.PhotoImage(Image.open("resourses/add.png"))
addiconlabel = Label(leftframe,image=addiconimg,width=30,height=32,bg="#181b1e")
removebtn = Button(leftframe,width=15,height=2,text="Edit, Remove\nEmployee",fg="#434647",bg="#181b1e",borderwidth=0,font=("Arial",15),cursor="pirate",command=removeemployee)
removeiconimg=ImageTk.PhotoImage(Image.open("resourses/remove.png"))
removeiconlabel = Label(leftframe,image=removeiconimg,width=30,height=32,bg="#181b1e")

# create developer info section
separator=ttk.Separator(leftframe,orient=HORIZONTAL )
devimg=ImageTk.PhotoImage(Image.open("resourses/devimg.png"))
devimglabel=Label(leftframe,image=devimg,width=60,height=87,bg="#181b1e")
namelabel=Label(leftframe,text="Eslam Yasser",font=("Arial Bold",14),fg="#ffffff",bg="#181b1e")
devinflabel1=Label(leftframe,text="+201018410318",font=("Arial Bold",10),fg="#aaaaaa",bg="#181b1e")
devinflabel2=Label(leftframe,text="eng.eslam.yasser.1@gmail.com",font=("Arial Bold",8),fg="#999999",bg="#181b1e")

# add buttons to move between to classes to left frame
addbtn.place(x=50,y=100)
addiconlabel.place(x=20,y=100)
removebtn.place(x=60,y=180)
removeiconlabel.place(x=20,y=195)

# add developer info section to left frame
separator.place(x=0,y=400,relwidth=200)
devimglabel.place(x=5,y=420)
namelabel.place(x=70,y=420)
devinflabel1.place(x=70,y=450)
devinflabel2.place(x=70,y=470)

# add main widget to root
leftframe.place(x=10,y=20)





#run the app

root.mainloop()