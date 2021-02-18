from tkinter import*
from tkinter import messagebox
import mysql.connector as mysql
from tkinter import ttk



#----Exit Window----
def window():
    win.destroy()


#------Window----
win=Tk()
win.title("Library System")
win.geometry('990x650+200+15')
win.resizable(False,False)
win.config(bg="#70a9a9")
win.iconbitmap(r'bookshelf+library+icon.ico')

def back_dashboard():
    dashboard()

def Add_Book():
    def add_details():
        def win_destroy():
            win2.destroy()


        def Delete():
            by1.delete(0,'end')
            by2.delete(0,'end')
            by3.delete(0,'end')
            by4.delete(0,'end')
            by5.delete(0,'end')

        Id = by1.get()
        TITLE = by2.get()
        AUTHOR = by3.get()
        EDITION = by4.get()
        TOTAL = by5.get()

        if Id == "" or TITLE == "" or AUTHOR == "" or EDITION == "" or TOTAL == "":
            win2 = Toplevel(win)
            win2.title("Insert Status")
            win2.resizable(False,False)
            win2.geometry("300x120+500+320")

            lu1 = Label(win2,image="::tk::icons::error")
            lu1.place(x=40,y=20)
            lu2 = Label(win2,text="All Fields are required")
            lu2.place(x=90,y=25)

            bu1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
            bu1.place(x=180,y=80)
            win2.mainloop()

        else:
            flg=0
            conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
            cursor = conn.cursor()
            cursor.execute("SELECT `Book ID` ,`Title`  FROM `book_details` where `Book ID`=" + Id)
            for (I,T) in cursor:
                if str(I) == (Id):
                    flg = 1

            cursor.close()
            if flg==1:
                win2 = Toplevel(win)
                win2.title("Error")
                win2.resizable(False,False)
                win2.geometry("250x120+500+320")

                Lu1 = Label(win2,image="::tk::icons::error")
                Lu1.place(x=40,y=20)
                Lu2 = Label(win2,text="ID is already Exist!!")
                Lu2.place(x=90,y=25)

                B1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
                B1.place(x=90,y=80)
                win2.mainloop()
            else:
                conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")

                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO `book_details`(`Book ID`, `Title`, `Author`, `Edition`, `Total`) VALUES('" + Id + "','" + TITLE + "','" + AUTHOR + "','" + EDITION + "','" + TOTAL + "')")
                cursor.execute("commit")
                cursor.close()

                win2 = Toplevel(win)
                win2.title("Add Books")
                win2.resizable(False,False)
                win2.geometry("300x120+500+320")

                lu2 = Label(win2,image="::tk::icons::information")
                lu2.place(x=40,y=20)
                lu3 = Label(win2,text="Inserted Successfully")
                lu3.place(x=90,y=25)

                bu2 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
                bu2.place(x=180,y=80)
                Delete()
                by1.focus()
                win2.mainloop()


    f2 = Frame(bg="#8fbcbc")
    f2.place(x=0,y=0,width=990,height=650)

    f3=Frame(f2,bg="#396060")
    f3.place(x=0,y=0,width=990,height=90)

    l= Label(f3,text="Pikachu Library",font=('veranda',45,'bold'),bg='#396060',fg='#F5FFFA')
    l.place(x=280,y=5)

    wh=Frame(f2,bg="#F5FFFA")
    wh.place(x=0,y=90,width=990,height=30)

    f4=Frame(f2,bg="#F5FFFA")
    f4.place(x=200,y=150,width=600,height=460)

    f5=Frame(f4,bg="#396060")
    f5.place(x=0,y=0,width=600,height=50)

    l1=Label(f5,text="Add Book Details",font=('veranda',25,'bold'),bg="#396060",fg='#F5FFFA')
    l1.place(x=170,y=2)

    id = StringVar()
    title = StringVar()
    author = StringVar()
    edition = StringVar()
    total = StringVar()

    ID = Label(f4,text="Book ID",font=('veranda',10,'bold'),bg="#F5FFFA")
    ID.place(x=60,y=100)

    by1 = Entry(f4,textvariable=id,bd=1,font=('Arial',15,'bold'),bg="white",border=2,relief=GROOVE)
    by1.place(x=180,y=100,height=25,width=300)

    Title = Label(f4,text="Title",font=('veranda',10,'bold'),bg="#F5FFFA")
    Title.place(x=60,y=160)

    by2 = Entry(f4,textvariable=title,bd=1,font=('Arial',15,'bold'),bg="white",border=2,relief=GROOVE)
    by2.place(x=180,y=160,height=25,width=300)

    Author = Label(f4,text="Author",font=('veranda',10,'bold'),bg="#F5FFFA")
    Author.place(x=60,y=220)

    by3 = Entry(f4,textvariable=author,bd=1,font=('Arial',15,'bold'),bg="white",border=2,relief=GROOVE)
    by3.place(x=180,y=220,height=25,width=300)

    Edition = Label(f4,text="Edition",font=('veranda',10,'bold'),bg="#F5FFFA")
    Edition.place(x=60,y=280)

    by4 = Entry(f4,textvariable=edition,bd=1,font=('Arial',15,'bold'),bg="white",border=2,relief=GROOVE)
    by4.place(x=180,y=280,height=25,width=300)

    Total = Label(f4,text="Total Books",font=('veranda',10,'bold'),bg="#F5FFFA")
    Total.place(x=60,y=340)

    by5 = Entry(f4,textvariable=total,bd=1,font=('Arial',15,'bold'),bg="white",border=2,relief=GROOVE)
    by5.place(x=180,y=340,height=25,width=300)

    Submit = Button(f4,text='Submit',height=1,width=20,font=('veranda',12,'bold'),bg="#3366ff",fg="white",command=add_details)
    Submit.place(x=220,y=390)

    De1 = Button(f2,text='<Back',height=1,width=8,font=('veranda',12,'bold'),bg="#396060",fg="white",command=back_dashboard)
    De1.place(x=10,y=140)

    by1.focus()


