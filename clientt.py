import socket
import maskpass
import os
import time
from itertools import islice
import tkinter
from tkinter import *
from tkinter import messagebox
TCP_IP = '192.168.94.154'
TCP_PORT    = 9002
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
username_login=None
password_login=None
email_login=None
tic_login=None
seat_login=None
sn1=None
window = tkinter.Tk()
window.title(" Bus Reservation !! ")
window.geometry('440x440')
window.configure(bg='#333333')
frame = tkinter.Frame(bg='#333333')
ls=[]
os.system("cls")
# print("\n--------------------------------------------------")
# print("            (: PURPLE BUS .COM :)              ")
# print("       BOOK YOUR SEAT AT YOUR FINGER TIP       ")
# print("--------------------------------------------------")

# print("\n             * REGISTER YOURSELF *         \n")


def no():
    window6 = tkinter.Tk()
    window6.title(" Exit !! ")
    window6.geometry('940x440')
    window6.configure(bg='#333333')
    frame6 = tkinter.Frame(window6,bg='#333333')
    avai_label    = tkinter.Label(frame6, text="Have a happy journey ...!", bg='#333333', fg="#FF3399", font=("Arial", 30))
    avai_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    avai_label1    = tkinter.Label(frame6, text="****  Thank You , Visit Again ***", bg='#333333', fg="#FF3399", font=("Arial", 30))
    avai_label1.grid(row=1, column=0, columnspan=2, sticky="news", pady=40)
    frame6.pack()
    window6.mainloop()

def yes():
    global sn1
    ch='Y'
    sn1=int(sn1)
    s.send(str(ch).encode('utf8')) 
    mn8=s.recv(1024)
    s.send(str(sn1).encode('utf8')) 
    mn9=s.recv(1024)
    print(ls)

    while(sn1>0):
        
        ls3=str(ls)
        ls3=ls3.encode()
        s.send(ls3)
        sn1-=1

    data5=s.recv(4096)
    data5=data5.decode('utf-8')
    data5=eval(data5)
    data6 = iter(data5)
  
    window7 = tkinter.Tk()
    window7.title(" Cancellation !! ")
    window7.geometry('1240x440')
    window7.configure(bg='#333333')
    frame7 = tkinter.Frame(window7,bg='#333333')
    avai_label    = tkinter.Label(frame7, text="Cancellation Successful", bg='#333333', fg="#FF3399", font=("Arial", 30))
    avai_label.grid(row=0, column=1, columnspan=3, sticky="news", pady=40)
    length_to_split1 = [5,5,5,5,5,5,5,5]
    Output1 = [list(islice(data6, elem))
         for elem in length_to_split1]
    t_rows1=len(Output1)
    t_columns1=len(Output1[0])

    for i in range(t_rows1):
        for j in range(t_columns1):
            e1 = tkinter.Entry(frame7, width=20, fg='blue',
                               font=('Arial',16,'bold'))

            e1.grid(row=i+2, column=j)
            e1.insert(END, Output1[i][j])

    avai_label1    = tkinter.Label(frame7, text="****  Thank You , Visit Again ***", bg='#333333', fg="#FF3399", font=("Arial", 30))
    avai_label1.grid(row=10, column=1, columnspan=3, sticky="news", pady=40)

    frame7.pack()
    window7.mainloop()

