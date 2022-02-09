from Tkinter import*
import os

v=Tk()
v.geometry("500x560")
v.title("X_O")

v1=Canvas(v,width=500,height=560,background="white")

v1.create_line(166,0,166,500)
v1.create_line(332,0,332,500)
v1.create_line(0,166,500,166)
v1.create_line(0,332,500,332)
v1.create_line(0,500,500,500)

v1.pack()

lis_mach=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
a_player=[]
a_machine=[]
res=[]



def pulsacion(num):
    if num==1:
        global x1
        global x_1
        x1=v1.create_line(0,0,166,166,fill="#FF4500")
        x_1=v1.create_line(166,0,0,166,fill="#FF4500")
        lis_mach.remove(1)
        lis_mach.remove(2)
        b1.place_forget()
        b2.place_forget()
        a_player.append(1)
    elif num==2:
        global o2
        o2=v1.create_oval(0,0,166,166,outline="#00FFFF")
        lis_mach.remove(1)
        lis_mach.remove(2)
        b1.place_forget()
        b2.place_forget()
        a_machine.append(2)
    elif num==3:
        global x3
        global x_3
        x3=v1.create_line(0,166,166,332,fill="#FF4500")
        x_3=v1.create_line(166,166,0,332,fill="#FF4500")
        lis_mach.remove(3)
        lis_mach.remove(4)
        b3.place_forget()
        b4.place_forget()
        a_player.append(3)
    elif num==4:
        global o4
        o4=v1.create_oval(0,166,166,332,outline="#00FFFF")
        lis_mach.remove(3)
        lis_mach.remove(4)
        b3.place_forget()
        b4.place_forget()
        a_machine.append(4)
    elif num==5:
        global x5
        global x_5
        x5=v1.create_line(0,332,166,498,fill="#FF4500")
        x_5=v1.create_line(166,332,0,498,fill="#FF4500")
        lis_mach.remove(5)
        lis_mach.remove(6)
        b5.place_forget()
        b6.place_forget()
        a_player.append(5)
    elif num==6:
        global o6
        o6=v1.create_oval(0,332,166,498,outline="#00FFFF")
        lis_mach.remove(5)
        lis_mach.remove(6)
        b5.place_forget()
        b6.place_forget()
        a_machine.append(6)
    elif num==7:
        global x7
        global x_7
        x7=v1.create_line(166,0,332,166,fill="#FF4500")
        x_7=v1.create_line(332,0,166,166,fill="#FF4500")
        lis_mach.remove(7)
        lis_mach.remove(8)
        b7.place_forget()
        b8.place_forget()
        a_player.append(7)
    elif  num==8:
        global o8
        o8=v1.create_oval(166,0,332,166,outline="#00FFFF")
        lis_mach.remove(7)
        lis_mach.remove(8)
        b7.place_forget()
        b8.place_forget()
        a_machine.append(8)
    elif num==9:
        global x9
        global x_9
        x9=v1.create_line(166,166,332,332,fill="#FF4500")
        x_9=v1.create_line(332,166,166,332,fill="#FF4500")
        lis_mach.remove(9)
        lis_mach.remove(10)
        b9.place_forget()
        b10.place_forget()
        a_player.append(9)
    elif num==10:
        global o10
        o10=v1.create_oval(166,166,332,332,outline="#00FFFF")
        lis_mach.remove(9)
        lis_mach.remove(10)
        b9.place_forget()
        b10.place_forget()
        a_machine.append(10)
    elif num==11:
        global x11
        global x_11
        x11=v1.create_line(166,332,332,498,fill="#FF4500")
        x_11=v1.create_line(332,332,166,498,fill="#FF4500")
        lis_mach.remove(11)
        lis_mach.remove(12)
        b11.place_forget()
        b12.place_forget()
        a_player.append(11)
    elif num==12:
        global o12
        o12=v1.create_oval(166,332,332,498,outline="#00FFFF")
        lis_mach.remove(11)
        lis_mach.remove(12)
        b11.place_forget()
        b12.place_forget()
        a_machine.append(12)
    elif num==13:
        global x13
        global x_13
        x13=v1.create_line(332,0,498,166,fill="#FF4500")
        x_13=v1.create_line(498,0,332,166,fill="#FF4500")
        lis_mach.remove(13)
        lis_mach.remove(14)
        b13.place_forget()
        b14.place_forget()
        a_player.append(13)
    elif num==14:
        global o14
        o14=v1.create_oval(332,0,498,166,outline="#00FFFF")
        lis_mach.remove(13)
        lis_mach.remove(14)
        b13.place_forget()
        b14.place_forget()
        a_machine.append(14)
    elif num==15:
        global x15
        global x_15
        x15=v1.create_line(332,166,498,332,fill="#FF4500")
        x_15=v1.create_line(498,166,332,332,fill="#FF4500")
        lis_mach.remove(15)
        lis_mach.remove(16)
        b15.place_forget()
        b16.place_forget()
        a_player.append(15)
    elif num==16:
        global o16
        o16=v1.create_oval(332,166,498,332,outline="#00FFFF")
        lis_mach.remove(15)
        lis_mach.remove(16)
        b15.place_forget()
        b16.place_forget()
        a_machine.append(16)
    elif num==17:
        global x17
        global x_17
        x17=v1.create_line(332,332,498,498,fill="#FF4500")
        x_17=v1.create_line(498,332,332,498,fill="#FF4500")
        lis_mach.remove(17)
        lis_mach.remove(18)
        b17.place_forget()
        b18.place_forget()
        a_player.append(17)
    elif num==18:
        global o18
        o18=v1.create_oval(332,332,498,498,outline="#00FFFF")
        lis_mach.remove(17)
        lis_mach.remove(18)
        b17.place_forget()
        b18.place_forget()
        a_machine.append(18)

