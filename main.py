from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import ttk
import os
import connection

window = Tk()
window.title('Doggo House')
window.iconbitmap('pet.ico')

frame= Frame(window,bg='#ff7675',width=800,height=450)
frame.pack(fill=BOTH,expand=YES)

l2= Label(frame,text='Welcome to',fg='white',font=('Comic Sans MS',35,'bold italic'),bg='#ff7675')
l2.place(x=250,y=100)

l4= Label(frame,text='The Doggo House',fg='white',font=('Comic Sans MS',35,'bold italic'),bg='#ff7675')
l4.place(x=200,y=160)
  
pic1=Image.open('ba.png').resize((300,200))
photo=ImageTk.PhotoImage(pic1)
l1=Label(frame,image=photo,bg='#ff7675')
l1.place(x=455,y=260)

pic2=Image.open('cutty.png').resize((200,200))
photo1=ImageTk.PhotoImage(pic2)
l3=Label(frame,image=photo1,bg='#ff7675')
l3.place(x=5,y=25)

v=IntVar()

def first_frame():
    global frame
    frame.destroy()

    frame= Frame(window,bg='#ff7675',width=800,height=450)
    frame.pack(fill=BOTH,expand=YES)

    img=Image.open('cutty.png')
    render=ImageTk.PhotoImage(img)
    ddimg=Label(frame,width=250,height=250,image=render,bg='#ff7675')
    ddimg.image=render
    ddimg.place(x=490,y=270)

    img1=Image.open('paw1.png')
    render=ImageTk.PhotoImage(img1)
    dddimg=Label(frame,width=700,height=180,image=render,bg='#ff7675')
    dddimg.image=render
    dddimg.place(x=-60,y=12)
   

    heading=Label(frame,text='All Dogs in Doggo House',fg='white',font=('Comic Sans MS',33,'bold underline'),bg='#ff7675')
    heading.place(x=140,y=100)

    see_all_details = Radiobutton(frame,text='See All Dogs',variable=v,value=1,fg='white',font=('Comic Sans MS',22,'bold'),
    bg='#ff7675',activebackground='#ff7675',selectcolor='grey',activeforeground="white")
    see_all_details.place(x=220,y=180)

    # see_all_details_by_species = Radiobutton(frame,text='See Dogs By Species',variable=v,value=2,fg='white',font=('Comic Sans MS',22,'bold'),
    # bg='#ff7675',selectcolor='grey',activeforeground="white",activebackground='#ff7675')
    # see_all_details_by_species.place(x=220,y=230)

    add = Radiobutton(frame,text='Add Dogs',variable=v,value=3,fg='white',font=('Comic Sans MS',22,'bold'),
    bg='#ff7675',selectcolor='grey',activeforeground="white",activebackground='#ff7675')
    add.place(x=220,y=230)

    customer = Radiobutton(frame,text='Customer',variable=v,value=4,fg='white',font=('Comic Sans MS',22,'bold'),
    bg='#ff7675',selectcolor='grey',activeforeground="white",activebackground='#ff7675')
    customer.place(x=220,y=280)

    b1= Button(frame,text='Next',fg='black',font=('Comic Sans MS',22,'bold'),bd=0.5,padx=4,pady=2,bg='white',command=sel)
    b1.place(x=220,y=350)

def sel():
    print(v.get())
    if v.get() ==1:
        select_dog()
    if v.get() ==3:
        add()
    if v.get() ==4:
        customer1()

