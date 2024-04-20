from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

root = Tk()
root.geometry("1530x700")
root.title("Employee Mangement System")

l_title = Label(text="Employee Mangement System",font="lato 40 bold",fg="darkblue",bg="white")
l_title.place(x=0,y=0,width=1530,height=60)

# VARIBLES 
var_dep = StringVar()
var_name = StringVar()
var_post = StringVar()
var_email = StringVar()
var_address = StringVar()
var_dob = StringVar()
var_idproofcomb = StringVar()
var_idproof = StringVar()
var_gender = StringVar()
var_phone = StringVar()
var_country = StringVar()
var_salary = StringVar()
var_joining_year = StringVar()



# Logo img
img_logo = Image.open("logo.jpg")
img_logo = img_logo.resize((50,50),Image.ANTIALIAS)
photo_logo = ImageTk.PhotoImage(img_logo)
logo = Label(root,image=photo_logo)
logo.place(x=280,y=5,width=50,height=50)

# Frame
img_frame = Frame(root,bd=2,relief=RIDGE,bg="white")
img_frame.place(x=0,y=65,width=1530,height=170)

#Image 1
img1 = Image.open("img1.jpg")
img1 = img1.resize((550,160),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img1)
img_1 = Label(img_frame,image=photo)
img_1.place(x=0,y=0,width=550,height=160)