# x win fila
    if not 1 in res:
        if 1 in a_player:
            if 7 in a_player:
                if 13 in a_player:
                    res.append(1)
                    global win1
                    win1=v1.create_line(0,83,500,83,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="X-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win1)

                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
        if 3 in a_player:
            if 9 in a_player:
                if 15 in a_player:
                    res.append(1)
                    global win2
                    win2=v1.create_line(0,249,500,249,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="X-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win2)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
        if 5 in a_player:
            if 11 in a_player:
                if 17 in a_player:
                    res.append(1)
                    global win16
                    win16=v1.create_line(0,415,500,415,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="X-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win16)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
# X win Columna
    if not 1 in res:
        if 1 in a_player:
            if 3 in a_player:
                if 5 in a_player:
                    res.append(1)
                    global win3
                    win3=v1.create_line(83,0,83,500,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="X-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win3)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
        if 7 in a_player:
            if 9 in a_player:
                if 11 in a_player:
                    res.append(1)
                    global win4
                    win4=v1.create_line(249,0,249,500,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="X-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win4)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
        if 13 in a_player:
            if 15 in a_player:
                if 17 in a_player:
                    res.append(1)
                    global win5
                    win5=v1.create_line(415,0,415,500,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="X-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win5)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
# x win diagonal
    if not 1 in res:
        if 1 in a_player:
            if 9 in a_player:
                if 17 in a_player:
                    res.append(1)
                    global win6
                    win6=v1.create_line(0,0,498,498,fill="#DC143C")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="X-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win6)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
        if 13 in a_player:
            if 9 in a_player:
                if 5 in a_player:
                    res.append(1)
                    global win7
                    win7=v1.create_line(498,0,0,498,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="X-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win7)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
                                     
# O en columna 
    if not 1 in res:
        if 2 in a_machine:
            if 4 in a_machine:
                if 6 in a_machine:
                    res.append(1)
                    global win8
                    win8=v1.create_line(83,0,83,500,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="O-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win8)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
        if 8 in a_machine:
            if 10 in a_machine:
                if 12 in a_machine:
                    res.append(1)
                    global win9
                    win9=v1.create_line(249,0,249,500,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="O-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win9)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
        if 14 in a_machine:
            if 16 in a_machine:
                if 18 in a_machine:
                    res.append(1)
                    global win10
                    win10=v1.create_line(415,0,415,500,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="O-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win10)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
# O en fila
    if not 1 in res:
        if 2 in a_machine:
            if 8 in a_machine:
                if 14 in a_machine:
                    res.append(1)
                    global win11
                    win11=v1.create_line(0,83,500,83,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="O-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win11)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
        if 4 in a_machine:
            if 10 in a_machine:
                if 16 in a_machine:
                    res.append(1)
                    global win12
                    win12=v1.create_line(0,249,500,249,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="O-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win12)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
        if 6 in a_machine:
            if 12 in a_machine:
                if 18 in a_machine:
                    res.append(1)
                    global win13
                    win13=v1.create_line(0,415,500,415,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="O-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win13)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
# O en diagonal
    if not 1 in res:
        if 2 in a_machine:
            if 10 in a_machine:
                if 18 in a_machine:
                    res.append(1)
                    global win14
                    win14=v1.create_line(0,0,498,498,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="O-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win14)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)
        if 14 in a_machine:
            if 10 in a_machine:
                if 6 in a_machine:
                    res.append(1)
                    global win15
                    win15=v1.create_line(498,0,0,498,fill="red")
                    vent=Tk()
                    vent.title("X_O")
                    vent.geometry("400x250")
                    Label(vent,text="O-win",font=("arial",20),justify="center").place(x=160,y=105)
                    def pul(num):
                        vent.destroy()
                        b1.place(x=120,y=135)
                        b2.place(x=140,y=135)
                        b3.place(x=120,y=300)
                        b4.place(x=140,y=300)
                        b5.place(x=120,y=465)
                        b6.place(x=140,y=465)
                        b7.place(x=285,y=135)
                        b8.place(x=305,y=135)
                        b9.place(x=285,y=300)
                        b10.place(x=305,y=300)
                        b11.place(x=285,y=465)
                        b12.place(x=305,y=465)
                        b13.place(x=450,y=135)
                        b14.place(x=470,y=135)
                        b15.place(x=450,y=300)
                        b16.place(x=470,y=300)
                        b17.place(x=450,y=465)
                        b18.place(x=470,y=465)
                        lis_mach.clear()
                        for i in range(19):
                            lis_mach.append(i)
                        if 1 in a_player:
                            v1.delete(x1)
                            v1.delete(x_1)
                        if 2 in a_machine:
                            v1.delete(o2)
                        if 3 in a_player:
                            v1.delete(x3)
                            v1.delete(x_3)
                        if 4 in a_machine:
                            v1.delete(o4)
                        if 5 in a_player:
                            v1.delete(x5)
                            v1.delete(x_5)
                        if 6 in a_machine:
                            v1.delete(o6)
                        if 7 in a_player:
                            v1.delete(x7)
                            v1.delete(x_7)
                        if 8 in a_machine:
                            v1.delete(o8)
                        if 9 in a_player:
                            v1.delete(x9)
                            v1.delete(x_9)
                        if 10 in a_machine:
                            v1.delete(o10)
                        if 11 in a_player:
                            v1.delete(x11)
                            v1.delete(x_11)
                        if 12 in a_machine:
                            v1.delete(o12)
                        if 13 in a_player:
                            v1.delete(x13)
                            v1.delete(x_13)
                        if 14 in a_machine:
                            v1.delete(o14)
                        if 15 in a_player:
                            v1.delete(x15)
                            v1.delete(x_15)
                        if 16 in a_machine:
                            v1.delete(o16)
                        if 17 in a_player:
                            v1.delete(x17)
                            v1.delete(x_17)
                        if 18 in a_machine:
                            v1.delete(o18)
                        a_machine.clear()
                        a_player.clear()
                        res.clear()
                        v1.delete(win15)
                    b25=Button(vent,text="Play Again",width=15,height=4,command=lambda:pul(25)).place(x=140,y=150)

def reset(num):
        b1.place(x=120,y=135)
        b2.place(x=140,y=135)
        b3.place(x=120,y=300)
        b4.place(x=140,y=300)
        b5.place(x=120,y=465)
        b6.place(x=140,y=465)
        b7.place(x=285,y=135)
        b8.place(x=305,y=135)
        b9.place(x=285,y=300)
        b10.place(x=305,y=300)
        b11.place(x=285,y=465)
        b12.place(x=305,y=465)
        b13.place(x=450,y=135)
        b14.place(x=470,y=135)
        b15.place(x=450,y=300)
        b16.place(x=470,y=300)
        b17.place(x=450,y=465)
        b18.place(x=470,y=465)
        lis_mach.clear()
        for i in range(19):
            lis_mach.append(i)
            if 1 in a_player:
                v1.delete(x1)
                v1.delete(x_1)
        if 2 in a_machine:
            v1.delete(o2)
        if 3 in a_player:
            v1.delete(x3)
            v1.delete(x_3)
        if 4 in a_machine:
            v1.delete(o4)
        if 5 in a_player:
            v1.delete(x5)
            v1.delete(x_5)
        if 6 in a_machine:
            v1.delete(o6)
        if 7 in a_player:
            v1.delete(x7)
            v1.delete(x_7)
        if 8 in a_machine:
            v1.delete(o8)
        if 9 in a_player:
            v1.delete(x9)
            v1.delete(x_9)
        if 10 in a_machine:
            v1.delete(o10)
        if 11 in a_player:
            v1.delete(x11)
            v1.delete(x_11)
        if 12 in a_machine:
            v1.delete(o12)
        if 13 in a_player:
            v1.delete(x13)
            v1.delete(x_13)
        if 14 in a_machine:
            v1.delete(o14)
        if 15 in a_player:
            v1.delete(x15)
            v1.delete(x_15)
        if 16 in a_machine:
            v1.delete(o16)
        if 17 in a_player:
            v1.delete(x17)
            v1.delete(x_17)
        if 18 in a_machine:
            v1.delete(o18)
        a_machine.clear()
        a_player.clear()
        res.clear()




#Columna derecha
b1=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="X",background="White",command=lambda:pulsacion(1))
b1.place(x=120,y=135)
b2=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="O",background="White",command=lambda:pulsacion(2))
b2.place(x=140,y=135)
b3=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="X",background="White",command=lambda:pulsacion(3))
b3.place(x=120,y=300)
b4=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="O",background="White",command=lambda:pulsacion(4))
b4.place(x=140,y=300)
b5=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="X",background="White",command=lambda:pulsacion(5))
b5.place(x=120,y=465)
b6=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="O",background="White",command=lambda:pulsacion(6))
b6.place(x=140,y=465)


#Columna central
b7=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="X",background="White",command=lambda:pulsacion(7))
b7.place(x=285,y=135)
b8=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="O",background="White",command=lambda:pulsacion(8))
b8.place(x=305,y=135)
b9=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="X",background="White",command=lambda:pulsacion(9))
b9.place(x=285,y=300)
b10=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="O",background="White",command=lambda:pulsacion(10))
b10.place(x=305,y=300)
b11=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="X",background="White",command=lambda:pulsacion(11))
b11.place(x=285,y=465)
b12=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="O",background="White",command=lambda:pulsacion(12))
b12.place(x=305,y=465)


#Columna izquierda
b13=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="X",background="White",command=lambda:pulsacion(13))
b13.place(x=450,y=135)
b14=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="O",background="White",command=lambda:pulsacion(14))
b14.place(x=470,y=135)
b15=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="X",background="White",command=lambda:pulsacion(15))
b15.place(x=450,y=300)
b16=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="O",background="White",command=lambda:pulsacion(16))
b16.place(x=470,y=300)
b17=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="X",background="White",command=lambda:pulsacion(17))
b17.place(x=450,y=465)
b18=Button(v,font=("arial",10),width=1,height=1,relief="flat",text="O",background="White",command=lambda:pulsacion(18))
b18.place(x=470,y=465)


#boton reseteo

b19=Button(v,font=("arial",10),text="Reseteo",width=9,height=1,background="White",command=lambda:reset(1))
b19.place(x=400,y=520)


#(nombre boton).place_forget() ocultar boton. Si se quiere volver a ver (nombre boton).place(x=,y=)


mainloop()