def Delete():
    def DEL():
        def win_destroy():
            win2.destroy()

        B_ID = dy1.get()
        B_Name = dy2.get()

        if B_ID == "" and B_Name == "":
            win2 = Toplevel(win)
            win2.title("Insert ID")
            win2.resizable(False,False)
            win2.geometry("300x120+500+320")

            lu1 = Label(win2,image="::tk::icons::error")
            lu1.place(x=40,y=20)
            lu2 = Label(win2,text="Book ID or Book Name is required")
            lu2.place(x=90,y=25)

            bu1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
            bu1.place(x=180,y=80)
            win2.mainloop()
        elif B_ID != "":
            flg_id = 0
            conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
            cursor = conn.cursor()
            cursor.execute("SELECT `Book ID` ,`Title` FROM `book_details` where `Book ID`=" + B_ID)
            for (I,T) in cursor:
                if str(I) == (B_ID):
                    flg_id = 1
            cursor.close()

            if flg_id == 0:
                win2 = Toplevel(win)
                win2.title("Error")
                win2.resizable(False,False)
                win2.geometry("300x120+500+320")

                Lu1 = Label(win2,image="::tk::icons::error")
                Lu1.place(x=40,y=20)
                Lu2 = Label(win2,text="Book ID is not found")
                Lu2.place(x=90,y=25)

                B1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
                B1.place(x=180,y=80)
                win2.mainloop()
            else:
                conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM `book_details` WHERE `Book ID`='" + B_ID + "'")
                cursor.execute("commit")
                cursor.close()

                win2 = Toplevel(win)
                win2.title("Delete Book")
                win2.resizable(False,False)
                win2.geometry("300x120+500+320")

                Lu1 = Label(win2,image="::tk::icons::information")
                Lu1.place(x=40,y=20)
                Lu2 = Label(win2,text="Deleted Successfully")
                Lu2.place(x=90,y=25)

                B1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
                B1.place(x=180,y=80)
                dy1.delete(0,'end')
                win2.mainloop()

        else:
            flg_name = 0
            conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
            cursor = conn.cursor()
            cursor.execute("SELECT `Book ID` ,`Title` FROM `book_details` where `Title`= '" + B_Name + "'")
            for (I,T) in cursor:
                if T.upper() == B_Name.upper():
                    flg_name = 1
            cursor.close()

            if flg_name == 0:
                win2 = Toplevel(win)
                win2.title("Error")
                win2.resizable(False,False)
                win2.geometry("300x120+500+320")

                Lu1 = Label(win2,image="::tk::icons::error")
                Lu1.place(x=40,y=20)
                Lu2 = Label(win2,text="Book Name is not found")
                Lu2.place(x=90,y=25)

                B1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
                B1.place(x=180,y=80)
                win2.mainloop()

            else:
                conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM `book_details` WHERE `Book ID`='" + B_Name + "'")
                cursor.execute("commit")
                cursor.close()

                win2 = Toplevel(win)
                win2.title("Delete Book")
                win2.resizable(False,False)
                win2.geometry("300x120+500+320")

                Lu1 = Label(win2,image="::tk::icons::information")
                Lu1.place(x=40,y=20)
                Lu2 = Label(win2,text="Deleted Successfully")
                Lu2.place(x=90,y=25)

                B1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
                B1.place(x=180,y=80)
                dy2.delete(0,'end')
                win2.mainloop()

    f2 = Frame(bg="#8fbcbc")
    f2.place(x=0,y=0,width=990,height=650)

    f3 = Frame(f2,bg="#396060")
    f3.place(x=0,y=0,width=990,height=90)

    l = Label(f3,text="Pikachu Library",font=('veranda',45,'bold'),bg='#396060',fg='#F5FFFA')
    l.place(x=280,y=5)

    wh = Frame(f2,bg="#F5FFFA")
    wh.place(x=0,y=90,width=990,height=30)

    f4 = Frame(f2,bg="#F5FFFA")
    f4.place(x=200,y=180,width=600,height=400)

    f5 = Frame(f4,bg="#396060")
    f5.place(x=0,y=0,width=600,height=50)

    l1 = Label(f5,text="Delete Book",font=('veranda',25,'bold'),bg="#396060",fg='#F5FFFA')
    l1.place(x=200,y=2)

    delete_ID = StringVar()
    delete_name = StringVar()

    d_ID = Label(f4,text="Book ID",font=('veranda',10,'bold'),bg="#F5FFFA")
    d_ID.place(x=60,y=100)

    dy1 = Entry(f4,textvariable=delete_ID,bd=1,font=('Arial',15,'bold'),border=2,bg="white",relief=GROOVE)
    dy1.place(x=180,y=100,height=25,width=300)

    Or = Label(f4,text='Or',font=('veranda',12,'bold'),bg="#F5FFFA",fg="#B22222")
    Or.place(x=310,y=150)

    d_name = Label(f4,text="Book Name",font=('veranda',10,'bold'),bg="#F5FFFA")
    d_name.place(x=60,y=200)

    dy2 = Entry(f4,textvariable=delete_name,bd=1,font=('Arial',15,'bold'),border=2,bg="white",relief=GROOVE)
    dy2.place(x=180,y=200,height=25,width=300)

    De1 = Button(f2,text='<Back',height=1,width=10,font=('veranda',12,'bold'),bg="#396060",fg="white",
                 command=back_dashboard)
    De1.place(x=10,y=140)

    De = Button(f4,text='Delete',height=1,width=25,font=('veranda',12,'bold'),bg="#396060",fg="white",command=DEL)
    De.place(x=190,y=280)


    dy1.focus()

