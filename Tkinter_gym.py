import tkinter as tk
import mysql.connector as mys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


#LOGIN FRAME
def loginscr():
    #FUNCTIONS

    def funclear(): #command for clear button
        txtUser.delete(0,END)
        txtpass.delete(0,END)

    def funlogin(): #command for login button
        passw=txtpass.get()
        if passw=="adis":
            myconn=mys.connect(host="localhost",user="root",password="1234",database="myprojects")
            cursor = myconn.cursor()
            messagebox.showinfo("Login Sucessful","LOGIN SUCCESSFUL")
            root.destroy()
            menu()
            
        else:
            messagebox.showinfo("Login Failed" , "Login Failed Try Again")

    #GUI
    root=tk.Tk()
    root.geometry("300x300")
    root.title("TOP GYM LOGIN")
    root["background"] = "salmon"
    
    #background
    bg=PhotoImage(file="nebula_space_red.png")
    canvas01 = Canvas(root, height = 250, width = 300)
    canvas01.pack(fill= "both",expand=True)  
    canvas01.create_image(0,0,image = bg, anchor ='nw')

    #Labels and texts
    lbluser=tk.Label(root,text="Username -",bg="thistle1",font=("Times New Roman Bold",10),borderwidth=0)
    lbluser.place(x=50,y=50)
    txtUser=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10),borderwidth=0)
    txtUser.place(x=150,y=50,width=100,)
    lblpass=tk.Label(root, text="Password -", bg="thistle1", font=("Times New Roman Bold", 10))
    lblpass.place(x=50,y=100)
    txtpass=tk.Entry(root,show="*",width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtpass.place(x=150,y=100,width=100)
    btnlogin=tk.Button(root, text="Login", bg="goldenrod1",font=("Times New Roman Bold",10), command=funlogin)
    btnlogin.place(x=50,y=150,width=80)
    btnclear=tk.Button(root,text="Clear",bg="goldenrod1",font=("Times New Roman Bold",10),command=funclear)
    btnclear.place(x=150,y=150,width=80)
    root.mainloop()
    
    
    


#THE MENU FRAME

def menu():

    #GUI
    root = tk.Tk()
    root.geometry("1200x500")
    root.title("TOP GYM MANAGEMENT")
    root["background"] = "gray18"

    #background
    bg=PhotoImage(file="nebula_space_black.png")
    canvas1 = Canvas(root, height = 400, width = 300)
    canvas1.pack(fill= "both",expand=True)  
    canvas1.create_image(0,0,image = bg, anchor ='nw')

    photo=tk.PhotoImage(file="strong.gif")
    Button(image = photo)
    Button(root, image = photo, fg ="black",bg="black").place(x=0,y=0)

    #labels, texts and buttons

    btntransaction = tk.Button(root, text="STATISTICS",bg="goldenrod1",font= ("Times New Roman Bold", 10),command=Statistics)
    btntransaction.place(x = 100, y=400, width=150)
    

    lblwelc = tk.Label(root, text = " MANAGEMENT SYSTEM ", fg ="black", bg="goldenrod1",font = ("Times New Roman Bold", 33))
  
    lblwelc.place(x = 500, y = 50)

    btninsert = tk.Button(root, text ="INSERT",bg="goldenrod1",font = ("Times New Roman Bold", 10),command=insert)
    btninsert.place(x = 400, y = 300, width = 150)

    btnupdate = tk.Button(root, text ="UPDATE",bg="goldenrod1",font = ("Times New Roman Bold", 10),command=update)
    btnupdate.place(x = 600, y = 300, width = 150)

    btndelete = tk.Button(root, text ="DELETE",bg="goldenrod1",font = ("Times New Roman Bold", 10),command=delete)
    btndelete.place(x = 800, y = 300, width = 150)

    btndisplay = tk.Button(root, text ="DISPLAY",bg="goldenrod1",font = ("Times New Roman Bold", 10),command=display)
    btndisplay.place(x = 1000, y = 300, width = 150)

    btntransaction = tk.Button(root, text="TRANSACTION",bg="goldenrod1",font= ("Times New Roman Bold", 10),command=transaction)
    btntransaction.place(x = 700, y=200, width=150)

    
    btnsearch = tk.Button(root, text="SEARCH",bg="goldenrod1", font = ("Times New Roman Bold", 10),command=search)
    btnsearch.place(x = 700 , y=400 , width=150)
    root.mainloop()

#INSERT

def insert():

    #FUNCTIONS 

    def CHECKED(gender): #accepts argument from lambda

        global genderm

        if gender=="male":
            genderm="Male"
        elif gender=="female":
            genderm="Female"


    def fun_insert(): #command for insert button
        try:
            
            
            myconn=mys.connect(host="localhost",user="root",password="1234",database="myprojects")
            mycursor=myconn.cursor()
            
           

            membernumber = txtmemberno.get()
            membername = txtmembername.get()
            mobilenumber = txtmobileno.get()
            dob = txtdob.get()
            service = service_options.get()
            duration = duration_options.get()
            
            
            

            query="insert into insert_table values ({},'{}',{},'{}','{}','{}','{}')".format(membernumber,membername,mobilenumber,dob,genderm,service,duration)
            mycursor.execute(query)

            myconn.commit()

            messagebox.showinfo("INSERT","INSERTED SUCCESSFULLY")
            
            root.destroy()
            
            
        
    
            for i in mycursor:
                print(i)

        except Exception as e:
            print(e)
            

    

    def funclear_insert():
        txtmemberno.delete(0,END)
        txtmembername.delete(0,END)
        txtmobileno.delete(0,END)
        txtdob.delete(0,END)
        male.deselect()
        female.deselect()

    
    #GUI
    root = tk.Tk()
    root.geometry("400x600")
    root.title("Insert")
    root["background"] = "black"

    

 
    

    

    cb_male=IntVar()
    cb_female=IntVar()

    #CHECK BOXES 
    male = Checkbutton(root, text = "Male",variable=cb_male,command=lambda:CHECKED('male'))
    male.place(x = 25, y = 25)

    female = Checkbutton(root, text = "Female",variable=cb_female,command=lambda:CHECKED('female'))
    female.place(x = 150 , y = 25)


    #DROP DOWN BOXES
    service_options = tk.StringVar(root)
    service_options.set('Gym')
    optionMenu = tk.OptionMenu(root, service_options, 'Gym', 'Sauna', 'Yoga', 'Zumba',"Kickboxing")#SERVICES
    optionMenu.place(x = 150 , y = 375)

    duration_options = tk.StringVar(root)
    duration_options.set('3months')
    durationmenu = tk.OptionMenu(root, duration_options, '1month', '2months', '3months', '6months','1year')
    durationmenu.place(x = 150 , y = 425 )
    

    

    

    #labels and text
    lblmemberno=tk.Label(root,text="Member no. :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmemberno.place(x=25,y=100,width=100)
    txtmemberno=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmemberno.place(x=150,y=100,width=100)

    lblmembername=tk.Label(root, text="Member name :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lblmembername.place(x=25,y=175,width=100)
    txtmembername=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtmembername.place(x=150,y=175,width=100)

    lblmobileno=tk.Label(root,text="Mobile no. :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmobileno.place(x=25,y=250,width=100)
    txtmobileno=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmobileno.place(x=150,y=250,width=100)

    lbldob=tk.Label(root, text="Date of Birth :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lbldob.place(x=25,y=325,width=100)
    txtdob=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtdob.place(x=150,y=325,width=100)

    btnclear=tk.Button(root,text="Clear",bg="thistle1",font=("Times New Roman Bold",10),command=funclear_insert)
    btnclear.place(x=25,y=525,width=80)

    btninsert=tk.Button(root,text="Insert",bg="thistle1",font=("Times New Roman Bold",10),command=fun_insert)
    btninsert.place(x=150,y=525,width=80)

    lblservice=tk.Label(root,text="Service :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblservice.place(x=25,y=380,width=100)
    lblduration=tk.Label(root,text="Duration :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblduration.place(x=25,y=430,width=100)

    root.mainloop()

    


def display():
    try:
        myconn = mys.connect(host="localhost", user="root", password="1234", database="myprojects")

        if myconn.is_connected():
            print("connection sucessful")
        
            mycur = myconn.cursor()
            query = "select * from insert_table order by membernumber"
            mycur.execute(query)
            rs = mycur.fetchall()

        root = tk.Tk() 
        root.geometry("1400x800")
        root.title("GYM DATABASE")
        root['background'] = "RosyBrown1"

        bg=ImageTk.PhotoImage(file="nebula_space_red_blue.jpg",master=root)
        canvas01 = Canvas(root, height = 1400, width = 800)
        
        canvas01.create_image(0,0,image = bg, anchor ='nw')

        canvas01.image=bg
        
        canvas01.place(relx=0,rely=0,width=1400)



        ttk.Label(root, text = "GYM DATABASE", font = ("Times New Roman Bold",20)).pack()
        frame=Frame(root)
        frame.pack()
        tree=ttk.Treeview(frame, columns = (1,2,3,4,5,6,7), height = 300, show='headings')
        tree.pack(side='right')
        tree.heading(1, text = "MEMBERNO")
        tree.heading(2, text = "MEMBERNAME")
        tree.heading(3, text = "PHONENUMBER")
        tree.heading(4, text = "DATE")
        tree.heading(5, text = "GENDER")
        tree.heading(6, text = "SERVICE")
        tree.heading(7, text = "DURATION")
        tree.column(1, width = 130)
        tree.column(2, width = 130)
        tree.column(3, width = 130)
        tree.column(4, width = 130)
        tree.column(5, width = 130)
        tree.column(6, width = 130)
        tree.column(7, width = 130)

        scroll = ttk.Scrollbar(frame, orient= "vertical", command=tree.yview)
        scroll.pack(side= 'right', fill= 'y')

        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1], val[2], val[3], val[4], val[5], val[6]))


    except Exception as e:
        print(e)


def update():

    def funclear_update():
        txtmemberno.delete(0,END)
        txtmembername.delete(0,END)
        txtmobileno.delete(0,END)
        txtdob.delete(0,END)
        
    
    def fun_update():
        try:
            
            
            myconn=mys.connect(host="localhost",user="root",password="1234",database="myprojects")
            mycursor=myconn.cursor()
            
           

            membernumber = txtmemberno.get()
            membername = txtmembername.get()
            mobilenumber = txtmobileno.get()
            dob = txtdob.get()
            service = service_options.get()
            duration = duration_options.get()
            
            
            
            mycur=myconn.cursor()

            query="update insert_table set membernumber = {}, mobilenumber= {}, dob= '{}', service='{}' , duration = '{}' where membernumber = {}".format(membernumber,mobilenumber,dob,service,duration,membernumber)
            
            mycur.execute(query)

            myconn.commit()

            messagebox.showinfo("MEMBER RECORD","MEMBER UPDATED SUCCESFULLY")
            
            root.destroy()
            
            
        
    
            for i in mycursor:
                print(i)

        except Exception as e:
            print(e)
        
    def update_search():
        try:
            
            
            myconn=mys.connect(host="localhost",user="root",password="1234",database="myprojects")
            mycursor=myconn.cursor()
            
           
            membernumbersearch = txtmembernumbersearch.get()
            membernumber = txtmemberno.get()
            membername = txtmembername.get()
            mobilenumber = txtmobileno.get()
            dob = txtdob.get()
            service = service_options.get()
            duration = duration_options.get()
            
            
            mycur=myconn.cursor()

            query=("select * from insert_table where membernumber = {}".format(membernumbersearch))
            
            mycur.execute(query)

            rs=mycur.fetchone()
            rs=list(rs)
            membernumber=rs[0]
            membername=rs[1]
            mobilenumber=rs[2]
            dob=rs[3]
            service=rs[5]
            duration=rs[6]

            if rs==None:
                messagebox.showinfo("MEMBER INFO", "NO SUCH MEMBER FOUND  ")
            else:
                messagebox.showinfo("MEMBER INFO","MEMBER FOUND")
                txtmemberno.insert(END,membernumber)
                txtmembername.insert(END,membername)
                txtmobileno.insert(END,mobilenumber)
                txtdob.insert(END,dob)
                service_options.set(service)
                duration_options.set(duration)
    
            for i in mycursor:
                print(i)

        except Exception as e:
            print(e)

            

            

    #GUI
    root = tk.Tk()
    root.geometry("400x600")
    root.title("Insert")
    root["background"] = "gray18"


 
  

    #DROP DOWN BOXES
    service_options = tk.StringVar(root)
    service_options.set('Gym')
    optionMenu = tk.OptionMenu(root, service_options, 'Gym', 'Sauna', 'Yoga', 'Zumba',"Kickboxing")#SERVICES
    optionMenu.place(x = 150 , y = 375)

    duration_options = tk.StringVar(root)
    duration_options.set('3months')
    durationmenu = tk.OptionMenu(root, duration_options, '1month', '2months', '3months', '6months','1year')#DURATION
    durationmenu.place(x = 150 , y = 425 )
    

    

    

    #labels and text
    lblmembernumbersearch=tk.Label(root,text="Search MEMB.NO :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmembernumbersearch.place(x=15,y=25,width=125)
    txtmembernumbersearch=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmembernumbersearch.place(x=150,y=25,width=100)

    lblmemberno=tk.Label(root,text="Member no. :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmemberno.place(x=25,y=60,width=100)
    txtmemberno=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmemberno.place(x=150,y=60,width=100)

    lblmembername=tk.Label(root, text="Member name :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lblmembername.place(x=25,y=100,width=100)
    txtmembername=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtmembername.place(x=150,y=100,width=100)

    lblmobileno=tk.Label(root,text="Mobile no. :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmobileno.place(x=25,y=175,width=100)
    txtmobileno=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmobileno.place(x=150,y=175,width=100)

    lbldob=tk.Label(root, text="Date of Birth :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lbldob.place(x=25,y=250,width=100)
    txtdob=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtdob.place(x=150,y=250,width=100)

    btnclear=tk.Button(root,text="Clear",bg="thistle1",font=("Times New Roman Bold",10),command=funclear_update)
    btnclear.place(x=25,y=525,width=80)

    btnupdate=tk.Button(root,text="Update",bg="thistle1",font=("Times New Roman Bold",10),command=fun_update)
    btnupdate.place(x=150,y=525,width=80)

    btnsearch=tk.Button(root,text="Search",bg="thistle1",font=("Times New Roman Bold",10),command=update_search)
    btnsearch.place(x=275,y=525,width=80)

    lblservice=tk.Label(root,text="Service :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblservice.place(x=25,y=380,width=100)
    lblduration=tk.Label(root,text="Duration :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblduration.place(x=25,y=430,width=100)

    root.mainloop()


def search():

    def funsearch_clear():

        txtmemberno.delete(0,END)
        txtmembername.delete(0,END)
        txtmobileno.delete(0,END)
        txtdob.delete(0,END)

    
    def search_search():
        try:
            
            
            myconn=mys.connect(host="localhost",user="root",password="1234",database="myprojects")
            mycursor=myconn.cursor()
            
           
            membernumbersearch = txtmembernumbersearch.get()
            membernumber = txtmemberno.get()
            membername = txtmembername.get()
            mobilenumber = txtmobileno.get()
            dob = txtdob.get()
            service = service_options.get()
            duration = duration_options.get()

            
            
            mycur=myconn.cursor()

            query=("select * from insert_table where membernumber = {}".format(membernumbersearch))
            
            mycur.execute(query)

            rs=mycur.fetchone()
            rs=list(rs)
            membernumber=rs[0]
            membername=rs[1]
            mobilenumber=rs[2]
            dob=rs[3]
            service=rs[5]
            duration=rs[6]

            if rs==None:
                messagebox.showinfo("MEMBER INFO", "NO SUCH MEMBER FOUND  ")
            else:
                messagebox.showinfo("MEMBER INFO","MEMBER FOUND")
                txtmemberno.insert(END,membernumber)
                txtmembername.insert(END,membername)
                txtmobileno.insert(END,mobilenumber)
                txtdob.insert(END,dob)
                service_options.set(service)
                duration_options.set(duration)




            
            
        
    
            for i in mycursor:
                print(i)

        except Exception as e:
            print(e)

            

            

    #GUI
    root = tk.Tk()
    root.geometry("400x600")
    root.title("Insert")
    root["background"] = "black"

    

 
  

    #DROP DOWN BOXES
    service_options = tk.StringVar(root)
    service_options.set('Gym')
    optionMenu = tk.OptionMenu(root, service_options, 'Gym', 'Sauna', 'Yoga', 'Zumba',"Kickboxing")#SERVICES
    optionMenu.place(x = 150 , y = 375)

    duration_options = tk.StringVar(root)
    duration_options.set('3months')
    durationmenu = tk.OptionMenu(root, duration_options, '1month', '2months', '3months', '6months','1year')#DURATION
    durationmenu.place(x = 150 , y = 425 )
    

    

    

    #labels and text
    lblmembernumbersearch=tk.Label(root,text="Search MEMB.NO :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmembernumbersearch.place(x=15,y=25,width=125)
    txtmembernumbersearch=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmembernumbersearch.place(x=150,y=25,width=100)

    lblmemberno=tk.Label(root,text="Member no. :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmemberno.place(x=25,y=60,width=100)
    txtmemberno=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmemberno.place(x=150,y=60,width=100)

    lblmembername=tk.Label(root, text="Member name :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lblmembername.place(x=25,y=100,width=100)
    txtmembername=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtmembername.place(x=150,y=100,width=100)

    lblmobileno=tk.Label(root,text="Mobile no. :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmobileno.place(x=25,y=175,width=100)
    txtmobileno=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmobileno.place(x=150,y=175,width=100)

    lbldob=tk.Label(root, text="Date of Birth :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lbldob.place(x=25,y=250,width=100)
    txtdob=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtdob.place(x=150,y=250,width=100)

    btnclear=tk.Button(root,text="Clear",bg="thistle1",font=("Times New Roman Bold",10),command=funsearch_clear)
    btnclear.place(x=25,y=525,width=80)

    btnsearch=tk.Button(root,text="Search",bg="thistle1",font=("Times New Roman Bold",10),command=search_search)
    btnsearch.place(x=150,y=525,width=80)

    lblservice=tk.Label(root,text="Service :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblservice.place(x=25,y=380,width=100)
    lblduration=tk.Label(root,text="Duration :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblduration.place(x=25,y=430,width=100)

    root.mainloop()


def delete():

    def delete_clear():
        
        txtmemberno.delete(0,END)
        txtmembername.delete(0,END)
        txtmobileno.delete(0,END)
        txtdob.delete(0,END)
        
    
    def delete_delete():
        try:
            

            myconn=mys.connect(host="localhost",user="root",password="1234",database="myprojects")
            mycursor=myconn.cursor()
            
           

            membernumber = txtmemberno.get()

            mycur=myconn.cursor()

            query="delete from insert_table where membernumber={}".format(membernumber)
            
            mycur.execute(query)

            myconn.commit()

            messagebox.showinfo("MEMBER RECORD","MEMBER DELETED SUCCESSFULLY")
            
            root.destroy()
            
            
        
    
            for i in mycursor:
                print(i)

        except Exception as e:
            print(e)
        
    def delete_search():
        try:
            
            
            myconn=mys.connect(host="localhost",user="root",password="1234",database="myprojects")
            mycursor=myconn.cursor()
            
           
            membernumbersearch = txtmembernumbersearch.get()
            membernumber = txtmemberno.get()
            membername = txtmembername.get()
            mobilenumber = txtmobileno.get()
            dob = txtdob.get()
            service = service_options.get()
            duration = duration_options.get()
            
            
            mycur=myconn.cursor()

            query=("select * from insert_table where membernumber = {}".format(membernumbersearch))
            
            mycur.execute(query)

            rs=mycur.fetchone()
            rs=list(rs)
            membernumber=rs[0]
            membername=rs[1]
            mobilenumber=rs[2]
            dob=rs[3]
            service=rs[5]
            duration=rs[6]

            if rs==None:
                messagebox.showinfo("MEMBER INFO", "NO SUCH MEMBER FOUND  ")
            else:
                messagebox.showinfo("MEMBER INFO","MEMBER FOUND")
                txtmemberno.insert(END,membernumber)
                txtmembername.insert(END,membername)
                txtmobileno.insert(END,mobilenumber)
                txtdob.insert(END,dob)
                service_options.set(service)
                duration_options.set(duration)
    
            for i in mycursor:
                print(i)

        except Exception as e:
            print(e)

            

            

    #GUI
    root = tk.Tk()
    root.geometry("400x600")
    root.title("Insert")
    root["background"] = "black"

    

 
  

    #DROP DOWN BOXES
    service_options = tk.StringVar(root)
    service_options.set('Gym')
    optionMenu = tk.OptionMenu(root, service_options, 'Gym', 'Sauna', 'Yoga', 'Zumba',"Kickboxing")#SERVICES
    optionMenu.place(x = 150 , y = 375)

    duration_options = tk.StringVar(root)
    duration_options.set('3months')
    durationmenu = tk.OptionMenu(root, duration_options, '1month', '2months', '3months', '6months','1year')#DURATION
    durationmenu.place(x = 150 , y = 425 )
    

    

    

    #labels and text
    lblmembernumbersearch=tk.Label(root,text="Search MEMB.NO :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmembernumbersearch.place(x=15,y=25,width=125)
    txtmembernumbersearch=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmembernumbersearch.place(x=150,y=25,width=100)

    lblmemberno=tk.Label(root,text="Member no. :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmemberno.place(x=25,y=60,width=100)
    txtmemberno=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmemberno.place(x=150,y=60,width=100)

    lblmembername=tk.Label(root, text="Member name :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lblmembername.place(x=25,y=100,width=100)
    txtmembername=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtmembername.place(x=150,y=100,width=100)

    lblmobileno=tk.Label(root,text="Mobile no. :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmobileno.place(x=25,y=175,width=100)
    txtmobileno=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmobileno.place(x=150,y=175,width=100)

    lbldob=tk.Label(root, text="Date of Birth :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lbldob.place(x=25,y=250,width=100)
    txtdob=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtdob.place(x=150,y=250,width=100)

    btnclear=tk.Button(root,text="Clear",bg="thistle1",font=("Times New Roman Bold",10),command=delete_clear)
    btnclear.place(x=25,y=525,width=80)

    btndelete=tk.Button(root,text="Delete",bg="thistle1",font=("Times New Roman Bold",10),command=delete_delete)
    btndelete.place(x=150,y=525,width=80)

    btnsearch=tk.Button(root,text="Search",bg="thistle1",font=("Times New Roman Bold",10),command=delete_search)
    btnsearch.place(x=275,y=525,width=80)

    lblservice=tk.Label(root,text="Service :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblservice.place(x=25,y=380,width=100)
    lblduration=tk.Label(root,text="Duration :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblduration.place(x=25,y=430,width=100)

    root.mainloop()


def transaction():

    def transaction_clear():
        txtmemberno.delete(0,END)
        txtmembername.delete(0,END)
        txtmobileno.delete(0,END)
        txtdob.delete(0,END)
        
    
    def transaction_calculate():
        
        discount=0

        service = service_options.get()
        duration = duration_options.get()
        discount_txt = txtdiscount.get()
        discount = int(discount_txt)
        
        month_1=1
        month_2=2
        month_3=3
        month_6=6
        month_12=12

        service_Gym=150
        service_Yoga=250
        service_Sauna=200
        service_Zumba=100
        service_Kickboxing=250

        netamt=0
        
        

        if service == "Gym":

            if duration == "1month":
                netamt=(service_Gym*month_1)-discount
            elif duration == "2months":
                netamt=(service_Gym*month_2)-discount
            elif duration == "3months":
                netamt=(service_Gym*month_3)-discount
            elif duration == "6months":
                netamt=(service_Gym*month_6)-discount
            elif duration == "1year":
                netamt=(service_Gym*month_12)-discount

        if service == "Sauna":

            if duration == "1month":
                netamt=(service_Sauna*month_1)-discount
            elif duration == "2months":
                netamt=(service_Sauna*month_2)-discount
            elif duration == "3months":
                netamt=(service_Sauna*month_3)-discount
            elif duration == "6months":
                netamt=(service_Sauna*month_6)-discount
            elif duration == "1year":
                netamt=(service_Sauna*month_12)-discount

        if service == "Yoga":

            if duration == "1month":
                netamt=(service_Yoga*month_1)-discount
            elif duration == "2months":
                netamt=(service_Yoga*month_2)-discount
            elif duration == "3months":
                netamt=(service_Yoga*month_3)-discount
            elif duration == "6months":
                netamt=(service_Yoga*month_6)-discount
            elif duration == "1year":
                netamt=(service_Yoga*month_12)-discount

        if service == "Kickboxing":

            if duration == "1month":
                netamt=(service_Kickboxing*month_1)-discount
            elif duration == "2months":
                netamt=(service_Kickboxing*month_2)-discount
            elif duration == "3months":
                netamt=(service_Kickboxing*month_3)-discount
            elif duration == "6months":
                netamt=(service_Kickboxing*month_6)-discount
            elif duration == "1year":
                netamt=(service_Kickboxing*month_12)-discount

        if service == "Zumba":
            
            if duration == "1month":
                netamt=(service_Zumba*month_1)-discount
            elif duration == "2months":
                netamt=(service_Zumba*month_2)-discount
            elif duration == "3months":
                netamt=(service_Zumba*month_3)-discount
            elif duration == "6months":
                netamt=(service_Zumba*month_6)-discount
            elif duration == "1year":
                netamt=(service_Zumba*month_12)-discount
        
        messagebox.showinfo("TRANSACTION","TRANSACTED")
        txttotalamt.insert(END,netamt)




    def transaction_search():
        try:
            
            
            myconn=mys.connect(host="localhost",user="root",password="1234",database="myprojects")
            mycursor=myconn.cursor()
            
           
           
            membernumbersearch = txtmembernumbersearch.get()
            membernumber = txtmemberno.get()
            membername = txtmembername.get()
            mobilenumber = txtmobileno.get()
            dob = txtdob.get()
            service = service_options.get()
            duration = duration_options.get()
            
            
            mycur=myconn.cursor()

            query=("select * from insert_table where membernumber = {}".format(membernumbersearch))
            
            mycur.execute(query)

            rs=mycur.fetchone()
            rs=list(rs)
            membernumber=rs[0]
            membername=rs[1]
            mobilenumber=rs[2]
            dob=rs[3]
            service=rs[5]
            duration=rs[6]

            if rs==None:
                messagebox.showinfo("MEMBER INFO", "NO SUCH MEMBER FOUND  ")
            else:
                messagebox.showinfo("MEMBER INFO","MEMBER FOUND")
                txtmemberno.insert(END,membernumber)
                txtmembername.insert(END,membername)
                txtmobileno.insert(END,mobilenumber)
                txtdob.insert(END,dob)
                service_options.set(service)
                duration_options.set(duration)
    
            for i in mycursor:
                print(i)

        except Exception as e:
            print(e)

            

            

    #GUI
    root = tk.Tk()
    root.geometry("600x500")
    root.title("Insert")
    root["background"] = "black"

    
 
  

    #DROP DOWN BOXES
    service_options = tk.StringVar(root)
    service_options.set('Gym')
    optionMenu = tk.OptionMenu(root, service_options, 'Gym', 'Sauna', 'Yoga', 'Zumba', 'Kickboxing')#SERVICES
    optionMenu.place(x = 150 , y = 275)

    duration_options = tk.StringVar(root)
    duration_options.set('3months')
    durationmenu = tk.OptionMenu(root, duration_options, '1month', '2months', '3months', '6months','1year')#DURATION
    durationmenu.place(x = 450 , y = 275 )
    

    

    

    #labels and text
    lblmembernumbersearch=tk.Label(root,text="Search MEMB.NO :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmembernumbersearch.place(x=175,y=25,width=125)
    txtmembernumbersearch=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmembernumbersearch.place(x=335,y=25,width=100)

    lblmemberno=tk.Label(root,text="Member no. :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmemberno.place(x=25,y=75,width=100)
    txtmemberno=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmemberno.place(x=150,y=75,width=100)

    lblmembername=tk.Label(root, text="Member name :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lblmembername.place(x=310,y=75,width=100)
    txtmembername=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtmembername.place(x=450,y=75,width=100)

    lblmobileno=tk.Label(root,text="Mobile no. :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblmobileno.place(x=25,y=175,width=100)
    txtmobileno=tk.Entry(root, width=35, bg='thistle1', font=("Times New Roman Bold",10))
    txtmobileno.place(x=150,y=175,width=100)

    lbldob=tk.Label(root, text="Date of Birth :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lbldob.place(x=310,y=175,width=100)
    txtdob=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtdob.place(x=450,y=175,width=100)

    #BUTTONS
    btnclear=tk.Button(root,text="Clear",bg="thistle1",font=("Times New Roman Bold",10),command=transaction_clear)
    btnclear.place(x=25,y=450,width=80)

    btnupdate=tk.Button(root,text="Calculate",bg="thistle1",font=("Times New Roman Bold",10),command=transaction_calculate)
    btnupdate.place(x=150,y=450,width=80)

    btnsearch=tk.Button(root,text="Search",bg="thistle1",font=("Times New Roman Bold",10),command=transaction_search)
    btnsearch.place(x=275,y=450,width=80)

    #labels and text

    lblservice=tk.Label(root,text="Service :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblservice.place(x=25,y=275,width=100)
    lblduration=tk.Label(root,text="Duration :-",bg="thistle1",font=("Times New Roman Bold",10))
    lblduration.place(x=310,y=275,width=100)

    lbldiscount=tk.Label(root, text="Discount :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lbldiscount.place(x=310,y=375,width=100)
    txtdiscount=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txtdiscount.place(x=450,y=375,width=100)

    lblinfo=tk.Label(root, text="Enter above the amount to be deducted from the total", bg="thistle1", font=("Times New Roman Bold", 10))
    lblinfo.place(x=280,y=415,width=300)

    lbltotalamt=tk.Label(root, text="Total Amt :-", bg="thistle1", font=("Times New Roman Bold", 10))
    lbltotalamt.place(x=25,y=375,width=100)
    txttotalamt=tk.Entry(root,width=35,bg="thistle1", font=("Times New Roman Bold",10))
    txttotalamt.place(x=150,y=375,width=100)



    root.mainloop()

def Statistics():
    #zumba, kickboxing, yoga, sauna, gym 
    try:
        myconn = mys.connect(host="localhost", user="root", password="1234", database="myprojects")

        if myconn.is_connected():
            print("connection sucessful")
        
            mycur = myconn.cursor()
            query = "select membernumber, service from insert_table"
            mycur.execute(query)
            rs = mycur.fetchall()

            Service_graph=[]
            Name_graph=[]

            for i in rs:
                Name_graph.append(i[0])
                Service_graph.append(i[1])

            print("Name of Members = ", Name_graph)
            print("Service  = ", Service_graph)
            #GRAPH
            
            plt.bar(Name_graph,Service_graph)
            plt.ylim(0, 10)
            plt.xlabel("Service")
            plt.ylabel("Member Name")
            plt.title("Gym Statistics")
            plt.show()

    except Exception as e:
        print(e)            



loginscr()