def buy(id,name2,breed2,price2):
    vars=IntVar()
    global frame
    frame.destroy()


    gender_values={
        1:'Male',
        2:'Female'
    }

    def next_func():
        global frame
        dog_name=name2
        dog_breed=breed2
        dog_price=price2
        cust_name=Cname_e1.get()
        cust_gender=gender_values[vars.get()]
        cust_mob=Cphone_e1.get()
        cust_address=Caddres_e1.get()
        connection.insert_customer(dog_name,dog_breed,dog_price,cust_name,cust_gender,cust_mob,cust_address)
        messagebox.showinfo('Checkout','Thanks for Buying')
        connection.remove_dog(id)
        select_dog()

    


    frame= Frame(window,bg='#ff7675',width=800,height=450)
    frame.pack(fill=BOTH,expand=YES)

    heading=Label(frame,text='Customer Details',fg='white',font=('Arial Unicode MS',20,'bold underline'),bg='#ff7675')
    heading.place(x=300,y=10)

    name=Label(frame,text='Name :'+           name2,fg='white',font=('Comic Sans MS',15),bg='#ff7675')
    name.place(x=300,y=60) 

    id1=Label(frame,text='ID :'+              str(id),fg='white',font=('Comic Sans MS',15),bg='#ff7675')
    id1.place(x=300,y=100) 

    gender=Label(frame,text='Breed :'+          breed2,fg='white',font=('Comic Sans MS',15),bg='#ff7675')
    gender.place(x=300,y=140) 

    Cname=Label(frame,text='Customer_Name :',fg='white',font=('Comic Sans MS',15),bg='#ff7675')
    Cname.place(x=170,y=200)
    Cname_e1=Entry(frame,width=20,fg='white',font=('comic sans ms',15),bd=1,bg='#ff7675')
    Cname_e1.place(x=350,y=200)

    Cgender=Label(frame,text='Customer_Gender:',fg='white',font=('Comic Sans MS',15,'italic'),bg='#ff7675')
    Cgender.place(x=160,y=250)
    Cgender_e1=Radiobutton(frame,text='Male',variable=vars,value=1,fg='white',font=('comic sans ms',15)
    ,bg='#ff7675',selectcolor='grey')
    Cgender_e1.place(x=350,y=253)
    Cgender_e2=Radiobutton(frame,text='Female',variable=vars,value=2,fg='white',font=('comic sans ms',15),
    bg='#ff7675',selectcolor='grey')
    Cgender_e2.place(x=450,y=253)

    Cphone=Label(frame,text='Customer Mobile No. :',fg='white',font=('Comic Sans MS',15,'italic'),bg='#ff7675')
    Cphone.place(x=120,y=300)
    Cphone_e1=Entry(frame,width=30,fg='black',font=('comic sans ms',12),bd=1,bg='#ff7675')
    Cphone_e1.place(x=350,y=300)

    Caddres=Label(frame,text='Customer_Address :',fg='white',font=('Comic Sans MS',15),bg='#ff7675')
    Caddres.place(x=130,y=360)
    Caddres_e1=Entry(frame,width=30,fg='white',font=('comic sans ms',15),bd=1,bg='#ff7675')
    Caddres_e1.place(x=350,y=360)

    price=Label(frame,text='Price :'+          price2,fg='white',font=('Comic Sans MS',15),bg='#ff7675')
    price.place(x=300,y=400) 

    cod=Label(frame,text='Payment Mode :'+'COD',fg='white',font=('Comic Sans MS',15),bg='#ff7675')
    cod.place(x=130,y=430)   

    b2=Button(frame,text='Next',bg='white',font=('montserrat semibold','12'),bd=0,padx=14,command=next_func)
    b2.place(x=480,y=450)

    b3=Button(frame,text='Back',bg='white',font=('montserrat semibold','12'),bd=0,padx=14,command=select_dog)
    b3.place(x=590,y=450)

