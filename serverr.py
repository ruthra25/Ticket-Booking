import socket
import linecache
import os
from threading import Thread
TCP_IP = '192.168.94.90'
TCP_PORT = 9002
BUFFER_SIZE = 1024
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))

threads = []
class ClientThread(Thread):
    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        # print ("New thread started for "+ip+":"+str(port))
    def run(self):   
        l1=[]   
        listt=[]    
        try:     
            filename=self.sock.recv(1024)
            mn="hii"
            self.sock.send(str(mn).encode('utf-8'))
            pw=self.sock.recv(1024)
            mn2="hello"
            self.sock.send(str(mn2).encode('utf-8'))
            em=self.sock.recv(1024)
            mn3="hihello"
            self.sock.send(str(mn3).encode('utf-8'))

            l=[]
            l.append(filename.decode())
            l.append(pw.decode())
            l.append(em.decode())

            var=l[2]

            with open(var, 'w') as fp:
                print('created file: ', var)
                for i in l:
                    fp.write("%s\n "%i)
        
            del l
            l1.append(var)
            
            filename1=self.sock.recv(1024)
            mn4="hii"
            self.sock.send(str(mn).encode('utf-8'))
            pw1=self.sock.recv(1024)
            mn5="hello"
            self.sock.send(str(mn2).encode('utf-8'))
            em1=self.sock.recv(1024)
            mn6="hihello"
            self.sock.send(str(mn3).encode('utf-8'))

            fp=em1.decode()
            print(fp)

            if fp in l1:
                file=open(fp,"r")
                x = file.read()
                username, password,email,d = list(x.split('\n'))

                if (password == pw1.decode() and username==filename1.decode()):
                    msg="LOGIN SUCCESSFUL"
                    self.sock.send(str(msg).encode('utf8'))
                    bn=self.sock.recv(1024)
                    print(bn.decode())
                    file=open("seats.txt",'r')
                    l=file.read()
                    array=[]
                    array=list(l.split())
                    file.close()

                    array=str(array)
                    array=array.encode()
                    self.sock.send(array)
                
                    array=array.decode('utf-8')
                    array=eval(array)

                    avail=40
                    k=self.sock.recv(1024) #no of seats 5
                    k=k.decode()
                    seat=int(k) #5
                    seat1=seat
                    mn7="hi"
                    self.sock.send(str(mn7).encode('utf-8'))
                    if(seat<avail): #5<40
                        avail=avail-seat #40-5=35
                        ls=[]
                        while(seat>0): #5<0

                            seatnum=self.sock.recv(1024) #14 12 15 18 17
                            seatnum=seatnum.decode() 
                            seatnum=int(seatnum) 

                            seatno=seatnum-1

                            for i in range(len(array)):
                                if seatno==i:
                                    array[i]='-Booked-'
                                    listt.append(seatno)

                            with open("seats.txt", 'w') as fp1:
                                for i in array:
                                    fp1.write("%s\n "%i)
                            fp1.close()

                            seatnum=str(seatnum)
                            ls.append(seatnum)
                            seat-=1
                                
                        #print(array)

                        array=str(array)
                        array=array.encode()
                        self.sock.send(array)

                        array=array.decode('utf-8')
                        array=eval(array)

                        if fp in l1:
                            file=open(fp,"r")
                            x = file.read()
                            l2=str(x)
                            a2=[]
                            a2=list(l2.split())
                            seat1=str(seat1)
                            a2.append(seat1)
                            a2.append(ls)
                            
                            a3=str(a2)
                            a3=a3.encode()
                            self.sock.send(a3)

                        ch=self.sock.recv(1024) 
                        mn8="hi2"
                        self.sock.send(str(mn8).encode('utf-8'))
                        ch=ch.decode()  
                        if(ch=='Y' or ch=='y'):
                            s=self.sock.recv(1024) #14 12 15 18 17
                            s=s.decode()
                            mn9="hello2"
                            self.sock.send(str(mn9).encode('utf-8'))
                            s=int(s)   
                            print(s)
                        
                            data5=self.sock.recv(1024)
                            data5=data5.decode('utf-8')
                            data5=eval(data5)
                            print(data5)

                            while(s>0):
                                for i in range (len(data5)):
                                    for j in range(len(array)):
                                        if data5[i]==j:
                                            g='.Empty'
                                            h=str(j) + g
                                            array[j-1]=h
                                s-=1

                            with open("seats.txt", 'w') as fp3:
                                for i in array:
                                    fp3.write("%s\n "%i)
                            fp3.close()
                                            
                            array=str(array)
                            array=array.encode()
                            self.sock.send(array)
                else:
                    msg="\nLOGIN UNSUCCESSFUL\n"
                    self.sock.send(str(msg).encode('utf8'))

            else:
                msg1="\nLOGIN UNSUCCESSFUL\n"
                self.sock.send(str(msg1).encode('utf8'))
            
        except FileNotFoundError as e:
            print("\nInvalid Login\n")
while True:
    os.system("cls")
    tcpsock.listen(5)
    print("Waiting for incoming client connections...") 
    (conn, (ip,port)) = tcpsock.accept()
    print ('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)
    
for t in threads:
    t.join()