def book3():
    global sn1
    data2=s.recv(4096)
    data2=data2.decode('utf-8')
    data2=eval(data2)
    info=[]
    name=data2[0]
    emailid=data2[2]
    sn=data2[3]
    sn=int(sn)
    sn1=sn
    cost=sn*250
    ls=[]
    ls=data2[4]
    ls1=[eval(i) for i in ls]
    na="Name:"
    em="Email:"
    n_t="No of Tickets Booked:"
    c="Fare:"
    info.append(na)
    info.append(name)
    info.append(em)
    info.append(emailid)
    info.append(n_t)
    info.append(sn)
    info.append("Booked Seats")
    info.append(ls1)
    info.append(c)
    info.append(cost)
    data3 = iter(info)
    length_to_split1 = [2,2,2,2,2]
    Output1 = [list(islice(data3, elem))
         for elem in length_to_split1]
    window5 = tkinter.Tk()
    window5.title(" Invoice !! ")
    window5.geometry('740x440')
    window5.configure(bg='#333333')
    frame5 = tkinter.Frame(window5,bg='#333333')
    avai_label    = tkinter.Label(frame5, text="INVOICE", bg='#333333', fg="#FF3399", font=("Arial", 30))
    avai_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

    t_rows1=len(Output1)
    t_columns1=len(Output1[0])

    for i in range(t_rows1):
        for j in range(t_columns1):
            e1 = tkinter.Entry(frame5, width=20, fg='blue',
                               font=('Arial',16,'bold'))

            e1.grid(row=i+1, column=j)
            e1.insert(END, Output1[i][j])

    cancel_label = tkinter.Label(frame5, text="Cancel Booking Y/N?", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    yes_button = tkinter.Button(frame5, text="Yes", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=yes)
    no_button = tkinter.Button(frame5, text="No", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=no)
    cancel_label.grid(row=6, column=0)
    yes_button.grid(row=6, column=1, pady=10)
    no_button.grid(row=6, column=2, pady=10)
    frame5.pack()
    window5.mainloop()
    
        



def booking():
    data=s.recv(4096)
    data=data.decode('utf-8')
    data=eval(data)
    data1 = iter(data)
    
    
    window4 = tkinter.Tk()
    window4.title(" Booking !! ")
    window4.geometry('1240x440')
    window4.configure(bg='#333333')
    frame4 = tkinter.Frame(window4,bg='#333333')
    avai_label    = tkinter.Label(frame4, text="Booking Successful", bg='#333333', fg="#FF3399", font=("Arial", 30))
    avai_label.grid(row=0, column=1, columnspan=3, sticky="news", pady=40)
    length_to_split = [5,5,5,5,5,5,5,5]
    Output = [list(islice(data1, elem))
        for elem in length_to_split]
    t_rows=len(Output)
    t_columns=len(Output[0])
   
    for i in range(t_rows):
      for j in range(t_columns):
        e = tkinter.Entry(frame4, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
        e.grid(row=i+1, column=j)
        e.insert(END, Output[i][j])

    book_button = tkinter.Button(frame4, text="View Your ticket", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=book3)
    book_button.grid(row=10, column=1, columnspan=3, pady=30)



    frame4.pack()
    window4.mainloop()


def book1():
    seat=tic_login.get()
    n_seats=int(seat)
    seat_n=seat_login.get()
    seat_numbers=seat_n.split(',')
    print(seat_numbers)
    ls1=[eval(i) for i in seat_numbers]
    print(ls1)
    s.send(str(n_seats).encode('utf-8'))
    mn7=s.recv(1024)
    for i in range(len(ls1)):
        ls.append(ls1[i])
        s.send(str(ls1[i]).encode('utf-8'))   
       
    booking()

def book():
    global tic_login
    global seat_login
    window3 = tkinter.Tk()
    window3.title(" Book The Tickets !! ")
    window3.geometry('440x440')
    window3.configure(bg='#333333')
    frame3 = tkinter.Frame(window3,bg='#333333')
    book_label    = tkinter.Label(frame3, text="Book You Tickets", bg='#333333', fg="#FF3399", font=("Arial", 30))
    tic_label = tkinter.Label(frame3, text="Number of Tickets", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    tic_login = tkinter.Entry(frame3, font=("Arial", 16))
    seat_label = tkinter.Label(frame3, text="Seat Numbers", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    seat_login = tkinter.Entry(frame3, font=("Arial", 16))
    book_button = tkinter.Button(frame3, text="Book", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=book1)

    book_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    tic_label.grid(row=1, column=0)
    tic_login.grid(row=1, column=1, pady=20)
    seat_label.grid(row=2, column=0)
    seat_login.grid(row=2, column=1, pady=20)
    book_button.grid(row=4, column=0, columnspan=2, pady=30)

    frame3.pack()
    window3.mainloop()
    


def seats():
    data=s.recv(4096)
    data=data.decode('utf-8')
    data=eval(data)
    data1 = iter(data)
    window2 = tkinter.Tk()
    window2.title(" Seats !! ")
    window2.geometry('1240x440')
    window2.configure(bg='#333333')
    frame2 = tkinter.Frame(window2,bg='#333333')
    avai_label    = tkinter.Label(frame2, text="Available Seats", bg='#333333', fg="#FF3399", font=("Arial", 30))
    avai_label.grid(row=0, column=1, columnspan=3, sticky="news", pady=40)
    print("\n\n\n")
    length_to_split = [5,5,5,5,5,5,5,5]
    Output = [list(islice(data1, elem))
        for elem in length_to_split]
    t_rows=len(Output)
    t_columns=len(Output[0])
   
    for i in range(t_rows):
      for j in range(t_columns):
        e = tkinter.Entry(frame2, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
        e.grid(row=i+1, column=j)
        e.insert(END, Output[i][j])

    book_button = tkinter.Button(frame2, text="Book now", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=book)
    book_button.grid(row=10, column=1, columnspan=3, pady=30)
    

    frame2.pack()
    window2.mainloop()

def Login():
    user=username_login.get()
    pas=password_login.get()
    em=email_login.get()
    print(user,pas,em)
    s.send(str(user).encode('utf-8'))
    d1=s.recv(1024)
    print("Received data:",d1)
    s.send(str(pas).encode('utf-8'))
    d2=s.recv(1024)
    print("Received data:",d2)
    s.send(str(em).encode('utf-8'))
    d3=s.recv(1024)
    print("Received data:",d3)
    var=s.recv(1024)#success msg
    bn="hello"
    s.send(str(bn).encode('utf-8'))
    print("\t\t\t\t\t\t",var.decode())
    if(var.decode()=="LOGIN SUCCESSFUL"):
        messagebox.showinfo("Information","Logged in Successfully")  
        seats()

def login():
    global username_login
    global password_login
    global email_login
    window1 = tkinter.Tk()
    window1.title("Login !! ")
    window1.geometry('440x440')
    window1.configure(bg='#333333')
    frame1 = tkinter.Frame(window1,bg='#333333')
    login_label    = tkinter.Label(frame1, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
    username_label = tkinter.Label(frame1, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    username_login = tkinter.Entry(frame1, font=("Arial", 16))
    password_login = tkinter.Entry(frame1, show="*", font=("Arial", 16))

    password_label = tkinter.Label(frame1, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    email_label = tkinter.Label(frame1, text="Email", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    email_login = tkinter.Entry(frame1, font=("Arial", 16))

    login_button = tkinter.Button(frame1, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Login)
    
    # Placing widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_login.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_login.grid(row=2, column=1, pady=20)
    email_label.grid(row=3, column=0)
    email_login.grid(row=3, column=1, pady=20)
    login_button.grid(row=4, column=0, columnspan=2, pady=30)

    frame1.pack()
    window1.mainloop()

def register():
        user=username_entry.get()
        pas=password_entry.get()
        em=email_entry.get()
        print(user,pas,em)
        s.send(str(user).encode('utf-8'))
        d1=s.recv(1024)
        print("Received data:",d1)
        s.send(str(pas).encode('utf-8'))
        d2=s.recv(1024)
        print("Received data:",d2)
        s.send(str(em).encode('utf-8'))
        d3=s.recv(1024)
        print("Received data:",d3)
        messagebox.showinfo("Information","Registered Successfully")  
        login()


login_label    = tkinter.Label(frame, text="Register", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))



password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))

password_label = tkinter.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
email_label = tkinter.Label(frame, text="Email", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
email_entry = tkinter.Entry(frame, font=("Arial", 16))

login_button = tkinter.Button(frame, text="Register", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=register)
    
    # Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
email_label.grid(row=3, column=0)
email_entry.grid(row=3, column=1, pady=20)
login_button.grid(row=4, column=0, columnspan=2, pady=30)

frame.pack()
window.mainloop()


s.close()