def Views():
    f2 = Frame(bg="#8fbcbc")
    f2.place(x=0,y=0,width=990,height=650)

    f3 = Frame(f2,bg="#396060")
    f3.place(x=0,y=0,width=990,height=90)

    l = Label(f3,text="Pikachu Library",font=('veranda',45,'bold'),bg='#396060',fg='#F5FFFA')
    l.place(x=280,y=5)

    wh = Frame(f2,bg="#F5FFFA")
    wh.place(x=0,y=90,width=990,height=90)

    f4 = Frame(f2,bg="#F5FFFA")
    f4.place(x=0,y=133,width=990,height=520)

    f5 = Frame(f4,bg="#396060")
    f5.place(x=0,y=0,width=990,height=50)

    l1 = Label(f5,text="All Book Details",font=('veranda',25,'bold'),bg="#396060",fg='#F5FFFA')
    l1.place(x=360,y=0)

    scroll_bar = Scrollbar(f4,orient=VERTICAL)

    style = ttk.Style()
    style.theme_use('alt')
    style.configure(".",font=('veranda',10))
    style.configure("Treeview.Heading",font=('veranda',12,'bold'),foreground='black',background="#6495ED")
    style.configure("Treeview",rowheight=20,foreground="back",background="#D3D3D3",fieldbackground="#D3D3D3")
    style.map('Treeview',background=[('selected','#4169E1')])

    book_table = ttk.Treeview(f4,columns=("Book ID","Title","Author","Edition","Total Books"),
                              yscrollcommand=scroll_bar.set)

    scroll_bar.place(x=970,y=50,height=470)
    scroll_bar.config(command=book_table.yview)

    book_table.heading("Book ID",text="Book ID")
    book_table.heading("Title",text="Title")
    book_table.heading("Author",text="Author")
    book_table.heading("Edition",text="Edition")
    book_table.heading("Total Books",text="Total Books")

    book_table.column("Book ID",width=198)
    book_table.column("Title",width=198)
    book_table.column("Author",width=198)
    book_table.column("Edition",width=198)
    book_table.column("Total Books",width=198)

    book_table['show'] = 'headings'
    book_table.place(x=0,y=50,height=460,width=970)

    conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
    cursor = conn.cursor()
    cursor.execute("SELECT `Book ID`, `Title`, `Author`, `Edition`, `Total` FROM `book_details` ")

    for (B,T,A,E,TO) in cursor:
        book_table.insert('',END,values=(B,T,A,E,TO))

    cursor.close()
    De1 = Button(f2,text='<Back',height=1,width=8,font=('veranda',12,'bold'),bg="#F5FFFA",fg="RED",
                 command=back_dashboard,relief=FLAT,activebackground="#F5FFFA")
    De1.place(x=0,y=92)


