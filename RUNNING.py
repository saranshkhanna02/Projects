from tkinter import *
import mysql.connector
from tkinter.ttk import Combobox, Progressbar
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string
Frame = Tk()
Frame.title("WANDERING-WHEELS")
Frame.config(background="black")
Frame.geometry("290x165")
bg8 = PhotoImage(file=r"img.png").subsample(1, 1)
Label(Frame, image=bg8).place(x=0, y=0)
bg1 = PhotoImage(file=r'cust&admin.png').subsample(1, 1)
bg2 = PhotoImage(file=r'logout.png').subsample(1, 1)
bg3 = PhotoImage(file=r'btn.png').subsample(1, 1)
bg4 = PhotoImage(file=r'receipt.png').subsample(1, 1)
bg5 = PhotoImage(file=r'img_8.png').subsample(1, 1)
bg6 = PhotoImage(file=r"flip.png").subsample(1, 1)
bg7 = PhotoImage(file=r"black.png").subsample(1, 1)
global cur, con, i, show, images, slide_image, n, company, a, name_card, issued_date, end_date, address, Phone, x, home


def running():
    global cur, con, i, show, images, slide_image, n, company, a, name_card, issued_date, end_date, address, Phone, x, \
        home, bg7, bg1
    Root = Toplevel(Frame)
    Label(Root, image=bg1).place(x=0, y=0)
    Root.title("W A N D E R   W H E E L S")
    Root.configure(background="black")
    Root.attributes('-fullscreen', True)

    def admin_login():
        global bg7
        root1 = Toplevel(Root)
        root1.configure(background="black")
        root1.title("W A N D E R   W H E E L S")
        bg7 = PhotoImage(file=r'login.png')
        bg7.subsample(1, 1)
        label1 = Label(root1, image=bg7)
        label1.place(x=0, y=0)
        root1.attributes('-fullscreen', True)
        username = StringVar()
        username.set("USERNAME")
        password = StringVar()
        password.set("PASSWORD")

        def user():
            running()
            root1.destroy()

        def for_page3():
            global cur, con
            if admin_Username.get() == "" or admin_Password.get() == "":
                messagebox.showerror("Error", "Enter User Name And Password", parent=root1)
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
                    cur = con.cursor()

                    cur.execute("select * from admin where username=%s and password = %s",
                                (admin_Username.get(), admin_Password.get()))
                    row = cur.fetchone()

                    if row is None:
                        messagebox.showerror("Error", "Invalid User Name And Password", parent=root1)

                    else:
                        messagebox.showinfo("Success", "Successfully Login", parent=root1)
                        root1.destroy()
                        admin_panel1()
                    con.close()

                except Exception as es:
                    messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=root1)
                finally:
                    if con.is_connected():
                        cur.close()
                        con.close()

        "------------------------ LABEL ------------------------"
        label3 = Label(root1, image=bg5, relief="groove", borderwidth=30, bg="orange")
        label3.grid(row=1, column=2, padx=300)
        "------------------------ TEXT BOX ------------------------"

        admin_Username = Entry(root1, font='Georgia 15 bold', bg='black', fg='grey', textvariable=username, width=15)
        admin_Username.grid(row=3, column=2, pady=20, padx=10)

        admin_Password = Entry(root1, show='*', font='Georgia 15 bold', bg='black', fg='grey', textvariable=password,
                               width=15)
        admin_Password.grid(row=5, column=2, pady=20, padx=10)

        "------------------------ BUTTON ------------------------"
        btn1 = Button(root1, text='LOGIN', font='Georgia 15 bold', fg='#116562', bg='black', command=for_page3)
        btn1.grid(row=6, column=2, padx=2, pady=15)
        btn2 = Button(root1, font='Georgia 15 italic', fg='#4a7abc', bg='black', command=user, image=bg6)
        btn2.grid(row=0, column=0, padx=5, pady=5)

    def admin_panel1():
        global bg7
        root2 = Toplevel(Root)
        root2.configure(background='black')
        root2.title('A D M I N   P A N E L  1')
        bg7 = PhotoImage(file=r'admin_panel.png')
        bg7.subsample(1, 1)
        label_a = Label(root2, image=bg7)
        label_a.place(x=0, y=0)
        root2.attributes('-fullscreen', True)

        def back_panel1():
            admin_login()
            root2.destroy()

        def emp_details():
            admin_panel4()
            root2.destroy()

        def c_details():
            admin_panel2()
            root2.destroy()

        def cust_details():
            root20 = Toplevel(Root)
            root20.attributes('-fullscreen', True)
            root20.configure(background='black')
            global con, cur, i, bg7
            bg7 = PhotoImage(file=r'cust_view.png')
            bg7.subsample(1, 1)
            label2 = Label(root20, image=bg7)
            label2.place(x=0, y=0)
            root2.destroy()

            Label(root20, text="NAME", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=0, pady=10)
            Label(root20, text="AGE", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=1, pady=10)
            Label(root20, text="GENDER", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=2, pady=10)
            Label(root20, text="LICENSE", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=3)
            Label(root20, text="ISSUED", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=4, pady=10)
            Label(root20, text="END", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=5, pady=10)
            Label(root20, text="ADDRESS", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=6)
            Label(root20, text="MOBILE", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=7, pady=10)
            Label(root20, text="DESTINATION", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=8)

            con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
            cur = con.cursor()

            cur.execute("SELECT name, age, gender, license, issued, end, address, mob, destination FROM user_detail")

            def back_details():
                admin_panel1()
                root20.destroy()

            i = 2
            for user_detail in cur:
                for j in range(len(user_detail)):
                    e = Entry(root20, width=12, fg='orange', bg='black', font='Georgia 12 italic')
                    e.grid(row=i, column=j, padx=10, pady=10)
                    e.insert(END,  user_detail[j])
                i = i + 1
            button = Button(root20, text='BACK', fg='green', bg='black', font='georgia 12 italic', command=back_details,
                            image=bg3)
            button.grid(row=0, column=0, padx=10, pady=10)

        def p_details():
            root24 = Toplevel(Root)
            root24.attributes('-fullscreen', True)
            root24.configure(background='black')
            global con, cur, i, bg7
            bg7 = PhotoImage(file=r'payment_view.png')
            bg7.subsample(1, 1)
            label2 = Label(root24, image=bg7)
            label2.place(x=0, y=0)
            root2.destroy()

            Label(root24, text="I D", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=0, pady=10)
            Label(root24, text="N A M E", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=1)
            Label(root24, text="M O B I L E", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=2)
            Label(root24, text="C O M P A N Y", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=3)
            Label(root24, text="A M O U N T", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=4)
            Label(root24, text="T Y P E", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=5)

            con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
            cur = con.cursor()

            cur.execute("SELECT r_no, name, mobile, company, amount, type FROM receipt")

            def back_details():
                admin_panel1()
                root24.destroy()

            i = 2
            for Receipt in cur:
                for j in range(len(Receipt)):
                    e = Entry(root24, width=18, fg='green', bg='black', font='Georgia 14 italic')
                    e.grid(row=i, column=j, padx=10, pady=10)
                    e.insert(END, Receipt[j])
                i = i + 1
            button = Button(root24, text='BACK', fg='green', bg='black', font='georgia 12 italic', command=back_details,
                            image=bg3)
            button.grid(row=0, column=0, padx=5, pady=10)

        "------------------------ BUTTON ------------------------"
        button1 = Button(root2, text="E M P L O Y E E   D E T A I L", font='Georgia 15 italic', fg='red', bg='black',
                         borderwidth=3, relief="flat", command=c_details)
        button1.grid(row=4, column=0, pady=600, padx=30)
        button2 = Button(root2, text="C U S T O M E R   D E T A I L", font='Georgia 15 italic', fg='green', bg='black',
                         borderwidth=3, relief="flat", command=cust_details)
        button2.grid(row=4, column=1, pady=10, padx=70)
        button3 = Button(root2, text="C A R   D E T A I L S", command=emp_details,
                         font='Georgia 15 italic', fg='blue', bg='black', borderwidth=3, relief="flat")
        button3.grid(row=4, column=2, pady=10, padx=50)

        button4 = Button(root2, text='LOGOUT', font='Georgia 15 italic', image=bg2, fg='white', bg='black',
                         command=back_panel1, borderwidth=3, relief="flat")
        button4.grid(row=0, column=4, padx=20, pady=10)

        button4 = Button(root2, text='P A Y M E N T', font='Georgia 15 italic', fg='yellow', bg='black',
                         command=p_details, borderwidth=3, relief="flat")
        button4.grid(row=4, column=3, padx=20, pady=30)

    def admin_panel4():
        global bg7, bg2
        root3 = Toplevel(Root)
        root3.configure(background="black")
        root3.title("A D M I N    P A N E L  2")
        bg7 = PhotoImage(file=r'car_panel.png')
        bg7.subsample(1, 1)
        bg2 = PhotoImage(file=r'logout.png')
        bg2.subsample(1, 1)
        label1 = Label(root3, image=bg7)
        label1.place(x=0, y=0)
        root3.attributes('-fullscreen', True)

        def add_car():
            root3.destroy()
            global bg7
            root11 = Toplevel(Root)
            root11.configure(background='black')
            root11.title('A D D   C A R')
            root11.attributes('-fullscreen', True)
            bg7 = PhotoImage(file=r'add_Car.png')
            bg7.subsample(1, 1)
            label2 = Label(root11, image=bg7)
            label2.place(x=0, y=0)

            label3 = Label(root11, text='BRAND', font='Georgia 15 bold', bg='black', fg='white', relief="groove")
            label3.grid(row=1, column=1, pady=20, padx=10)

            brand = Entry(root11, font='Georgia 20 bold', bg='black', fg='white')
            brand.grid(row=1, column=2)

            label4 = Label(root11, text='SEAT', font='Georgia 15 bold', bg='black', fg='white', relief="groove")
            label4.grid(row=2, column=1, pady=20, padx=10)

            seat = Entry(root11, font='Georgia 20 bold', bg='black', fg='white')
            seat.grid(row=2, column=2)

            label5 = Label(root11, text='PRICE', font='Georgia 15 bold', bg='black', fg='white', relief="groove")
            label5.grid(row=3, column=1, pady=20, padx=10)

            price = Entry(root11, font='Georgia 20 bold', bg='black', fg='white')
            price.grid(row=3, column=2)

            label6 = Label(root11, text='MODEL', font='Georgia 15 bold', bg='black', fg='white', relief="groove")
            label6.grid(row=4, column=1, pady=20, padx=10)

            model = Entry(root11, font='Georgia 20 bold', bg='black', fg='white')
            model.grid(row=4, column=2)

            label7 = Label(root11, text='FUEL', font='Georgia 15 bold', bg='black', fg='white', relief="groove")
            label7.grid(row=5, column=1, pady=20, padx=10)

            fuel = Entry(root11, font='Georgia 20 bold', bg='black', fg='white')
            fuel.grid(row=5, column=2)

            def back_addcar():
                admin_panel4()
                root11.destroy()

            def add():
                global cur, con
                if brand.get() == "" or seat.get() == "" or price.get() == "" or model.get() == "" or fuel.get() == "":
                    messagebox.showerror("Error", "Enter Details", parent=Root)
                    add_car()
                else:
                    try:
                        con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
                        cur = con.cursor()
                        query = "insert into car_detail(brand, seat, price, model, fuel) values(%s, %s, %s, %s, %s)"
                        Brand = brand.get()
                        Seat = seat.get()
                        Price = price.get()
                        Model = model.get()
                        Fuel = fuel.get()
                        record = (Brand, Seat, Price, Model, Fuel)
                        cur.execute(query, record)
                        con.commit()
                        messagebox.showinfo("Success", "Successfully inserted", parent=Root)
                    except mysql.connector.Error:
                        messagebox.showerror("Error", "Failed to insert record", parent=Root)
                    finally:
                        if con.is_connected():
                            cur.close()
                            con.close()

            button6 = Button(root11, text='ADD', command=add, font='Georgia 15 italic', fg='white', bg='black',
                             borderwidth=3, relief="flat")
            button6.grid(row=6, column=2)
            button = Button(root11, text='BACK', fg='green', bg='black', font='georgia 12 italic', command=back_addcar,
                            image=bg3)
            button.grid(row=0, column=0, padx=15, pady=10)

        def del_car():
            global bg7
            root3.destroy()
            root12 = Toplevel(Root)
            root12.configure(background='black')
            root12.title('D E L   C A R')
            root12.attributes('-fullscreen', True)
            bg7 = PhotoImage(file=r'del_Car.png')
            bg7.subsample(1, 1)
            label2 = Label(root12, image=bg7)
            label2.place(x=0, y=0)

            label3 = Label(root12, text='C A R   N A M E ', font='Georgia 15 bold', bg='black', fg='white')
            label3.grid(row=1, column=2, pady=200, padx=150)
            Id = Entry(root12, font='Georgia 20 bold', bg='black', fg='white')
            Id.grid(row=1, column=3, pady=10, padx=10)

            def back():
                admin_panel4()
                root12.destroy()

            def delete():
                global con, cur
                car_name = Id.get()
                root12.destroy()
                if car_name == "":
                    messagebox.showerror("Error", "Enter Car id", parent=Root)
                    del_car()
                else:
                    try:
                        con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
                        cur = con.cursor()
                        sql_Delete_query = "Delete from car_detail where brand = %s"
                        cur.execute(sql_Delete_query, (car_name,))
                        con.commit()
                        messagebox.showinfo("Success", "Successfully deleted")
                        del_car()
                        cur.close()
                        con.close()
                    except Exception as es:
                        messagebox.showerror("Error", f"Error Dui to : {str(es)}")
                        del_car()
                    finally:
                        if con.is_connected():
                            cur.close()
                            con.close()

            button5 = Button(root12, command=delete, font='Georgia 15 italic', fg='white', bg='black',
                             borderwidth=3, relief="flat", text='DELETE')
            button5.grid(row=2, column=3)

            button = Button(root12, text='BACK', fg='green', bg='black', font='georgia 12 italic', command=back,
                            image=bg3)
            button.grid(row=0, column=0, pady=5, padx=10)

        def view_car():
            global con, cur, i, bg7
            root21 = Toplevel(Root)
            root21.attributes('-fullscreen', True)
            root21.configure(background='black')
            bg7 = PhotoImage(file=r'car_view.png')
            bg7.subsample(1, 1)
            label2 = Label(root21, image=bg7)
            label2.place(x=0, y=0)
            root3.destroy()

            Label(root21, text="BRAND", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=0, pady=10)
            Label(root21, text="SEAT", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=1, pady=10)
            Label(root21, text="PRICE", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=2, pady=10)
            Label(root21, text="MODEL", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=3, pady=10)
            Label(root21, text="FUEL", fg='cyan', bg='black', font='Georgia 12 italic').grid(row=1, column=4, pady=10)
            con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
            cur = con.cursor()
            cur.execute("SELECT brand, seat, price, model, fuel FROM car_detail")
            i = 2
            for car in cur:
                for j in range(len(car)):
                    e = Entry(root21, width=15, fg='blue', bg='black', font='Georgia 12 italic')
                    e.grid(row=i, column=j, padx=10, pady=10)
                    e.insert(END, car[j])
                i = i + 1

            def back():
                admin_panel4()
                root21.destroy()

            button = Button(root21, text='BACK', fg='green', bg='black', font='georgia 12 italic', command=back,
                            image=bg3)
            button.grid(row=0, column=0, padx=10, pady=10)

        def back_panel4():
            admin_panel1()
            root3.destroy()

        "------------------------ BUTTON ------------------------"
        button1 = Button(root3, text="ADD CAR", font='Georgia 15 italic', fg='white', bg='black',
                         borderwidth=3, relief="flat", command=add_car)
        button1.grid(row=4, column=0, padx=20, pady=600)
        button2 = Button(root3, text='DELETE CAR', font='Georgia 15 italic', fg='white', bg='black',
                         borderwidth=3, relief="flat", command=del_car)
        button2.grid(row=4, column=1, padx=350, pady=10)
        button3 = Button(root3, text='VIEW CAR LIST', font='Georgia 15 italic', fg='white', bg='black',
                         borderwidth=3, relief="flat", command=view_car)
        button3.grid(row=4, column=2, padx=20, pady=10)
        button4 = Button(root3, text='LOGOUT', font='Georgia 15 italic',
                         image=bg3, fg='white', bg='black', command=back_panel4, borderwidth=3, relief="flat")
        button4.grid(row=1, column=3, padx=30, pady=10)

    def admin_panel2():
        global bg7
        root7 = Toplevel(Root)
        root7.title("E M P L O Y E E   D E T A I L S")
        root7.configure(background='black')
        root7.attributes('-fullscreen', True)
        bg7 = PhotoImage(file=r'emp_panel.png')
        bg7.subsample(1, 1)
        label1 = Label(root7, image=bg7)
        label1.place(x=0, y=0)

        def back():
            admin_panel1()
            root7.destroy()

        def hire():
            global bg7
            root8 = Toplevel(Root)
            root8.configure(background='black')
            root8.title('H I R E')
            root8.attributes('-fullscreen', True)
            bg7 = PhotoImage(file=r'hire.png')
            bg7.subsample(1, 1)
            label2 = Label(root8, image=bg7)
            label2.place(x=0, y=0)
            root7.destroy()

            label3 = Label(root8, text='N A M E', font='Georgia 15 bold', bg='black', fg='white', relief="groove")
            label3.grid(row=1, column=1, pady=20, padx=5)

            name = Entry(root8, font='Georgia 16 bold', bg='black', fg='white')
            name.grid(row=1, column=2)

            label4 = Label(root8, text='A G E', font='Georgia 15 bold', bg='black', fg='white', relief="groove")
            label4.grid(row=2, column=1, pady=20, padx=5)

            age = Entry(root8, font='Georgia 16 bold', bg='black', fg='white')
            age.grid(row=2, column=2)

            label5 = Label(root8, text='G E N D E R', font='Georgia 15 bold', bg='black', fg='white', relief="groove")
            label5.grid(row=3, column=1, pady=20, padx=5)

            gender = Entry(root8, font='Georgia 16 bold', bg='black', fg='white')
            gender.grid(row=3, column=2)

            label6 = Label(root8, text='A D D R E S S', font='Georgia 15 bold', bg='black', fg='white', relief="groove")
            label6.grid(row=4, column=1, pady=20, padx=5)

            Addre = Entry(root8, font='Georgia 16 bold', bg='black', fg='white')
            Addre.grid(row=4, column=2)

            label7 = Label(root8, text='Q U A L I F I C A T I O N', font='Georgia 15 bold', bg='black', fg='white',
                           relief="groove")
            label7.grid(row=5, column=1, pady=20, padx=5)

            qualification = Entry(root8, font='Georgia 16 bold', bg='black', fg='white')
            qualification.grid(row=5, column=2)

            label8 = Label(root8, text='E X P E R I E N C E ', font='Georgia 15 bold', bg='black', fg='white',
                           relief="groove")
            label8.grid(row=6, column=1, pady=20, padx=5)

            experience = Entry(root8, font='Georgia 16 bold', bg='black', fg='white')
            experience.grid(row=6, column=2)

            label9 = Label(root8, text='M O B I L E', font='Georgia 15 bold', bg='black', fg='white', relief="groove")
            label9.grid(row=7, column=1, pady=20, padx=5)

            mobile = Entry(root8, font='Georgia 16 bold', bg='black', fg='white')
            mobile.grid(row=7, column=2)

            def back_hire():
                admin_panel2()
                root8.destroy()

            def hire_db():
                global cur, con
                if name.get() == "" or age.get() == "" or gender.get() == "" or Addre.get() == "" \
                        or qualification.get() == "" or experience.get() == "":
                    messagebox.showerror("Error", "Enter Details", parent=Root)
                    customer_detail()
                else:
                    try:
                        con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
                        cur = con.cursor()
                        query = "insert into employee_detail(name, age, gender, address, qual, exp, mob) " \
                                "values(%s, %s, %s, %s, %s, %s, %s)"
                        Name = name.get()
                        Age = age.get()
                        Gender = gender.get()
                        Address = Addre.get()
                        Qualification = qualification.get()
                        Experience = experience.get()
                        Mobile = mobile.get()
                        record = (Name, Age, Gender, Address, Qualification, Experience, Mobile)
                        cur.execute(query, record)
                        con.commit()
                        messagebox.showinfo("Success", "Successfully Hired", parent=Root)
                    except mysql.connector.Error:
                        messagebox.showerror("Error", "Failed to hire", parent=Root)
                    finally:
                        if con.is_connected():
                            cur.close()
                            con.close()

            button5 = Button(root8, text='S U B M I T', command=hire_db, font='Georgia 15 italic', fg='white',
                             bg='black', borderwidth=3, relief="flat")
            button5.grid(row=8, column=2, pady=20)

            button = Button(root8, text='BACK', fg='green', bg='black', font='georgia 12 italic', command=back_hire,
                            image=bg3)
            button.grid(row=0, column=0, padx=5, pady=20)

        def fire():
            global bg7, con, cur
            root7.destroy()
            root9 = Toplevel(Root)
            root9.attributes('-fullscreen', True)
            root9.configure(background='black')
            root9.title('F I R E')
            bg7 = PhotoImage(file=r'fire.png')
            bg7.subsample(1, 1)
            label2 = Label(root9, image=bg7)
            label2.place(x=0, y=0)

            label3 = Label(root9, text='E M P L O Y E E   N A M E', font='Georgia 15 bold', bg='black', fg='white')
            label3.grid(row=1, column=1, pady=20, padx=5)
            Id = Entry(root9, font='Georgia 20 bold', bg='black', fg='white')
            Id.grid(row=1, column=2, pady=20, padx=5)

            def back_fire():
                admin_panel2()
                root9.destroy()

            def fire_db():
                global con, cur
                if Id.get() == "":
                    messagebox.showerror("Error", "Enter Employee Name", parent=Root)
                else:
                    try:
                        con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
                        cur = con.cursor()
                        sql_Delete_query = "Delete from employee_detail where name = %s"
                        cur.execute(sql_Delete_query, (Id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Successfully fired", parent=Root)
                        fire()
                        cur.close()
                        con.close()
                    except mysql.connector.Error:
                        messagebox.showerror("Error", "Failed to fired", parent=Root)
                        fire()
                    finally:
                        if con.is_connected():
                            cur.close()
                            con.close()

            button5 = Button(root9, command=fire_db, font='Georgia 15 italic', fg='white', bg='black',
                             borderwidth=3, relief="flat", text='S U B M I T')
            button5.grid(row=2, column=1)

            button = Button(root9, text='BACK', fg='green', bg='black', font='georgia 12 italic', command=back_fire,
                            image=bg3)
            button.grid(row=0, column=0, padx=5)

        def view_detail():
            root10 = Toplevel(Root)
            root7.destroy()
            root10.attributes('-fullscreen', True)
            root10.configure(background='black')
            root10.title('V I E W   D E T A I L S')
            global con, cur, i, bg7
            bg7 = PhotoImage(file=r'Emp_view.png')
            bg7.subsample(1, 1)
            label2 = Label(root10, image=bg7)
            label2.place(x=0, y=0)

            Label(root10, text="NAME", fg='yellow', bg='black', font='Georgia 12 italic').grid(row=1, column=0)
            Label(root10, text="AGE", fg='yellow', bg='black', font='Georgia 12 italic').grid(row=1, column=1)
            Label(root10, text="GENDER", fg='yellow', bg='black', font='Georgia 12 italic').grid(row=1, column=2)
            Label(root10, text="ADDRESS", fg='yellow', bg='black', font='Georgia 12 italic').grid(row=1, column=3)
            Label(root10, text="QUALIFICATION", fg='yellow', bg='black', font='Georgia 12 italic').grid(row=1, column=4)
            Label(root10, text="EXPERIENCE", fg='yellow', bg='black', font='Georgia 12 italic').grid(row=1, column=5)
            Label(root10, text="MOBILE", fg='yellow', bg='black', font='Georgia 12 italic').grid(row=1, column=6)
            con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
            cur = con.cursor()

            def back_detail():
                admin_panel2()
                root10.destroy()

            cur.execute("SELECT name , age, gender, address, qual, exp, mob FROM employee_detail")
            i = 2
            for employee_detail in cur:
                for j in range(len(employee_detail)):
                    e = Entry(root10, width=15, fg='blue', bg='black', font='Georgia 12 italic')
                    e.grid(row=i, column=j, padx=10, pady=10)
                    e.insert(END, employee_detail[j])
                i = i + 1
            button = Button(root10, text='BACK', fg='green', bg='black', font='georgia 12 italic', command=back_detail,
                            image=bg3)
            button.grid(row=0, column=0, padx=5, pady=5)

        "------------------------ BUTTONS ------------------------"
        button1 = Button(root7, text='H I R E', font='Georgia 15 italic', fg='white', bg='black',
                         borderwidth=3, relief="flat", command=hire)
        button1.grid(row=4, column=0, padx=80, pady=500)
        button2 = Button(root7, text='F I R E', font='Georgia 15 italic', fg='white', bg='black',
                         borderwidth=3, relief="flat", command=fire)
        button2.grid(row=4, column=1, padx=80)
        button3 = Button(root7, text='V I E W   D E T A I L S', font='Georgia 15 italic', fg='white', bg='black',
                         borderwidth=3, relief="flat", command=view_detail)
        button3.grid(row=4, column=2, padx=100)

        button4 = Button(root7, text='LOGOUT', font='Georgia 15 italic', image=bg3, fg='white', bg='black',
                         command=back, borderwidth=3, relief="flat")
        button4.grid(row=1, column=3, padx=400, pady=10)

    def customer_panel1():
        global bg7
        root13 = Toplevel(Root)
        root13.title("W A N D E R   W H E E L S")
        root13.configure(background="black")
        root13.attributes('-fullscreen', True)
        bg7 = PhotoImage(file=r'rent&return.png')
        bg7.subsample(1, 1)
        label1 = Label(root13, image=bg7)
        label1.place(x=0, y=0)

        def user():
            Root.iconify()
            root13.destroy()

        def rent():
            root13.destroy()
            global bg7, i, show
            root14 = Toplevel(Root)
            root14.title("W A N D E R   W H E E L S")
            root14.attributes('-fullscreen', True)
            root14.configure(background="black")
            bg7 = PhotoImage(file=r'bg.png')
            bg7.subsample(1, 1)
            label2 = Label(root14, image=bg7)
            label2.place(x=0, y=0)
            global images, slide_image

            def backpage1():
                root14.destroy()
                customer_panel1()

            def nextpage1():
                root14.destroy()
                tesla()

            def tesla():
                root15 = Toplevel(Root)
                root15.attributes('-fullscreen', True)
                root15.configure(background="black")
                global images, slide_image, i, show, bg7
                bg7 = PhotoImage(file=r'bg.png')
                bg7.subsample(1, 1)
                label3 = Label(root15, image=bg7)
                label3.place(x=0, y=0)
                root14.destroy()
                listbox2 = Listbox(root15, width=30, bd=20, bg='orange', selectbackground="green", height=7)
                listbox2.insert(1, "Engine and Transmission Fast Charging")
                listbox2.insert(2, "Turbo Charger	no")
                listbox2.insert(3, "Super Charge")
                listbox2.insert(4, "TransmissionType	Automatic")
                listbox2.insert(5, "Fuel & Performance")
                listbox2.insert(6, "Fuel Type	Electric")
                listbox2.insert(7, "Dimensions & Capacity")
                listbox2.insert(8, "Length (mm)	4978")
                listbox2.insert(9, "Width (mm)	2189")
                listbox2.insert(10, "Wheel Base (mm)	2959")
                listbox2.insert(11, "Front Tread (mm)	1661")
                listbox2.insert(12, "Rear Tread (mm)	1699")
                listbox2.grid(row=0, column=0)

                def backpage():
                    root15.destroy()
                    rent()

                def nextpage():
                    root15.destroy()
                    rolls_royce()

                def start1():
                    global i, show
                    if i >= (len(images) - 1):
                        i = 0
                        slide_image.config(image=images[i])
                    else:
                        i = i + 1
                        slide_image.configure(image=images[i])
                    show = slide_image.after(2500, start1)

                img5 = Image.open('T1.png')
                img5.thumbnail((840, 560))
                img6 = Image.open('T2.png')
                img6.thumbnail((840, 560))
                img7 = Image.open('T3.png')
                img7.thumbnail((840, 560))
                img8 = Image.open('T4.png')
                img8.thumbnail((840, 560))
                image5 = ImageTk.PhotoImage(img5)
                image6 = ImageTk.PhotoImage(img6)
                image7 = ImageTk.PhotoImage(img7)
                image8 = ImageTk.PhotoImage(img8)
                images = [image5, image6, image7, image8]
                i = 0
                slide_image = Label(root15, image=images[i])
                slide_image.grid(row=1, column=1, pady=20, padx=80)
                start1()

                button5 = Button(root15, text='B A C K', font='Georgia 15 italic', fg='white', bg='black',
                                 borderwidth=3, relief="flat", command=backpage)
                button5.grid(row=1, column=0, pady=30, padx=50)
                button6 = Button(root15, text='N E X T', font='Georgia 15 italic', fg='white', bg='black',
                                 borderwidth=3, relief="flat", command=nextpage)
                button6.grid(row=1, column=2, pady=50)

            def rolls_royce():
                global images, slide_image, i, show, bg7
                root16 = Toplevel(Root)
                root16.attributes('-fullscreen', True)
                root16.configure(background='black')
                bg7 = PhotoImage(file=r'bg.png')
                bg7.subsample(1, 1)
                label3 = Label(root16, image=bg7)
                label3.place(x=0, y=0)

                listbox3 = Listbox(root16, width=35, bd=20, bg='orange', selectbackground="green", height=7)
                listbox3.insert(1, "Engine Type	V12 Petrol Engine")
                listbox3.insert(2, "Displacement (cc)	6749")
                listbox3.insert(3, "Max Power  563bhp@5000rpm")
                listbox3.insert(4, "Max Torque	900Nm@1700rpm")
                listbox3.insert(5, "No. of cylinder	12")
                listbox3.insert(6, "Valves Per Cylinder	4")
                listbox3.insert(7, "Valve Configuration	DOHC")
                listbox3.insert(8, "Fuel Supply System	Direct Injection")
                listbox3.insert(9, "Bore X Stroke	92.0 X 84.6 mm")
                listbox3.insert(10, "Turbo Charger")
                listbox3.insert(11, "Super Charge")
                listbox3.insert(12, "TransmissionType	Automatic")
                listbox3.insert(13, "Gear Box	8 Speed")
                listbox3.insert(14, "Drive Type	RWD")

                listbox3.insert(15, "Fuel & Performance")
                listbox3.insert(16, "Fuel Type	Petrol")
                listbox3.insert(17, "Mileage (ARAI)	9.8")
                listbox3.insert(18, "Fuel Tank Capacity (Litres)	100")
                listbox3.insert(19, "Emission Norm Compliance	BS VI")
                listbox3.insert(20, "Top Speed (Kmph)	250")

                listbox3.insert(21, "Suspension, Steering & Brakes")
                listbox3.insert(22, "Front Suspension	Double Wishbone")
                listbox3.insert(23, "Rear Suspension	Multi Link")
                listbox3.insert(23, "Rear Suspension	Multi Link")
                listbox3.insert(24, "Steering Type	Power")
                listbox3.insert(25, "Steering Column	Tilt")
                listbox3.insert(26, "Steering Gear Type	Rack & Pinion")
                listbox3.insert(27, "Turning Radius (Metres)	6.8 metres")
                listbox3.insert(28, "Front Brake Type	Ventilated Disc")
                listbox3.insert(29, "Rear Brake Type	Ventilated Disc")
                listbox3.insert(30, "Acceleration	5.4 sec")
                listbox3.insert(31, "0-100kmph	5.4 sec")

                listbox3.insert(32, "Dimensions & Capacity")
                listbox3.insert(33, "Length (mm)	5982")
                listbox3.insert(34, "Width (mm)	2018")
                listbox3.insert(35, "Height (mm)	1656")
                listbox3.insert(36, "Boot Space (Litres)	460")
                listbox3.insert(37, "Seating Capacity	5")
                listbox3.insert(38, "Ground Clearance Unladen (mm)	164")
                listbox3.insert(39, "Wheel Base (mm)	3772")
                listbox3.insert(40, "Front Tread (mm)	1686")
                listbox3.insert(41, "Rear Tread (mm)	1676")
                listbox3.insert(42, "Kerb Weight (Kg)	2745")
                listbox3.insert(43, "Gross Weight (Kg)	3170")
                listbox3.insert(44, "Rear Headroom (mm)	979")
                listbox3.insert(45, R"ear Legroom (mm)	1349")
                listbox3.insert(46, "Front Headroom (mm)	1047")
                listbox3.insert(47, "Front Legroom	1042")
                listbox3.insert(48, "No of Doors	4")
                listbox3.grid(row=0, column=0)

                def backpage():
                    root16.destroy()
                    tesla()

                def nextpage():
                    root16.destroy()
                    maserati()

                def start1():
                    global i, show
                    if i >= (len(images) - 1):
                        i = 0
                        slide_image.config(image=images[i])
                    else:
                        i = i + 1
                        slide_image.configure(image=images[i])
                    show = slide_image.after(2500, start1)

                img5 = Image.open('R1.png')
                img5.thumbnail((840, 560))
                img6 = Image.open('R2.png')
                img6.thumbnail((840, 560))
                img7 = Image.open('R3.png')
                img7.thumbnail((840, 560))
                img8 = Image.open('R4.png')
                img8.thumbnail((840, 560))
                image5 = ImageTk.PhotoImage(img5)
                image6 = ImageTk.PhotoImage(img6)
                image7 = ImageTk.PhotoImage(img7)
                image8 = ImageTk.PhotoImage(img8)
                images = [image5, image6, image7, image8]
                i = 0
                slide_image = Label(root16, image=images[i])
                slide_image.grid(row=1, column=1, pady=5, padx=80)
                start1()

                button5 = Button(root16, text='B A C K', font='Georgia 15 italic', fg='white', bg='black',
                                 borderwidth=3, relief="flat", command=backpage)
                button5.grid(row=1, column=0, pady=5, padx=50)
                button6 = Button(root16, text='N E X T', font='Georgia 15 italic', fg='white', bg='black',
                                 borderwidth=3, relief="flat", command=nextpage)
                button6.grid(row=1, column=2, pady=5)

            def maserati():
                global images, slide_image, i, show, bg7
                root17 = Toplevel(Root)
                root17.attributes('-fullscreen', True)
                root17.configure(background='black')
                bg7 = PhotoImage(file=r'bg.png')
                bg7.subsample(1, 1)
                label3 = Label(root17, image=bg7)
                label3.place(x=0, y=0)

                def backpage():
                    root17.destroy()
                    rolls_royce()

                def nextpage():
                    root17.destroy()
                    customer_detail()

                def start1():
                    global i, show
                    if i >= (len(images) - 1):
                        i = 0
                        slide_image.config(image=images[i])
                    else:
                        i = i + 1
                        slide_image.configure(image=images[i])
                    show = slide_image.after(2500, start1)

                img5 = Image.open('M1.png')
                img5.thumbnail((840, 560))
                img6 = Image.open('M2.png')
                img6.thumbnail((840, 560))
                img7 = Image.open('M3.png')
                img7.thumbnail((840, 560))
                img8 = Image.open('M4.png')
                img8.thumbnail((840, 560))
                image5 = ImageTk.PhotoImage(img5)
                image6 = ImageTk.PhotoImage(img6)
                image7 = ImageTk.PhotoImage(img7)
                image8 = ImageTk.PhotoImage(img8)
                images = [image5, image6, image7, image8]
                i = 0
                slide_image = Label(root17, image=images[i])
                slide_image.grid(row=1, column=1, pady=20, padx=80)
                start1()

                listbox4 = Listbox(root17, width=35, bd=20, bg='orange', selectbackground="green", height=7)
                listbox4.insert(1, "Engine Type	V-Type Petrol Engine")
                listbox4.insert(2, "Displacement (cc)	4691")
                listbox4.insert(3, "Max Power	460bhp@7000rpm")
                listbox4.insert(4, "Max Torque	520Nm@4750rpm")
                listbox4.insert(5, "No. of cylinder	8")
                listbox4.insert(6, "Valves Per Cylinder	4")
                listbox4.insert(7, "Valve Configuration	DOHC")
                listbox4.insert(8, "Fuel Supply System	Direct Injection")
                listbox4.insert(9, "Bore X Stroke	94 X 84.5 mm")
                listbox4.insert(10, "Compression Ratio	11.0:1")
                listbox4.insert(11, "Turbo Charger	")
                listbox4.insert(12, "Super Charge	")
                listbox4.insert(13, "TransmissionType	Automatic")
                listbox4.insert(14, "Gear Box	6 Speed")
                listbox4.insert(15, "Drive Type	RWD")
                listbox4.insert(16, "Report Incorrect Specs")

                listbox4.insert(17, "Fuel & Performance")
                listbox4.insert(18, "Fuel Type	Petrol")
                listbox4.insert(19, "Mileage (ARAI)	10.0")
                listbox4.insert(20, "Fuel Tank Capacity (Litres)	86")
                listbox4.insert(21, "Emission Norm Compliance	BS VI")
                listbox4.insert(22, "Top Speed (Kmph)	285")

                listbox4.insert(23, "Suspension, Steering & Brakes")
                listbox4.insert(24, "Front Suspension	Double Wishbone")
                listbox4.insert(25, "Rear Suspension	Five-Arm Multilink")
                listbox4.insert(26, "Steering Type	Power")
                listbox4.insert(27, "Steering Column	Height & Reach Adjustment")
                listbox4.insert(28, "Steering Gear Type	Rack & Pinion")
                listbox4.insert(29, "Turning Radius (Metres)	5.35 metres")
                listbox4.insert(30, "Front Brake Type	Ventilated Disc")
                listbox4.insert(31, "Rear Brake Type	Ventilated Disc")
                listbox4.insert(32, "Acceleration	5.2 Seconds")
                listbox4.insert(33, "0-100kmph	5.2 Seconds")

                listbox4.insert(34, "Dimensions & Capacity")
                listbox4.insert(35, "Length (mm)	4881")
                listbox4.insert(36, "Width (mm)	2056")
                listbox4.insert(37, "Height (mm)	1353")
                listbox4.insert(38, "Boot Space (Litres)	260")
                listbox4.insert(39, "Seating Capacity	4")
                listbox4.insert(40, "Ground Clearance Unladen (mm)	100")
                listbox4.insert(41, "Wheel Base (mm)	2942")
                listbox4.insert(42, "Front Tread (mm)	1586")
                listbox4.insert(43, "Rear Tread (mm)	1590")
                listbox4.insert(44, "Kerb Weight (Kg)	1955")
                listbox4.insert(45, "No of Doors	2")
                listbox4.grid(row=0, column=0)
                button5 = Button(root17, text='B A C K', font='Georgia 15 italic', fg='white', bg='black',
                                 borderwidth=3, relief="flat", command=backpage)
                button5.grid(row=1, column=0, pady=30, padx=50)
                button6 = Button(root17, text='N E X T', font='Georgia 15 italic', fg='white', bg='black',
                                 borderwidth=3, relief="flat", command=nextpage)
                button6.grid(row=1, column=2, pady=50)

            def start():
                global i, show
                if i >= (len(images) - 1):
                    i = 0
                    slide_image.config(image=images[i])
                else:
                    i = i + 1
                    slide_image.configure(image=images[i])
                show = slide_image.after(2500, start)

            img1 = Image.open('L1.png')
            img1.thumbnail((840, 560))
            img2 = Image.open('L2.png')
            img2.thumbnail((840, 560))
            img3 = Image.open('L3.png')
            img3.thumbnail((840, 560))
            img4 = Image.open('L4.png')
            img4.thumbnail((840, 560))
            image1 = ImageTk.PhotoImage(img1)
            image2 = ImageTk.PhotoImage(img2)
            image3 = ImageTk.PhotoImage(img3)
            image4 = ImageTk.PhotoImage(img4)
            images = [image1, image2, image3, image4]
            i = 0
            slide_image = Label(root14, image=images[i])
            slide_image.grid(row=1, column=1, pady=20, padx=80)
            start()

            listbox = Listbox(root14, width=35, bd=20, bg='orange', selectbackground="green", height=7)
            listbox.insert(1, "Engine Type	V12 Petrol Engine")
            listbox.insert(2, "Displacement (cc)	6498")
            listbox.insert(3, "Max Power	770bhp@8500rpm")
            listbox.insert(4, "Max Torque	720Nm@6750rpm")
            listbox.insert(5, "No. of cylinder	12")
            listbox.insert(6, "Valves Per Cylinder	4")
            listbox.insert(7, "Valve Configuration	DOHC")
            listbox.insert(8, "Fuel Supply System	MPI")
            listbox.insert(9, "Bore X Stroke	95 X 76.4 mm")
            listbox.insert(10, "Compression Ratio	11.8:1")
            listbox.insert(11, "Super Charge	")
            listbox.insert(12, "TransmissionType	Automatic")
            listbox.insert(13, "Gear Box	7 Speed")
            listbox.insert(14, "Drive Type	4WD")
            listbox.insert(15, "Clutch Type	Dry Double plate")
            listbox.insert(16, "Fuel & Performance")
            listbox.insert(17, "Fuel Type	Petrol")
            listbox.insert(18, "Mileage (ARAI)	7.69")
            listbox.insert(19, "Fuel Tank Capacity (Litres)	90")
            listbox.insert(20, "Emission Norm Compliance	BS VI")
            listbox.insert(21, "Top Speed (Kmph)	351")
            listbox.insert(22, "Suspension, Steering & Brakes")
            listbox.insert(23, "Front Suspension	Horizontal Mono Tube Damper With Push Rod System")
            listbox.insert(24, "Rear Suspension	Horizontal Mono Tube Damper With Push Rod System")
            listbox.insert(25, "Steering Type	Power")
            listbox.insert(26, "Steering Column	Collapsible Steering")
            listbox.insert(27, "Steering Gear Type	Rack & Pinion")
            listbox.insert(28, "Turning Radius (Metres)	6.25 metres")
            listbox.insert(29, "Front Brake Type	Carbon Ceramic Brake")
            listbox.insert(30, "Rear Brake Type	Carbon Ceramic Brake")
            listbox.insert(31, "Acceleration	2.8 Seconds")
            listbox.insert(32, "0-100kmph	2.8 Seconds")
            listbox.insert(33, "Dimensions & Capacity")
            listbox.insert(34, "Length (mm)	4843")
            listbox.insert(35, "Width (mm)	2273")
            listbox.insert(36, "Height (mm)	1136")
            listbox.insert(37, "Boot Space (Litres)	110")
            listbox.insert(38, "Seating Capacity	2")
            listbox.insert(39, "Ground Clearance Unladen (mm)	125")
            listbox.insert(40, "Wheel Base (mm)	2700")
            listbox.insert(40, "Front Tread (mm)	1720")
            listbox.insert(42, "Rear Tread (mm)	1700")
            listbox.insert(43, "Kerb Weight (Kg)	1625")
            listbox.insert(44, "No of Doors	2")
            listbox.grid(row=0, column=0)

            button3 = Button(root14, text='B A C K', font='Georgia 15 italic', fg='white', bg='black',
                             borderwidth=3, relief="flat", command=backpage1)
            button3.grid(row=1, column=0, pady=10, padx=50)
            button4 = Button(root14, text='N E X T', font='Georgia 15 italic', fg='white', bg='black',
                             borderwidth=3, relief="flat", command=nextpage1)
            button4.grid(row=1, column=2, pady=10)

        def return_car():
            global bg7
            root19 = Toplevel(Root)
            root19.attributes('-fullscreen', True)
            root19.configure(background='black')
            bg7 = PhotoImage(file=r'return.png')
            bg7.subsample(1, 1)
            label2 = Label(root19, image=bg7)
            label2.place(x=0, y=0)

            label3 = Label(root19, text='L I C E N S E   N U M B E R', font='Georgia 15 bold', bg='black', fg='white')
            label3.grid(row=1, column=1, pady=20, padx=5)
            Id = Entry(root19, font='Georgia 13 bold', bg='white', fg='black')
            Id.grid(row=1, column=2, pady=20, padx=5)

            def back():
                customer_panel1()
                root19.destroy()

            def delete():
                global con, cur
                if Id.get() == "":
                    messagebox.showerror("Error", "Enter Your License number", parent=Root)
                    customer_panel1()

                else:
                    try:
                        con = mysql.connector.connect(host="localhost", user="root", password="root", database="car")
                        cur = con.cursor()
                        sql_Delete_query = "Delete from user_detail where License = %s"
                        cur.execute(sql_Delete_query, (Id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Successfully deleted")
                        cur.close()
                        con.close()
                    except Exception as es:
                        messagebox.showerror("Error", f"Error Dui to : {str(es)}")
                    finally:
                        if con.is_connected():
                            cur.close()
                            con.close()

            button5 = Button(root19, command=delete, font='Georgia 15 italic', fg='white', bg='black',
                             borderwidth=3, relief="flat", text='DELETE')
            button5.grid(row=2, column=2)

            button = Button(root19, text='BACK', fg='green', bg='black', font='georgia 12 italic', command=back,
                            image=bg3)
            button.grid(row=0, column=0, padx=5, pady=5)

        "------------------------ BUTTON ------------------------"
        button1 = Button(root13, text='R E N T   C A R', font='Georgia 15 italic', fg='white', bg='black',
                         borderwidth=3, relief="flat", command=rent)
        button1.grid(row=1, column=1, padx=10, pady=500)
        button2 = Button(root13, text='R E T U R N   C A R ', font='Georgia 15 italic', fg='white', bg='black',
                         borderwidth=3, relief="flat", command=return_car)
        button2.grid(row=1, column=2, padx=700)
        Button(root13, image=bg6, font='Georgia 15 italic', fg='white', bg='black', borderwidth=3,
               relief="flat", command=user).grid(row=0, column=0, padx=5, pady=5)

    def customer_detail():
        global bg7, issued_date, end_date, address, Phone
        root18 = Toplevel(Root)
        root18.attributes('-fullscreen', True)
        root18.configure(background='black')
        bg7 = PhotoImage(file='cust_detail.png')
        bg7.subsample(1, 1)
        label1 = Label(root18, image=bg7)
        label1.place(x=0, y=0)

        label3 = Label(root18, text='N A M E', font='Georgia 15 bold', bg='black', fg='white')
        label3.grid(row=0, column=0, pady=20, padx=5)

        name = Entry(root18, font='Georgia 15 bold', bg='black', fg='white')
        name.grid(row=0, column=1, padx=5)

        label4 = Label(root18, text='A G E', font='Georgia 15 bold', bg='black', fg='white')
        label4.grid(row=1, column=0, pady=20, padx=5)

        age = Entry(root18, font='Georgia 15 bold', bg='black', fg='white')
        age.grid(row=1, column=1, padx=5)

        label5 = Label(root18, text='G E N D E R', font='Georgia 15 bold', bg='black', fg='white')
        label5.grid(row=2, column=0, pady=20, padx=5)

        gender = Entry(root18, font='Georgia 15 bold', bg='black', fg='white')
        gender.grid(row=2, column=1, padx=5)

        label6 = Label(root18, text='L I C E N S E', font='Georgia 15 bold', bg='black', fg='white')
        label6.grid(row=3, column=0, pady=20, padx=5)

        lic = Entry(root18, font='Georgia 15 bold', bg='black', fg='white')
        lic.grid(row=3, column=1, padx=5)

        label7 = Label(root18, text='I S S U E D', font='Georgia 15 bold', bg='black', fg='white')
        label7.grid(row=4, column=0, pady=20, padx=5)

        issued = Entry(root18, font='Georgia 15 bold', bg='black', fg='white')
        issued.grid(row=4, column=1, padx=5)

        label8 = Label(root18, text='E N D  D A T E', font='Georgia 15 bold', bg='black', fg='white')
        label8.grid(row=5, column=0, pady=20, padx=5)

        end = Entry(root18, font='Georgia 15 bold', bg='black', fg='white')
        end.grid(row=5, column=1, padx=5)

        label9 = Label(root18, text='A D D R E S S', font='Georgia 15 bold', bg='black', fg='white')
        label9.grid(row=6, column=0, pady=20, padx=5)

        address = Entry(root18, font='Georgia 15 bold', bg='black', fg='white')
        address.grid(row=6, column=1, padx=5)

        label11 = Label(root18, text='D E S T I N A T I O N', font='Georgia 15 bold', bg='black', fg='white')
        label11.grid(row=7, column=0, pady=20, padx=5)

        destination = Entry(root18, font='Georgia 15 bold', bg='black', fg='white')
        destination.grid(row=7, column=1, padx=5)

        label12 = Label(root18, text='M O B I L E', font='Georgia 15 bold', bg='black', fg='white')
        label12.grid(row=8, column=0, pady=20, padx=5)

        phone = Entry(root18, font='Georgia 15 bold', bg='black', fg='white')
        phone.grid(row=8, column=1, padx=5)

        def add():
            global cur, con, Phone, home, issued_date, end_date
            if name.get() == "" or age.get() == "" or gender.get() == "" or lic.get() == "" or issued.get() == "" \
                    or end.get() == "" or address.get() == "" or destination.get() == "" \
                    or phone.get() == "":
                messagebox.showerror("Error", "Enter Details", parent=Root)
                customer_detail()
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
                    cur = con.cursor()
                    query = "insert into user_detail(name, age, gender, license, issued, end, address, " \
                            "destination, mob) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    Name = name.get()
                    Age = age.get()
                    Gender = gender.get()
                    License = lic.get()
                    issued_date = issued.get()
                    end_date = end.get()
                    home = address.get()
                    Destination = destination.get()
                    Phone = phone.get()
                    record = (Name, Age, Gender, License, issued_date, end_date, home, Destination, Phone)
                    cur.execute(query, record)
                    con.commit()
                    messagebox.showinfo("Success", "Successfully Submitted", parent=Root)
                    payment()
                    root18.destroy()
                except Exception as es:
                    messagebox.showerror("Error", f"Error Dui to : {str(es)}")
                finally:
                    if con.is_connected():
                        cur.close()
                        con.close()

        button6 = Button(root18, text='S U B M I T', command=add, font='Georgia 15 italic', fg='white', bg='black',
                         borderwidth=3, relief="flat")
        button6.grid(row=9, column=1)

    def payment():
        global bg7, n, company, a, name_card
        root22 = Toplevel(Root)
        root22.attributes('-fullscreen', True)
        root22.configure(background='black')
        bg7 = PhotoImage(file='payment.png')
        bg7.subsample(1, 1)
        label1 = Label(root22, image=bg7)
        label1.place(x=0, y=0)

        n = StringVar()
        text = StringVar()
        m = StringVar()
        a = StringVar()
        month = StringVar()
        month.set("MONTH")
        year = StringVar()
        year.set("YEAR")
        text.set("- - - -    - - - -    - - - -    - - - -")
        mode = Combobox(root22, width=27, textvariable=n)
        mode['values'] = ('CREDIT CARD', 'DEBIT CARD')
        mode.grid(column=1, row=0, pady=10)
        mode.current()

        company = Combobox(root22, width=30, textvariable=m)
        company['values'] = ("LAMBORGHINI (AVENTADOR)", "TESLA (S)", "MASERATI (LEVANTE)", "ROLLS ROYCE (GHOST)")
        company.grid(row=0, column=3, padx=10)
        company.current()

        month = Combobox(root22, width=10, textvariable=month)
        month['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
        month.grid(row=4, column=0)

        year = Combobox(root22, width=10, textvariable=year)
        year['values'] = ('2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030')
        year.grid(row=4, column=1)

        label2 = Label(root22, text='Choose Your Card', font='Georgia 15 bold')
        label2.grid(row=0, column=0, padx=10, pady=30)
        label3 = Label(root22, text='CARD NUMBER', font='Georgia 15 bold')
        label3.grid(row=1, column=0, padx=10, pady=30)

        card = Entry(root22, font='Georgia 15 bold', textvariable=text)
        card.grid(row=1, column=1, padx=10, pady=30)

        label4 = Label(root22, text='EXPIRY', font='Georgia 15 bold')
        label4.grid(row=3, column=0, padx=10, pady=30)
        label5 = Label(root22, text='CVV/SECURITY NO.', font='Georgia 15 bold')
        label5.grid(row=3, column=2, padx=10, pady=30)

        cvv = Entry(root22, font='Georgia 13 bold', width=5)
        cvv.grid(row=4, column=2, padx=10, pady=30)

        label6 = Label(root22, text='Name on Card', font='Georgia 15 bold')
        label6.grid(row=5, column=0, padx=10, pady=30)

        name_card = Entry(root22, font='Georgia 15 bold')
        name_card.grid(row=5, column=1, padx=10, pady=30)

        label7 = Label(root22, text="MODEL", font='Georgia 15 bold')
        label7.grid(row=0, column=2)
        pay = Label(root22, text="AMOUNT", font="Georgia 15 bold")
        pay.grid(row=7, column=0, pady=20)
        label8 = Entry(root22, textvariable=a, font="Georgia 15 bold")
        label8.grid(row=7, column=1)

        progress = Progressbar(root22, orient=HORIZONTAL, length=300,  mode='determinate')
        progress.grid(row=8, column=2, pady=40)

        def check():
            if company.get() == "LAMBORGHINI (AVENTADOR)":
                a.set("3,81,200")
            elif company.get() == "TESLA (S)":
                a.set("2,12,800")
            elif company.get() == "MASERATI (LEVANTE)":
                a.set("2,68,800")
            elif company.get() == "ROLLS ROYCE (GHOST)":
                a.set("2,01,600")

        def bar():
            global i
            import time
            for i in range(3):
                root22.update_idletasks()
                progress['value'] += 150

                time.sleep(1)

        def process():
            global cur, con
            if m.get() == "" or name_card.get() == "" or cvv.get() == "" or card.get() == "" or n.get() == "" \
                    or month.get() == "" or year.get() == "":
                messagebox.showerror("Error", "Enter Details", parent=Root)
                payment()
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
                    cur = con.cursor()
                    query = "insert into payment(type, name, amount, car_model) values(%s, %s, %s, %s)"
                    Name = name_card.get()
                    Amount = a.get()
                    Type = n.get()
                    Company = m.get()
                    record = (Type, Name, Amount, Company)
                    cur.execute(query, record)
                    con.commit()
                    bar()
                    messagebox.showinfo("Success", "Paid Successfully", parent=Root)
                    receipt()
                except Exception as es:
                    messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=Root)
                finally:
                    if con.is_connected():
                        cur.close()
                        con.close()

        button = Button(root22, text='Confirm', command=check, font="georgia 15 bold", bg='black', fg='cyan')
        button.grid(row=1, column=3, padx=10)
        button1 = Button(root22, text="PAY", command=process, font='Georgia 20 bold', bg='black', fg='cyan')
        button1.grid(row=10, column=2, padx=10, pady=20)

    def receipt():
        global bg4, n, company, a, name_card, issued_date, end_date, address, Phone, x, home
        r = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(5))
        root23 = Toplevel(Root)
        root23.configure(background='black')
        root23.attributes('-fullscreen', True)

        labelC = Label(root23, image=bg4)
        labelC.place(x=0, y=0)

        label = Label(root23, text="W A N D E R I N G   W H E E L S", font='georgia 15 italic', fg='white', bg='black',
                      relief="groove")
        label.grid(row=0, column=2, padx=100, pady=5)

        name = Label(root23, text='NAME', font='georgia 15 italic', fg='white', bg='black', relief="groove")
        name.grid(row=1, column=0, padx=10, pady=20)

        Name = Label(root23, text="", font='georgia 15 italic', fg='black', bg='white')
        Name.grid(row=1, column=1)

        Name.config(text=name_card.get())

        mobile = Label(root23, text='MOBILE', font='georgia 15 italic', fg='white', bg='black', relief="groove")
        mobile.grid(row=2, column=0, padx=10, pady=20)

        Mobile = Label(root23, text=f"{Phone}", font='georgia 15 italic', fg='black', bg='white')
        Mobile.grid(row=2, column=1)

        Address = Label(root23, text='ADDRESS', font='georgia 15 italic', fg='white', bg='black', relief="groove")
        Address.grid(row=3, column=0, padx=10, pady=20)

        address = Label(root23, text=f"{home}", font='georgia 15 italic', fg='black', bg='white')
        address.grid(row=3, column=1)

        R_no = Label(root23, text=f"{r}", font='georgia 15 italic', fg='black', bg='white')
        R_no.grid(row=0, column=3)

        car = Label(root23, text='CAR', font='georgia 15 italic', fg='white', bg='black', relief="groove")
        car.grid(row=5, column=0, padx=10, pady=20)

        Car = Label(root23, text="", font='georgia 15 italic', fg='black', bg='white')
        Car.grid(row=5, column=1)

        Car.configure(text=company.get())

        amount = Label(root23, text='AMOUNT', font='georgia 15 italic', fg='white', bg='black', relief="groove")
        amount.grid(row=6, column=0, padx=10, pady=20)

        Amount = Label(root23, text="", font='georgia 15 italic', fg='black', bg='white')
        Amount.grid(row=6, column=1)

        Amount.configure(text=a.get())

        Date = Label(root23, text='DATE', font='georgia 15 italic', fg='white', bg='black', relief="groove")
        Date.grid(row=7, column=0, padx=10, pady=20)

        Issued = Label(root23, text=f"{issued_date}", font='georgia 15 italic', fg='black', bg='white')
        Issued.grid(row=7, column=1, padx=10, pady=20)

        To = Label(root23, text='T O', font='georgia 15 italic', fg='white', bg='black', relief="groove")
        To.grid(row=7, column=2, padx=10, pady=20)

        End = Label(root23, text=f"{end_date}", font='georgia 15 italic', fg='black', bg='white')
        End.grid(row=7, column=3, padx=10, pady=20)

        mode = Label(root23, text="PAYMENT THROUGH", font='georgia 15 italic', fg='white', bg='black', relief="groove")
        mode.grid(row=8, column=0, padx=10, pady=20)

        Mode = Label(root23, text="", font='georgia 15 italic', fg='black', bg='white')
        Mode.grid(row=8, column=1)

        Mode.configure(text=n.get())

        def data():
            global cur, con, n, company, a, name_card, issued_date, end_date, address, Phone, x, home
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="1234", database="car")
                cur = con.cursor()
                query = "insert into receipt(name, mobile, address, r_no, company, amount, issued_date, end_date, " \
                        " type) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                R_Name = name_card.get()
                R_Mobile = Phone
                R_Address = home
                R_number = r
                R_company = company.get()
                R_amount = a.get()
                R_issued = issued_date
                R_end = end_date
                R_type = n.get()
                record = (R_Name, R_Mobile, R_Address, R_number, R_company, R_amount, R_issued, R_end, R_type)
                cur.execute(query, record)
                con.commit()
                messagebox.showinfo("Success", "Successfully inserted", parent=Root)
                Root.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=Root)
            finally:
                if con.is_connected():
                    cur.close()
                    con.close()

        Button(root23, text="E X I T", font='georgia 15 italic', fg='black', bg='white', command=data) \
            .grid(row=9, column=2, pady=30)

    "----------------------------------------------- LABEL -----------------------------------------------"
    labelB = Label(Root, text='W E L C O M E   TO    "W A N D E R   W H E E L S"',
                   font='Georgia 20 italic', fg='white', relief="flat", borderwidth=20, bg="black")
    labelB.grid(row=0, column=1, padx=30,  pady=5)

    "----------------------------------------------- BUTTON -----------------------------------------------"
    btnA = Button(Root, text='C U S T O M E R', font='Georgia 15 italic', fg='white', bg='black', borderwidth=1,
                  relief="flat", command=customer_panel1)
    btnA.grid(row=3, column=0, padx=15, pady=500)
    btnB = Button(Root, text='A D M I N I S T R A T O R', font='Georgia 15 italic', fg='white', bg='black',
                  command=admin_login, borderwidth=1, relief="flat")
    btnB.grid(row=3, columnspan=2, padx=50, pady=15)


Button(Frame, text="S T A R T", font="georgia 15 bold", bg="black", fg="green", command=running).\
    grid(row=0, column=0, padx=70, pady=20)
Button(Frame, text="S T O P", font="georgia 15 bold", bg="black", fg="red", command=Frame.destroy).\
    grid(row=1, column=0, padx=70, pady=20)
mainloop()