def select_dog():
    global frame
    frame.destroy()

    record=connection.select_from_db()
    global num
    num=0

  
    
    def convert_to_image(data,filename):
        with open(filename,'wb') as file:
            binary=file.write(data)
   
    def select(m):
        global frame
        frame.destroy()
        print(m)
        if m<len(record) and m>=0:
           i=record[m]
           frame= Frame(window,bg='#ff7675',width=800,height=450)
           frame.pack(fill=BOTH,expand=YES)
     
           name=Label(frame,text='Name :'+i[1],fg='white',font=('Comic Sans MS',15,'bold italic'),bg='#ff7675')
           name.place(x=400,y=40) 

    
           breed=Label(frame,text='Breed :'+i[3],fg='white',font=('Comic Sans MS',15,'bold italic'),bg='#ff7675')
           breed.place(x=400,y=90)
        
           name_img=os.path.dirname(__file__)+"/Images/"+i[1]+str(i[0])+".jpg"
           convert_to_image(i[7],name_img)
         
           img=Image.open(name_img)
           render=ImageTk.PhotoImage(img)
           dimg=Label(frame,width=250,height=150,image=render,bg='#ff7675')
           dimg.image=render
           dimg.place(x=100,y=100)

           gender=Label(frame,text='Gender :'+i[2],fg='white',font=('Comic Sans MS',15,'bold italic'),bg='#ff7675')
           gender.place(x=390,y=140)

           about=Label(frame,text='About :',fg='white',font=('Comic Sans MS',15,'bold italic'),bg='#ff7675')
           about.place(x=400,y=190)
           about=Text(frame,width=24,height=5,bd=.1,fg='white',font=('Comic Sans MS',15)
           ,bg='#ff7675',wrap=WORD)
           about.place(x=490,y=190)
           about.insert(END,i[4])
           about.config(state=DISABLED)
    

           price=Label(frame,text='Price :'+i[5],fg='white',font=('Comic Sans MS',15,'bold italic'),bg='#ff7675')
           price.place(x=400,y=300)

           meet=Text(frame,width=20,height=3,bd=0,fg='white',font=('Comic Sans MS',10,'bold italic'),bg='#ff7675',wrap=WORD)
           meet.place(x=100,y=255)
           meet.insert(END,'Age'+':'+i[6])
           meet.config(state=DISABLED)

           b7=Button(frame,text='Previous',bg='white',font=('montserrat semibold','12'),bd=0,padx=14,command= lambda:select(m-1))
           b7.place(x=250,y=380)  

           b6=Button(frame,text='Next',bg='white',font=('montserrat semibold','12'),bd=0,padx=14,command= lambda:select(m+1))
           b6.place(x=360,y=380)
        
           b5=Button(frame,text='Back',bg='white',font=('montserrat semibold','12'),bd=0,padx=14,command=first_frame)
           b5.place(x=440,y=380)


           b4=Button(frame,text='Buy',bg='white',font=('montserrat semibold','12'),bd=0,padx=14,command=lambda:buy(i[0],i[1],i[3],i[5]))
           b4.place(x=530,y=380)

        elif m>=len(record):
            select(0)
        else:
            select(len(record)-1)
    select(num)