def Search():
    def SEARCH():
        def win_destroy():
            win2.destroy()

        def OK():
            win_in.destroy()

        B_ID = dy1.get()
        B_name = dy2.get()

        if B_ID == "" and B_name == "":
            win2 = Toplevel(win)
            win2.title("Insert ID")
            win2.resizable(False,False)
            win2.geometry("300x120+500+320")

            lu1 = Label(win2,image="::tk::icons::error")
            lu1.place(x=40,y=20)
            lu2 = Label(win2,text="Book ID or Book Name is required")
            lu2.place(x=90,y=25)

            bu1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
            bu1.place(x=180,y=80)
            win2.mainloop()

        elif B_ID != "":
            title = ""
            author = ""
            Total = 0
            flg = 0
            conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
            cursor = conn.cursor()
            cursor.execute("SELECT `Book ID` ,`Title` ,`Author`,`Total` FROM `book_details` where `Book ID`=" + B_ID)
            for (I,T,A,total) in cursor:
                if str(I) == (B_ID):
                    flg = 1
                    title = T
                    author = A
                    Total = total

            cursor.close()
            if flg == 0 or Total == 0:
                win2 = Toplevel(win)
                win2.title("Search")
                win2.resizable(False,False)
                win2.geometry("390x120+500+320")

                Lu1 = Label(win2,image="::tk::icons::warning")
                Lu1.place(x=40,y=20)
                Lu2 = Label(win2,text="Your Book ID's data is not found or available")
                Lu2.place(x=90,y=25)

                B1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
                B1.place(x=180,y=80)
                win2.mainloop()
            else:
                win_in = Toplevel(win)
                win_in.title("Search Book")
                win_in.resizable(False,False)
                win_in.geometry("340x250+550+180")
                win_in.configure(bg="#262626")

                fr = Frame(win_in,bg="#666666",relief=RAISED,bd=2)
                fr.place(x=0,y=0,width=350,height=50)
                lt = Label(fr,text="Available",font=('veranda',15,'bold'),bg='#666666',fg='#F5FFFA')
                lt.place(x=120,y=8)

                lt1 = Label(win_in,text="Book ID:",font=('veranda',15,'bold'),bg='#262626',fg='#F5FFFA')
                lt1.place(x=20,y=60)

                lt2 = Label(win_in,text="Title:",font=('veranda',15,'bold'),bg='#262626',fg='#F5FFFA')
                lt2.place(x=20,y=100)

                lt3 = Label(win_in,text="Author:",font=('veranda',15,'bold'),bg='#262626',fg='#F5FFFA')
                lt3.place(x=20,y=140)

                lt4 = Label(win_in,text=B_ID,font=('veranda',15,'bold'),bg='#262626',fg='#F5FFFA')
                lt4.place(x=150,y=60)

                lt5 = Label(win_in,text=title,font=('veranda',15,'bold'),bg='#262626',fg='#F5FFFA')
                lt5.place(x=150,y=100)

                lt6 = Label(win_in,text=author,font=('veranda',15,'bold'),bg='#262626',fg='#F5FFFA')
                lt6.place(x=150,y=140)

                bu4 = Button(win_in,text="OK",font=('veranda',12,'bold'),activebackground="#262626",bg="#666666",
                             fg="#e60000",relief=RAISED,command=OK)
                bu4.place(x=130,y=210,height=26,width=70)

                win_in.mainloop()

        else:

            conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT count(`Book ID`) ,`Total` FROM `book_details` where `Title` like '%" + B_name + "%' and `Total` !=0")
            cnt = 0
            for (I,T) in cursor:
                cnt = I

            cursor.close()

            if cnt == 0:
                win2 = Toplevel(win)
                win2.title("Search")
                win2.resizable(False,False)
                win2.geometry("390x120+500+320")

                Lu1 = Label(win2,image="::tk::icons::warning")
                Lu1.place(x=40,y=20)
                Lu2 = Label(win2,text="Your Book Name's data is not found or available")
                Lu2.place(x=90,y=25)

                B1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
                B1.place(x=180,y=80)
                win2.mainloop()

            else:
                win_in = Toplevel(win)
                win_in.title("Search Book")
                win_in.resizable(False,False)
                win_in.geometry("440x250+500+180")
                win_in.configure(bg="#F5FFFA")

                f1 = Frame(win_in,bg="#666666")
                f1.place(x=0,y=0,height=40,width=440)

                l1 = Label(f1,text="Available",font=('veranda',20,'bold'),bg='#666666',fg='#F5FFFA')
                l1.place(x=150,y=2)

                f2 = Frame(win_in,bg="#F5FFFA")
                f2.place(x=0,y=40,height=250,width=440)

                scroll_bar = Scrollbar(f2,orient=VERTICAL)

                style = ttk.Style()
                style.theme_use('alt')
                style.configure(".",font=('veranda',10))
                style.configure("Treeview.Heading",font=('veranda',12,'bold'),foreground='white',background="#262626")
                style.configure("Treeview",rowheight=20,foreground="black",background="#D3D3D3",
                                fieldbackground="#D3D3D3")
                style.map('Treeview',background=[('selected','#e60000')])

                book_table = ttk.Treeview(f2,columns=("Book ID","Title","Author"),
                                          yscrollcommand=scroll_bar.set)

                scroll_bar.place(x=420,y=0,height=200)
                scroll_bar.config(command=book_table.yview)

                book_table.heading("Book ID",text="Book ID")
                book_table.heading("Title",text="Title")
                book_table.heading("Author",text="Author")

                book_table.column("Book ID",width=50)
                book_table.column("Title",width=50)
                book_table.column("Author",width=50)

                book_table['show'] = 'headings'
                book_table.place(x=0,y=0,height=200,width=420)

                conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT `Book ID`, `Title`, `Author`  FROM `book_details` where `Title` like '%" + B_name + "%' and `Total` !=0")

                for (B,T,A) in cursor:
                    book_table.insert('',END,values=(B,T,A))

                cursor.close()

                win.mainloop()

    f2 = Frame(bg="#8fbcbc")
    f2.place(x=0,y=0,width=990,height=650)

    f3 = Frame(f2,bg="#396060")
    f3.place(x=0,y=0,width=990,height=90)

    l = Label(f3,text="Pikachu Library",font=('veranda',45,'bold'),bg='#396060',fg='#F5FFFA')
    l.place(x=280,y=5)

    wh = Frame(f2,bg="#F5FFFA")
    wh.place(x=0,y=90,width=990,height=30)

    f4 = Frame(f2,bg="#F5FFFA")
    f4.place(x=200,y=180,width=600,height=400)

    f5 = Frame(f4,bg="#396060")
    f5.place(x=0,y=0,width=600,height=50)

    l1 = Label(f5,text="Search Book",font=('veranda',25,'bold'),bg="#396060",fg='#F5FFFA')
    l1.place(x=200,y=2)

    search_ID = StringVar()
    search_name = StringVar()

    d_ID = Label(f4,text="Book ID",font=('veranda',10,'bold'),bg="#F5FFFA")
    d_ID.place(x=60,y=100)

    dy1 = Entry(f4,textvariable=search_ID,bd=1,font=('Arial',15,'bold'),border=2,bg="white",relief=GROOVE)
    dy1.place(x=180,y=100,height=25,width=300)

    Or = Label(f4,text='Or',font=('veranda',12,'bold'),bg="#F5FFFA",fg="#B22222")
    Or.place(x=310,y=150)

    d_name = Label(f4,text="Book Name",font=('veranda',10,'bold'),bg="#F5FFFA")
    d_name.place(x=60,y=200)

    dy2 = Entry(f4,textvariable=search_name,bd=1,font=('Arial',15,'bold'),border=2,bg="white",relief=GROOVE)
    dy2.place(x=180,y=200,height=25,width=300)
    dy1.focus()
    De = Button(f4,text='Search',height=1,width=25,font=('veranda',12,'bold'),bg="#396060",fg="white",command=SEARCH)
    De.place(x=190,y=280)

    De1 = Button(f2,text='<Back',height=1,width=10,font=('veranda',12,'bold'),bg="#396060",fg="white",
                 command=back_dashboard)
    De1.place(x=10,y=140)




