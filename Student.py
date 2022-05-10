def addstudents():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions','Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications','Id Already Exist try another id...',parent=addroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    addroot = Toplevel(master=dataentryframe)
    addroot.grab_set()
    addroot.resizable(False,False)
    addroot.geometry('470x470+220+200')
    addroot.title('Add student')
    addroot.config(bg='black')

    #--------------------labels------------------
    idlabel = Label(addroot,text='Enter Id : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot,text='Enter Address : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text='Enter D.O.B : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    #------------Entery wid----------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    #-------------------button
    submitbtn = Button(addroot,text='Submit',font=('times',15,'bold'),width=20,bd=5,activebackground='#ff101f',activeforeground='black',fg="#ff101f",
                      bg='black',command=submitadd)
    submitbtn.place(x=150,y=420)
    addroot.mainloop()
def searchtstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if (id!=''):
            str1="select * from studentdata1 where id=%s"
            mycursor.execute(str1,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in  datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
               studenttable.insert('',END,values=vv)
        elif (name!=''):
            str1="select * from studentdata1 where name=%s"
            mycursor.execute(str1,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in  datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
               studenttable.insert('',END,values=vv)
        elif (mobile!=''):
            str1="select * from studentdata1 where mobile=%s"
            mycursor.execute(str1,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in  datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
               studenttable.insert('',END,values=vv)
        elif (email!=''):
            str1="select * from studentdata1 where email=%s"
            mycursor.execute(str1,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in  datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
               studenttable.insert('',END,values=vv)
        elif (address!=''):
            str1="select * from studentdata1 where address=%s"
            mycursor.execute(str1,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in  datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
               studenttable.insert('',END,values=vv)
        elif (gender!=''):
            str1="select * from studentdata1 where gender=%s"
            mycursor.execute(str1,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in  datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
               studenttable.insert('',END,values=vv)
        elif (dob!=''):
            str1="select * from studentdata1 where dob=%s"
            mycursor.execute(str1,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in  datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
               studenttable.insert('',END,values=vv)
        elif (addeddate!=''):
            str1="select * from studentdata1 where date=%s"
            mycursor.execute(str1,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in  datas:
               vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
               studenttable.insert('',END,values=vv)


        
        
            
        
    searchroot = Toplevel(master=dataentryframe)
    searchroot.grab_set()
    searchroot.resizable(False,False)
    searchroot.geometry('470x470+220+200')
    searchroot.title('Search student')
    searchroot.config(bg='black')

    #--------------------labels------------------
    idlabel = Label(searchroot,text='Enter Id : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Name : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text='Enter Mobile : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text='Enter Email : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(searchroot,text='Enter Address : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text='Enter Gender : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(searchroot,text='Enter D.O.B : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    #------------Entery wid----------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    #-------------------button
    submitbtn = Button(searchroot,text='Submit',font=('times',15,'bold'),width=20,bd=5,activebackground='#ff101f',activeforeground='black',fg="#ff101f",
                      bg='black',command=search)
    submitbtn.place(x=150,y=420)
    searchroot.mainloop()

def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)
def updatestud():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()
        strr="update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s"
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showerror('Notifications','Id {} Modified ...',parent=updateroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    updateroot = Toplevel(master=dataentryframe)
    updateroot.grab_set()
    updateroot.resizable(False,False)
    updateroot.geometry('470x600+220+200')
    updateroot.title('Update student')
    updateroot.config(bg='black')
    #--------------------labels------------------
    idlabel = Label(updateroot,text='Enter Id : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text='Enter Name : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text='Enter Mobile : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text='Enter Email : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(updateroot,text='Enter Address : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text='Enter Gender : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(updateroot,text='Enter D.O.B : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(updateroot,text='Enter Date : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel = Label(updateroot,text='Enter Time : ',bg='black',fg="#ff101f",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)

    #------------Entery wid----------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=dateval)
    timeentry.place(x=250,y=490)

    #-------------------button
    submitbtn = Button(updateroot,text='Submit',font=('times',15,'bold'),width=20,bd=5,activebackground='#ff101f',activeforeground='black',fg="#ff101f",
                      bg='black',command=update)
    submitbtn.place(x=140,y=540)
    ff = studenttable.focus()
    content = studenttable.item(ff)
    dd = content['values']
    if(len(dd) != 0):
        idval.set(dd[0])
        nameval.set(dd[1])
        mobileval.set(dd[2])
        emailval.set(dd[3])
        addressval.set(dd[4])
        genderval.set(dd[5])
        dobval.set(dd[6])
        dateval.set(dd[7])
        timeval.set(dd[8])
    updateroot.mainloop()
def showstudent():
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)
def exit():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
        root.destroy()
def exportstud():
     ask_file=filedialog.asksaveasfilename()
     gg=studenttable.get_children()
     id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
     for i in gg:
         content=studenttable.item(i)
         pp=content["values"]
         id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
         dd=['Id','Name','Mobile','Email','Address','Gender','dob','addeddate','addedtime']
         df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
         paths=r"{}.csv".format(ask_file)
         df.to_csv(paths,index=False)
         messagebox.showinfo('Notification','Student data saved {}'.format(paths))
      
def connectdb():
    def connectdbs():
        global con,mycursor
        host = host1.get()
        user = user1.get()
        password = pass1.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected connected to the database ....',parent=dbroot)

        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database ....',parent=dbroot)
        dbroot.destroy()


    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.config(bg="black")
    dbroot.resizable(False,False)
    #============================lables
    hostl=Label(dbroot,text="HOST :",font=("times",20,"bold"),relief=GROOVE,bg="black",bd=4,width=10,fg="#ff101f",anchor=W)
    hostl.place(x=5,y=5)

    userl=Label(dbroot,text="USER :",font=("times",20,"bold"),relief=GROOVE,bg="black",bd=4,width=10,fg="#ff101f",anchor=W)
    userl.place(x=5,y=60)

    passl=Label(dbroot,text="PASS :",font=("times",20,"bold"),relief=GROOVE,bg="black",bd=4,width=10,fg="#ff101f",anchor=W)
    passl.place(x=5,y=120)

    #===================TEXT
    host1=StringVar()
    user1=StringVar()
    pass1=StringVar()
    hoste=Entry(dbroot,font=("times", 20,"bold italic"),textvariable=host1,width=17,relief=RIDGE,bd=4)
    hoste.place(x=190,y=5)

    usere=Entry(dbroot,font=("times", 20,"bold italic"),textvariable=user1,width=17,relief=RIDGE,bd=4)
    usere.place(x=190,y=60)

    passe=Entry(dbroot,font=("times", 20,"bold italic"),show="*",textvariable=pass1,width=17,relief=RIDGE,bd=4)
    passe.place(x=190,y=120)

    subbtn=Button(dbroot,text="CONNECT",font=('times', 17 ,'bold'),width=17,relief=GROOVE,background='black',foreground='#ff101f',bd=6,
               activebackground="#ff101f",activeforeground="black",command=connectdbs)
    subbtn.place(x=100,y=190)


    dbroot.mainloop()
def time1():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d:%m:%y")
    clock.config(text="Time :"+time_string+"\n"+"Date :"+date_string)
    clock.after(200,time1)
#-======================
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog 
from tkinter import ttk
from tkinter.ttk import Style, Treeview
import pymysql
import pandas
import  time
root=Tk()
root.title("Student managenment system")
root.configure(bg="black")
root.geometry("1174x700+200+50")
root.resizable(False,False)

#==============================
dataentryframe=Frame(root,bg="black",relief=GROOVE,borderwidth=5)
dataentryframe.place(x=15,y=15,width=300,height=673)

clock=Label(dataentryframe,font=('time', 25,'bold'),relief=GROOVE,background='black',foreground='#ff101f')
clock.place(x=20,y=5,width=250)
time1()


#----------------------------
addbtn=Button(dataentryframe,text="1. Add student",font=('times', 17 ,'bold'),width=17,relief=GROOVE,background='black',foreground='#ff101f',bd=6,
               activebackground="#ff101f",activeforeground="black",command=addstudents)
addbtn.place(x=10,y=100)

searchbtn=Button(dataentryframe,text="2. Search student",font=('times', 17 ,'bold'),width=17,relief=GROOVE,background='black',foreground='#ff101f',bd=6,
               activebackground="#ff101f",activeforeground="black",command=searchtstudent)
searchbtn.place(x=10,y=170)

updatebtn=Button(dataentryframe,text="3. Update student",font=('times', 17 ,'bold'),width=17,relief=GROOVE,background='black',foreground='#ff101f',bd=6,
               activebackground="#ff101f",activeforeground="black",command=updatestud)
updatebtn.place(x=10,y=240)

showbtn=Button(dataentryframe,text="4. Show student",font=('times', 17 ,'bold'),width=17,relief=GROOVE,background='black',foreground='#ff101f',bd=6,
               activebackground="#ff101f",activeforeground="black",command=showstudent)
showbtn.place(x=10,y=310)

deletebtn=Button(dataentryframe,text="5. Delete student",font=('times', 17 ,'bold'),width=17,relief=GROOVE,background='black',foreground='#ff101f',bd=6,
               activebackground="#ff101f",activeforeground="black",command=deletestudent)
deletebtn.place(x=10,y=380)

exportbtn=Button(dataentryframe,text="6. Export student",font=('times', 17 ,'bold'),width=17,relief=GROOVE,background='black',foreground='#ff101f',bd=6,
               activebackground="#ff101f",activeforeground="black",command=exportstud)
exportbtn.place(x=10,y=450)

exitbtn=Button(dataentryframe,text="7. Exit ",font=('times', 17 ,'bold'),width=17,relief=GROOVE,background='black',foreground='#ff101f',bd=6,
               activebackground="#ff101f",activeforeground="black",command=exit)
exitbtn.place(x=10,y=520)

connectdbbtn=Button(dataentryframe,text="Connect to DB",font=('times', 17 ,'bold'),width=17,relief=GROOVE,background='black',foreground='#ff101f',bd=6,
               activebackground="#ff101f",activeforeground="black",command=connectdb)
connectdbbtn.place(x=10,y=590)



#================================
showdataframe=Frame(root,bg="black",relief=GROOVE,borderwidth=5)
showdataframe.place(x=340,y=140,width=800,height=547)

style= ttk.Style()
style.theme_use("clam")
style.configure('Treeview.Heading',font=('times',20,'bold'),foreground="white",background="black")
style.configure('Treeview',font=('times'),fg="white",fieldbackground="black")
scroll_x=Scrollbar(showdataframe,orient=HORIZONTAL,background="black",)
scroll_y=Scrollbar(showdataframe,orient=VERTICAL,background="black")
studenttable=Treeview(showdataframe,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                       yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

studenttable.heading('Id',text="ID")
studenttable.heading('Name',text="NAME")
studenttable.heading('Mobile No',text="MOBILE NO")
studenttable.heading('Email',text="EMAIL")
studenttable.heading('Address',text="ADDRESS")
studenttable.heading('Gender',text="GENDER")
studenttable.heading('D.O.B',text="D.O.B")
studenttable.heading('Added Date',text="ADDED DATE")
studenttable.heading('Added Time',text="ADDED TIME")
studenttable['show']='headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=200)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=150)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=2)


#==============================
titledataframe=Frame(root,bg="black",relief=GROOVE,borderwidth=5)
titledataframe.place(x=340,y=15,width=800,height=100)

title=Label(titledataframe,text="  Student Management System",font=('times', 35 ,'bold'),foreground='#ff101f',background='black',width=25)
title.place(x=17,y=15)
root.mainloop()