#Image 2
img2 = Image.open("img2.jpg")
img2 = img2.resize((550,160),Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(img2)
img_2 = Label(img_frame,image=photo2)
img_2.place(x=550,y=0,width=550,height=160)

#Image 3
img3 = Image.open("img3.jpg")
img3 = img3.resize((550,160),Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(img3)
img_3 = Label(img_frame,image=photo3)
img_3.place(x=1000,y=0,width=550,height=160)

#Main Frame 
main_frame = Frame(root,bd=2,relief=RIDGE,bg="white")
main_frame.place(x=10,y=235,width=1500,height=600)

#Upper Frame
Upper_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",fg="red",text="Employee Information ",font="lato 12 bold")
Upper_frame.place(x=10,y=10,width=1480,height=280)

#Department
lbl_dep = Label(Upper_frame,text="Department:",font="arial 11 bold",bg="white")
lbl_dep.grid(row=0,column=0,padx=4,sticky=W)

combo_dep = ttk.Combobox(Upper_frame,textvariable=var_dep,font="arial 12 bold",width=17,state=READABLE)
combo_dep['value'] = ('Select Department','HR','Mananger','Software Enginner','CA','Worker') 
combo_dep.current(0)
combo_dep.grid(row=0,column=1,padx=4,pady=10,sticky=W)

#Post
lbl_post = Label(Upper_frame,text="Post:",font="arial 11 bold",bg="white")
lbl_post.grid(row=1,column=0,padx=4,pady=10,sticky=W)

txt_post = ttk.Entry(Upper_frame,textvariable=var_post,width=22,font="arial 11 bold")
txt_post.grid(row=1,column=1,padx=4,pady=10)

#Address
lbl_address = Label(Upper_frame,text="Address:",font="arial 11 bold",bg="white")
lbl_address.grid(row=2,column=0,padx=4,pady=10,sticky=W)

txt_address = ttk.Entry(Upper_frame,textvariable=var_address,width=22,font="arial 11 bold")
txt_address.grid(row=2,column=1,padx=4,pady=10)

#DOB
lbl_DOB = Label(Upper_frame,text="DOB:",font="arial 11 bold",bg="white")
lbl_DOB.grid(row=3,column=0,padx=4,pady=10,sticky=W)

txt_DOB = ttk.Entry(Upper_frame,textvariable=var_dob,width=22,font="arial 11 bold")
txt_DOB.grid(row=3,column=1,padx=4,pady=10)

#ID Proof
lbl_id = Label(Upper_frame,text="Select ID:",font="arial 11 bold",bg="white")
lbl_id.grid(row=4,column=0,padx=4,sticky=W)

combo_id = ttk.Combobox(Upper_frame,textvariable=var_idproofcomb,font="arial 11 bold",width=17,state=READABLE)
combo_id['value'] = ('Select id','PAN CARD','ADHAR CARD','VOTER ID') 
combo_id.current(0)
combo_id.grid(row=4,column=0,padx=4,pady=10,sticky=W)

txt_proof = ttk.Entry(Upper_frame,textvariable=var_idproof,width=22,font="arial 11 bold")
txt_proof.grid(row=4,column=1,padx=4,pady=10)

#Name
lbl_name = Label(Upper_frame,text="Name:",font="arial 11 bold",bg="white")
lbl_name.grid(row=0,column=2,padx=4,pady=10,sticky=W)

txt_name = ttk.Entry(Upper_frame,textvariable=var_name,width=22,font="arial 11 bold")
txt_name.grid(row=0,column=3,padx=4,pady=10)

#Email
lbl_email = Label(Upper_frame,text="Email:",font="arial 11 bold",bg="white")
lbl_email.grid(row=1,column=2,padx=4,pady=10,sticky=W)

txt_email = ttk.Entry(Upper_frame,textvariable=var_email,width=22,font="arial 11 bold")
txt_email.grid(row=1,column=3,padx=4,pady=10)

#Phone
lbl_phone = Label(Upper_frame,text="Phone No:",font="arial 11 bold",bg="white")
lbl_phone.grid(row=2,column=2,padx=4,pady=10,sticky=W)

txt_phone = ttk.Entry(Upper_frame,textvariable=var_phone,width=22,font="arial 11 bold")
txt_phone.grid(row=2,column=3,padx=4,pady=10)

#Gender
lbl_gen = Label(Upper_frame,text="Gender:",font="arial 11 bold",bg="white")
lbl_gen.grid(row=3,column=2,padx=4,sticky=W)

combo_gen = ttk.Combobox(Upper_frame,textvariable=var_gender,font="arial 12 bold",width=17,state=READABLE)
combo_gen['value'] = ('Select Gender','Male','Female') 
combo_gen.current(0)
combo_gen.grid(row=3,column=3,padx=4,pady=10,sticky=W)

#Country
lbl_con = Label(Upper_frame,text="Country:",font="arial 11 bold",bg="white")
lbl_con.grid(row=0,column=4,padx=4,pady=10,sticky=W)

txt_con = ttk.Entry(Upper_frame,textvariable=var_country,width=22,font="arial 11 bold")
txt_con.grid(row=0,column=5,padx=4,pady=10)

#Salary
lbl_salary = Label(Upper_frame,text="Salary:",font="arial 11 bold",bg="white")
lbl_salary.grid(row=1,column=4,padx=4,pady=10,sticky=W)

txt_salary = ttk.Entry(Upper_frame,textvariable=var_salary,width=22,font="arial 11 bold")
txt_salary.grid(row=1,column=5,padx=4,pady=10)

#Join
lbl_join = Label(Upper_frame,text="Joining Year:",font="arial 11 bold",bg="white")
lbl_join.grid(row=2,column=4,padx=4,pady=10,sticky=W)

txt_join = ttk.Entry(Upper_frame,textvariable=var_joining_year,width=22,font="arial 11 bold")
txt_join.grid(row=2,column=5,padx=4,pady=10)

#img
emp = Image.open("emp.jpg")
emp = emp.resize((250,250),Image.ANTIALIAS)
emp_img = ImageTk.PhotoImage(emp)

emp_1 = Label(Upper_frame,image=emp_img)
emp_1.place(x=1000,y=0,width=250,height=250)

#Button Frame

button_frame = Frame(Upper_frame,bd=2,relief=RIDGE,bg="white")
button_frame.place(x=1290,y=10,width=170,height=212)

btn_add = Button(button_frame,text="Save",font="arial 15 bold",width=13,bg="blue")
btn_add.grid(row=0,column=0,padx=1,pady=5)

btn_delete = Button(button_frame,text="Delete",font="arial 15 bold",width=13,bg="blue")
btn_delete.grid(row=1,column=0,padx=1,pady=5)
 

btn_update = Button(button_frame,text="Update",font="arial 15 bold",width=13,bg="blue")
btn_update.grid(row=2,column=0,padx=1,pady=5)

btn_clear = Button(button_frame,text="Clear",font="arial 15 bold",width=13,bg="blue")
btn_clear.grid(row=3,column=0,padx=1,pady=5)

#Lower Frame
Lower_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",fg="red",text="Employee Information Table",font="lato 12 bold")
Lower_frame.place(x=10,y=295,width=1480,height=280)

#Search Frame

Search_frame = LabelFrame(Lower_frame,bd=2,relief=RIDGE,bg="white",fg="red",text="Search Employee Information ",font="lato 12 bold")
Search_frame.place(x=0,y=0,width=1470,height=60)

search_by = Button(Search_frame,bd=2,relief=RIDGE,bg="red",fg="white",text="Search By",font="lato 12 bold")
search_by.grid(row=0,column=0,sticky=W,padx=5,pady=5)

com_txt_search = ttk.Combobox(Search_frame,state=READABLE,font="arial 12 bold",width=18)
com_txt_search['value'] = ("Select Option","Phone No","Id Proof")
com_txt_search.current(0)
com_txt_search.grid(row=0,column=1,sticky=W,padx=5,pady=5)

txt_search = ttk.Entry(Search_frame,width=22,font="arial 11 bold")
txt_search.grid(row=0,column=2,padx=5)

btn_search = Button(Search_frame,text="Search",width=11,font="arial 11 bold",bg="blue")
btn_search.grid(row=0,column=3,padx=5)

btn_Showall = Button(Search_frame,text="Show All",font= "arial 11 bold",width=11,bg="blue")
btn_Showall.grid(row=0,column=4,padx=5)


txt = Label(Search_frame,text="Employee Mangement",font="arial 20 bold",fg="red")
txt.place(x=780,y=0,width=600,height=30)


#################### EMPLOYEE TABLE #########################

table_frame = Frame(Lower_frame,bd=3,relief=RIDGE,bg="white")
table_frame.place(x=0,y=60,width=1470,height=170)

scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

emp_table = ttk.Treeview(table_frame,columns=('dep','name','post','email','address','dob','idproofcomb','idproof','gender','phone','country','salary','join year'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=emp_table.xview)
scroll_y.config(command=emp_table.yview)

emp_table.heading('dep',text='Department')
emp_table.heading('name',text='Name')
emp_table.heading('post',text='Post')
emp_table.heading('email',text='Email')
emp_table.heading('address',text='Address')
emp_table.heading('dob',text='DOB')
emp_table.heading('idproofcomb',text='Id Type')
emp_table.heading('idproof',text='Id Proof')
emp_table.heading('gender',text='Gender')
emp_table.heading('phone',text='Phone no')
emp_table.heading('country',text='Country')
emp_table.heading('salary',text='Salary')
emp_table.heading('join year',text='Joining Year')

emp_table['show'] = 'headings'
emp_table.column('dep',width=100)
emp_table.pack(fill=BOTH,expand=1)

################ FUNTION  DECLARATION #################


def save_data():
    if var_dep.get() =="" or var_email.get() =="":
        messagebox.showerror('Error','All Fields are required')
    else:
        try:
            conn = mysql.connector.connect(host='localhost',username='root',password='vicky123',database='first_project')
            my_cursor = conn.cursor()
            my_cursor.execute('insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                  var_dep.get(),
                                                                                                  var_name.get(),
                                                                                                  var_post.get(),
                                                                                                  var_email.get(),
                                                                                                  var_address.get(),
                                                                                                  var_dob.get(),
                                                                                                  var_idproofcomb.get(),
                                                                                                  var_idproof.get(),
                                                                                                  var_gender.get(),
                                                                                                  var_phone.get(),
                                                                                                  var_country.get(),
                                                                                                  var_salary.get(),
                                                                                                  var_joining_year.get()
                                                                                                   ))
                                                                                                               
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Employee has been added! ' ,parent = root)

        except Exception as es:
            messagebox.showerror('Error',f'Due to:{str(es)}',parent = root)




root.mainloop()