def Issue():
    print(9)

def Return():
    print(9)

def Update():
    def edit():
        def win_destroy():
            win2.destroy()

        Title_d = ""
        Author_d = ""
        Total_d = 0
        Edition_d = 0
        B_ID = dy1.get()

        if B_ID == "":
            win2 = Toplevel(win)
            win2.title("Insert ID")
            win2.resizable(False,False)
            win2.geometry("300x120+500+320")

            lu1 = Label(win2,image="::tk::icons::error")
            lu1.place(x=40,y=20)
            lu2 = Label(win2,text="Book ID is required")
            lu2.place(x=90,y=25)

            bu1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
            bu1.place(x=180,y=80)
            win2.mainloop()
        else:
            flg = 0
            conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT `Book ID` ,`Title` ,`Author`,`Total` , `Edition` FROM `book_details` where `Book ID`=" + B_ID)
            for (I,T,A,total,ED) in cursor:
                if str(I) == (B_ID):
                    flg = 1
                    Title_d = T
                    Author_d = A
                    Total_d = total
                    Edition_d = ED

            cursor.close()
            if flg == 0:
                win2 = Toplevel(win)
                win2.title("Search")
                win2.resizable(False,False)
                win2.geometry("340x120+500+320")

                Lu1 = Label(win2,image="::tk::icons::warning")
                Lu1.place(x=40,y=20)
                Lu2 = Label(win2,text="Your Book ID data is not found")
                Lu2.place(x=90,y=25)

                B1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win_destroy)
                B1.place(x=180,y=80)
                win2.mainloop()
            else:
                def up():
                    def wi_destroy():
                        win2.destroy()

                    def wi2_destroy():
                        win2.destroy()
                        win_in.destroy()


                    TITLE = by2.get()
                    AUTHOR = by3.get()
                    EDITION = by4.get()
                    TOTAL = by5.get()

                    if  TITLE == "" or AUTHOR == "" or EDITION == "" or TOTAL == "":
                        win2 = Toplevel(win)
                        win2.title("Insert Status")
                        win2.resizable(False,False)
                        win2.geometry("300x120+500+320")

                        lu1 = Label(win2,image="::tk::icons::error")
                        lu1.place(x=40,y=20)
                        lu2 = Label(win2,text="All Fields are required")
                        lu2.place(x=90,y=25)

                        bu1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=wi_destroy)
                        bu1.place(x=180,y=80)
                        win2.mainloop()
                    else:

                        conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
                        cursor = conn.cursor()
                        cursor.execute(
                            "UPDATE `book_details` SET `Book ID`= '" + B_ID + "' ,`Title`= ' " + by2.get() + "',`Author`='" + by3.get() + "',`Edition`='" + by4.get() + "',`Total` ='" + by5.get() + "' WHERE `Book ID`='" + B_ID + "'")
                        cursor.execute("commit")
                        cursor.close()

                        win2 = Toplevel(win)
                        win2.title("Add Books")
                        win2.resizable(False,False)
                        win2.geometry("300x120+500+320")

                        lu2 = Label(win2,image="::tk::icons::information")
                        lu2.place(x=40,y=20)
                        lu3 = Label(win2,text="Updated Successfully")
                        lu3.place(x=90,y=25)

                        bu2 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=wi2_destroy)
                        bu2.place(x=180,y=80)
                        by1.focus()
                        win2.mainloop()

                win_in = Toplevel(win)
                win_in.title("Edit Books Details")
                win_in.resizable(False,False)
                win_in.geometry("400x500+500+120")
                win_in.configure(bg="#F5FFFA")

                fr = Frame(win_in,bg="#396060")
                fr.place(x=0,y=0,width=420,height=50)

                lt = Label(fr,text="Edit Book",font=('veranda',20,'bold'),bg="#396060",fg="#F5FFFA")
                lt.place(x=135,y=5)


                title = StringVar()
                author = StringVar()
                edition = StringVar()
                total = StringVar()

                ID = Label(win_in,text="Book ID",font=('veranda',10,'bold'),bg="#F5FFFA")
                ID.place(x=20,y=100)

                by1 = Label(win_in,text=B_ID,font=('Arial',15,'bold'),bg="#F5FFFA",fg="black")
                by1.place(x=120,y=100)

                Title = Label(win_in,text="Title",font=('veranda',10,'bold'),bg="#F5FFFA")
                Title.place(x=20,y=160)

                by2 = Entry(win_in,textvariable=title,bd=1,font=('Arial',15,'bold'),bg="white")
                by2.place(x=120,y=160,height=25,width=235)

                Author = Label(win_in,text="Author",font=('veranda',10,'bold'),bg="#F5FFFA")
                Author.place(x=20,y=220)

                by3 = Entry(win_in,textvariable=author,bd=1,font=('Arial',15,'bold'),bg="white")
                by3.place(x=120,y=220,height=25,width=235)

                Edition = Label(win_in,text="Edition",font=('veranda',10,'bold'),bg="#F5FFFA")
                Edition.place(x=20,y=280)

                by4 = Entry(win_in,textvariable=edition,bd=1,font=('Arial',15,'bold'),bg="white")
                by4.place(x=120,y=280,height=25,width=235)

                Total = Label(win_in,text="Total Books",font=('veranda',10,'bold'),bg="#F5FFFA")
                Total.place(x=20,y=340)

                by5 = Entry(win_in,textvariable=total,bd=1,font=('Arial',15,'bold'),bg="white")
                by5.place(x=120,y=340,height=25,width=235)

                Submit = Button(win_in,text='Update',height=1,width=20,font=('veranda',12,'bold'),bg="#3366ff",
                                fg="white",command=up)
                Submit.place(x=90,y=430)


                by2.insert(0,Title_d)
                by3.insert(0,Author_d)
                by4.insert(0,Edition_d)
                by5.insert(0,Total_d)

                win_in.mainloop()

    f2 = Frame(bg="#8fbcbc")
    f2.place(x=0,y=0,width=990,height=650)

    f3 = Frame(f2,bg="#396060")
    f3.place(x=0,y=0,width=990,height=90)

    l = Label(f3,text="Pikachu Library",font=('veranda',45,'bold'),bg='#396060',fg='#F5FFFA')
    l.place(x=280,y=5)

    wh = Frame(f2,bg="#F5FFFA")
    wh.place(x=0,y=90,width=990,height=30)

    f4 = Frame(f2,bg="#F5FFFA")
    f4.place(x=200,y=200,width=600,height=250)

    f5 = Frame(f4,bg="#396060")
    f5.place(x=0,y=0,width=600,height=50)

    l1 = Label(f5,text="Edit Books Details",font=('veranda',25,'bold'),bg="#396060",fg='#F5FFFA')
    l1.place(x=160,y=2)

    update = StringVar()
    d_ID = Label(f4,text="Book ID",font=('veranda',10,'bold'),bg="#F5FFFA")
    d_ID.place(x=60,y=100)

    dy1 = Entry(f4,textvariable=update,bd=1,font=('Arial',15,'bold'),border=2,bg="white",relief=GROOVE)
    dy1.place(x=180,y=100,height=25,width=300)

    De = Button(f4,text='Edit',height=1,width=25,font=('veranda',12,'bold'),bg="#396060",fg="white",command=edit)
    De.place(x=190,y=160)

    De1 = Button(f2,text='<Back',height=1,width=10,font=('veranda',12,'bold'),bg="#396060",fg="white",
                 command=back_dashboard)
    De1.place(x=10,y=140)

    dy1.focus()