def add():
    global frame
    frame.destroy()
     
    var=IntVar()

    def Browose():
        global filename
        import os
        filename = filedialog.askopenfilename(initialdir=os.path.dirname('__file__'),title='select_file',
        filetype=(('jpeg files','*jpg'),('jpg files','*jpeg'),('png files','*png')))
        print(filename)
    
    gender_dict={
        1:'Male',
        2:'Female'
    }

    def insert():
        name1 = name_e1.get()
        image = filename
        gender1 = gender_dict[var.get()]
        breed1=breed_e1.get()
        about1 = about_e1.get(1.0,'end-1c')
        price1 = price_e1.get()
        meet1 = meet_e1.get(1.0,'end-1c')
        connection.insert_db(name1,gender1,breed1,about1,price1,meet1,image)
        print(name1,image,gender1,about1,price1,meet1)

        messagebox.showinfo('success','Successfully Added')
        name_e1.delete(0,END)
        about_e1.delete('1.0',END)
        meet_e1.delete('1.0',END)
        price_e1.delete(0,END)
        breed_e1.delete(0,END)
        var.set(None)


    frame= Frame(window,bg='#ff7675',width=800,height=450)
    frame.pack(fill=BOTH,expand=YES)


    heading=Label(frame,text='Add Dog',fg='white',font=('Arial Unicode MS',20,'bold underline'),bg='#ff7675')
    heading.place(x=300,y=10)

    name=Label(frame,text='Name :',fg='black',font=('Comic Sans MS',15,'italic'),bg='#ff7675')
    name.place(x=240,y=60)
    name_e1=Entry(frame,width=20,fg='black',font=('comic sans ms',12),bd=1,bg='#ff7675')
    name_e1.place(x=330,y=70)

    photo=Label(frame,text='Add Image :',fg='black',font=('Comic Sans MS',15,'italic'),bg='#ff7675')
    photo.place(x=200,y=110)
    photo_e1=Button(frame,text='Browse',fg='black',font=('comic sans ms',15,'italic underline'),bg='#ff7675',
    bd=0,command=Browose)
    photo_e1.place(x=330,y=100)
     

    
    breed=Label(frame,text='breed :',fg='black',font=('Comic Sans MS',15,'italic'),bg='#ff7675')
    breed.place(x=230,y=150)
    breed_e1=Entry(frame,width=20,fg='black',font=('comic sans ms',12),bd=1,bg='#ff7675')
    breed_e1.place(x=330,y=160)

    gender=Label(frame,text='Gender:',fg='black',font=('Comic Sans MS',15,'italic'),bg='#ff7675')
    gender.place(x=220,y=190)
    gender_e1=Radiobutton(frame,text='Male',variable=var,value=1,fg='white',font=('comic sans ms',15)
    ,bg='#ff7675',selectcolor='grey')
    gender_e1.place(x=330,y=193)
    gender_e2=Radiobutton(frame,text='Female',variable=var,value=2,fg='white',font=('comic sans ms',15),
    bg='#ff7675',selectcolor='grey')
    gender_e2.place(x=430,y=193)

    price=Label(frame,text='Price :',fg='black',font=('Comic Sans MS',15,'italic'),bg='#ff7675')
    price.place(x=230,y=250)
    price_e1=Entry(frame,width=20,fg='black',font=('comic sans ms',12),bd=1,bg='#ff7675')
    price_e1.place(x=330,y=260)

    about=Label(frame,text='About:',fg='black',font=('Comic Sans MS',15,'italic'),bg='#ff7675')
    about.place(x=230,y=310) 
    about_e1=Text(frame,width=29,height=4,bd=1,wrap=WORD,font=('comic sans MS',10,'bold italic'),bg='#ff7676')
    about_e1.place(x=330,y=310)

    meet=Label(frame,text='Age:',fg='black',font=('Comic Sans MS',15,'italic'),bg='#ff7675')
    meet.place(x=230,y=400)
    meet_e1=Text(frame,width=20,height=2,bd=1,wrap=WORD,font=('comic sans MS',10,'bold italic'),bg='#ff7676')
    meet_e1.place(x=330,y=400)

    b2=Button(frame,text='Next',bg='white',font=('montserrat semibold','12'),bd=0,padx=14,command=insert)
    b2.place(x=360,y=450)

    b3=Button(frame,text='Back',bg='white',font=('montserrat semibold','12'),bd=0,padx=14,command=first_frame)
    b3.place(x=440,y=450)

def customer1():
    global frame
    frame.destroy()
    frame= Frame(window,bg='#ff7675',width=800,height=450)
    frame.pack(fill=BOTH,expand=YES)
    treev =ttk.Treeview(frame,selectmode='browse')
    treev.pack(side='left',expand=YES,fill=BOTH)


    verscrlbar = ttk.Scrollbar(frame,
                            orient='vertical',
                            command=treev.yview)

    verscrlbar.pack(side='right',fill='y')

    treev.configure(yscrollcommand=verscrlbar.set)

    #defining number of colums
    treev["columns"]=("1","2","3","4","5","6","7")
     
    #defining number of colums
    treev['show']='headings'

    treev.column("1",width=30,anchor='c')
    treev.column("2",width=30,anchor='c')
    treev.column("3",width=30,anchor='c')
    treev.column("4",width=30,anchor='c')
    treev.column("5",width=30,anchor='c')
    treev.column("6",width=30,anchor='c')
    treev.column("7",width=30,anchor='c')

    treev.heading('1',text='Dog_Name')
    treev.heading('2',text='Dog_Breed')
    treev.heading('3',text='Dog_Price')
    treev.heading('4',text='Customer_Name')
    treev.heading('5',text='Customer_Gender')
    treev.heading('6',text='Custome_Mob_No')
    treev.heading('7',text='Custome_Addres')
    
    record=connection.customer_details()
    for i in record:
       treev.insert("",'end',
                    values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

frame.after(10000,first_frame)
window.geometry('800x500')
window.resizable(False,False)
window.mainloop()