def Log_out():
    win.destroy()


def Back():
    home()

def dashboard():
    # ----Frame2----

    f2 = Frame(bg="#568f8f")
    f2.place(x=0,y=0,width=990,height=650)

    headingf = Frame(f2,bg="#d62929",bd=5)
    headingf.place(x=150,y=5,height=110,width=650)
    headingl = Label(headingf,text="Welcome to Pikachu Library",bg='BLACK',fg='white',font=('Courier',15))
    headingl.place(x=20,y=5,height=90,width=600)

    but1 = Button(f2,text='Add Book Details',height=2,width=30,font=('veranda',15,''),bg="black",fg="#F5FFFA",command=Add_Book)
    but1.place(x=300,y=140)

    but2 = Button(f2,text='Search Book',height=2,width=30,font=('veranda',15,''),bg="black",fg="#F5FFFA",command=Search)
    but2.place(x=300,y=200)

    but3 = Button(f2,text='Delete Book',height=2,width=30,font=('veranda',15,''),bg="black",fg="#F5FFFA",command=Delete)
    but3.place(x=300,y=260)

    but4 = Button(f2,text='View Book List',height=2,width=30,font=('veranda',15,''),bg="black",fg="#F5FFFA",command=Views)
    but4.place(x=300,y=320)

    but5 = Button(f2,text='Update Book',height=2,width=30,font=('veranda',15,''),bg="black",fg="#F5FFFA",command=Update)
    but5.place(x=300,y=380)

    but6 = Button(f2,text='Issue Book to Student',height=2,width=30,font=('veranda',15,''),bg="black",fg="#F5FFFA",command=Issue)
    but6.place(x=300,y=440)

    but7 = Button(f2,text='Return Book',height=2,width=30,font=('veranda',15,''),bg="black",fg="#F5FFFA",command=Return)
    but7.place(x=300,y=500)

    but8 = Button(f2,text='Log Out',height=2,width=30,font=('veranda',15,''),bg="black",fg="#F5FFFA",command=Log_out)
    but8.place(x=300,y=560)

    back = Button(f2,text='Back',height=1,width=10,font=('veranda',10,'bold'),bg="#d62929",fg="BLACK",relief=SOLID,bd=5,command=Back)
    back.place(x=30,y=580)

def home():

    def change_password():

        def submit():
            def win2_destroy():
                win2.destroy()
            def end():
                win1.destroy()

            user_name = by.get()
            pas = by2.get()

            if (user_name == "" or pas == ""):
                win2 = Toplevel(win1)
                win2.title("Insert Status")
                win2.resizable(False,False)
                win2.geometry("300x120+500+320")

                lu1 = Label(win2,image="::tk::icons::error")
                lu1.place(x=40,y=20)
                lu2 = Label(win2,text="All Fields are required")
                lu2.place(x=90,y=25)

                bu1 = Button(win2,text='Ok',height=1,width=10,font=('veranda',10,''),command=win2_destroy)
                bu1.place(x=180,y=80)
                win2.mainloop()
            else:
                f = 0
                conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
                cursorr = conn.cursor()
                cursorr.execute("SELECT `User Name`,`Name`  FROM `admin`")
                for (us_name,name) in cursorr:
                    if us_name == user_name:
                        f=1
                        break
                conn.close()

                if f == 0:
                    np = Label(win1,text='User Name is not found',font=('Arial',10,'bold'),fg='#B22222')
                    np.place(x=200,y=129)

                else:
                    conn = mysql.connect(host="localhost",user="root",password="",database="library-management-db")
                    cursorr = conn.cursor()
                    cursorr.execute("UPDATE admin SET `Password` = '" + pas + "' WHERE `User Name`= '" + user_name +"'")
                    cursorr.execute("commit")
                    cursorr.close()

                    win3 = Toplevel(win1)
                    win3.title("Update Status")
                    win3.resizable(False,False)
                    win3.geometry("300x120+500+320")

                    lu2 = Label(win3,image="::tk::icons::information")
                    lu2.place(x=40,y=20)
                    lu3 = Label(win3,text="Updated Successfully")
                    lu3.place(x=90,y=25)

                    bu2 = Button(win3,text='Ok',height=1,width=10,font=('veranda',10,''),command=end)
                    bu2.place(x=180,y=80)
                    win3.mainloop()



        win1=Toplevel(win)
        win1.title("Change Password")
        win1.geometry("500x300+400+220")
        win1.resizable(False,False)


        si1 = StringVar()
        si2 = StringVar()
        title2 = Label(win1,text='New Password',font=('Arial',25,'bold'),fg='#B22222')
        title2.place(x=130,y=25)

        l2 = Label(win1,text="User ID:",font=('veranda',10,'bold'))
        l2.place(x=60,y=100)
        by = Entry(win1,textvariable=si1,bd=1,font=('Arial',15,'bold'))
        by.place(x=180,y=100,height=25,width=200)

        l3 = Label(win1,text="New Password:",font=('veranda',10,'bold'))
        l3.place(x=60,y=160)
        by2 = Entry(win1,textvariable=si2,bd=1,font=('Arial',15,'bold'))
        by2.place(x=180,y=160,height=25,width=200)

        but = Button(win1,text='Submit',height=1,width=20,font=('veranda',12,'bold'),fg="#F5FFFA",bg="#396060",command=submit)
        but.place(x=150,y=230)





        win1.mainloop()

    #----Clear Enter Username & Password
    def reset():
        b1.delete(0,'end')
        b2.delete(0,'end')
        b1.focus()

    def logIn():

        userid=b1.get()
        password=b2.get()


        if(userid=="" or password==""):
            messagebox.showinfo("Insert Status","All Fields are required")
        else:
            try:
               con=mysql.connect(host="localhost",user="root",password="",database="library-management-db")
            except:
                messagebox.showerror("Error","You are not connected to server(localhost)")

            else:
               flg=0
               cursor=con.cursor()
               cursor.execute("SELECT `User Name`, `Password` FROM `admin` ")

               for (us,pas)in cursor:
                   if userid == us and password == pas:
                       flg=1
                       break
               if flg==1:
                   dashboard()
               else:
                   messagebox.showerror("Library System","Your User Name or Password is wrong")
               con.close()


    # ----Frame1----
    f1 = Frame(bg="#70a9a9")
    f1.place(x=0,y=0,width=990,height=650)

    # ----Title----
    title = Label(f1,text='Library Management System',font=('Arial',45,'bold'),bg='#70a9a9',fg='#B22222')
    title.place(x=100,y=60)

    # ----UserName & Password
    frame1 = Frame(f1,bg="#396060",relief=RIDGE,bd=20,height=180,width=700)
    frame1.place(x=135,y=200)

    s1 = StringVar()
    s2 = StringVar()

    l1 = Label(frame1,text="User Name",font=('veranda',20,'bold'),fg='#F5FFFA',bg='#396060')
    l1.place(x=5,y=10)
    b1 = Entry(frame1,textvariable=s1,bd=5,font=('Arial',15,'bold'),bg="#e6e6e6")
    b1.place(x=200,y=15,height=35,width=420)

    l2 = Label(frame1,text="Password",font=('veranda',20,'bold'),fg='#F5FFFA',bg='#396060')
    l2.place(x=5,y=90)
    b2 = Entry(frame1,textvariable=s2,bd=5,font=('Arial',15,'bold'),bg="#e6e6e6")
    b2.place(x=200,y=90,height=35,width=420)

    # ----3 Buttons----
    frame2 = Frame(f1,bg="#396060",relief=RIDGE,bd=20,height=100,width=700)
    frame2.place(x=135,y=390)

    bu1 = Button(frame2,text='Login',height=1,width=16,font=('veranda',15,'bold'),bg="#C0C0C0",command=logIn)
    bu1.place(x=10,y=7)
    bu2 = Button(frame2,text='Reset',height=1,width=16,font=('veranda',15,'bold'),bg="#C0C0C0",command=reset)
    bu2.place(x=230,y=7)
    bu3 = Button(frame2,text='Exit Window',height=1,width=16,font=('veranda',15,'bold'),bg="#C0C0C0",
                         command=window)
    bu3.place(x=450,y=7)

    bu4 = Button(f1,text="Forgot Password?",font=('veranda',15,'bold'),activebackground="#70a9a9",bg="#70a9a9",
                         fg="#B22222",relief=FLAT,command=change_password)
    bu4.place(x=400,y=500)

    b1.focus()



home()
win.mainloop()
