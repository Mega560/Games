import random
from Tkinter import*

vent=Tk()

wd=40
hg=5

x = 0
a = 0

machine=""

player=""

resultado=""

def Botonclick(num):
    if num==1:
        vent.destroy()
        v=Tk("1")
        v.geometry("1370x300")
        v.title("El juego de Piedra, Papel y Tijera")
        
        mach1=StringVar()

        
        player1=StringVar()

        
        resultado1=StringVar()


        #resultado machine global con x,y,z
        
        rmachine1=StringVar()


        #resultado jugador global a,b,c
        
        jresultado=StringVar()

        l_1 = ["Piedra", "Papel", "Tijera"]
        v.mainloop
        ab=60
        al=2
        def btnClick(num):
            machine = random.choice(l_1)
            mach1.set(machine)
            if num==0:
                player = "Piedra"
                player1.set(player)
                if machine=="Papel":
                    resultado = "Tu Pierdes"
                    resultado1.set(resultado)
                    global a
                    global x
                    x = x+1
                    rmachine1.set(x)
                    if x==3 and a<3:
                        wi=Tk()
                        wi.geometry("700x300")
                        wi.title("El juego de Piedra, Papel y Tijera")
                        Label(wi,text="You lose",font=("arial",20)).place(x=300,y=130)
                elif machine=="Tijera":
                    resultado = "Tu ganas"
                    resultado1.set(resultado)
                    global ab
                    a = a + 1
                    jresultado.set(a)
                    if a==3 and x<3:
                        win=Tk()
                        win.geometry("700x300")
                        win.title("El juego de Piedra, Papel y Tijera")
                        Label(win,text="You win",font=("arial",20)).place(x=300,y=130)  
                elif machine=="Piedra":
                    resultado = "Empate"
                    resultado1.set(resultado)
            elif num==1:
                player = "Papel"
                player1.set(player)
                if machine=="Papel":
                    resultado = "Empate"
                    resultado1.set(resultado)
                elif machine=="Tijera":
                    resultado = "Tu pierdes"
                    resultado1.set(resultado)
                    global y
                    x = x + 1
                    rmachine1.set(x)
                    if x==3 and a<3:
                        wi=Tk()
                        wi.geometry("700x300")
                        wi.title("El juego de Piedra, Papel y Tijera")
                        Label(wi,text="You lose",font=("arial",20)).place(x=300,y=130)
                elif machine=="Piedra":
                    resultado = "Tu ganas"
                    resultado1.set(resultado)
                    global b
                    a = a + 1
                    jresultado.set(a)
                    if a==3 and x<3:
                        win=Tk()
                        win.geometry("700x300")
                        win.title("El juego de Piedra, Papel y Tijera")
                        Label(win,text="You win",font=("arial",20)).place(x=300,y=130)
            elif num==2:
                player = "Tijera"
                player1.set(player)
                if machine=="Papel":
                    resultado = "Tu ganas"
                    resultado1.set(resultado)
                    global c
                    a = a + 1
                    jresultado.set(a)
                    if a==3 and x<3:
                        win=Tk()
                        win.geometry("700x300")
                        win.title("El juego de Piedra, Papel y Tijera")
                        Label(win,text="You win",font=("arial",20)).place(x=300,y=130)
                elif machine=="Tijera":
                    resultado = "Empate"
                    resultado1.set(resultado)
                elif machine=="Piedra":
                    resultado = "Tu pierdes"
                    resultado1.set(resultado)
                    global z
                    x = x +1
                    rmachine1.set(x)
                    if x==3 and a<3:
                        wi=Tk()
                        wi.geometry("700x300")
                        wi.title("El juego de Piedra, Papel y Tijera")
                        Label(wi,text="You lose",font=("arial",20)).place(x=300,y=130)
    if num==2:
        vent.destroy()
        v=Tk("1")
        v.geometry("1370x300")
        v.title("El juego de Piedra, Papel y Tijera")
        
        mach1=StringVar()

        
        player1=StringVar()

        
        resultado1=StringVar()


        #resultado machine global con x,y,z
        
        rmachine1=StringVar()


        #resultado jugador global a,b,c
        
        jresultado=StringVar()

        l_1 = ["Piedra", "Papel", "Tijera"]
        v.mainloop
        ab=60
        al=2
        def btnClick(num):
            machine = random.choice(l_1)
            mach1.set(machine)
            if num==0:
                player = "Piedra"
                player1.set(player)
                if machine=="Papel":
                    resultado = "Tu Pierdes"
                    resultado1.set(resultado)
                    global a
                    global x
                    x = x+1
                    rmachine1.set(x)
                elif machine=="Tijera":
                    resultado = "Tu ganas"
                    resultado1.set(resultado)
                    global ab
                    a = a + 1
                    jresultado.set(a)  
                elif machine=="Piedra":
                    resultado = "Empate"
                    resultado1.set(resultado)
            elif num==1:
                player = "Papel"
                player1.set(player)
                if machine=="Papel":
                    resultado = "Empate"
                    resultado1.set(resultado)
                elif machine=="Tijera":
                    resultado = "Tu pierdes"
                    resultado1.set(resultado)
                    global y
                    x = x + 1
                    rmachine1.set(x)
                elif machine=="Piedra":
                    resultado = "Tu ganas"
                    resultado1.set(resultado)
                    global b
                    a = a + 1
                    jresultado.set(a)
            elif num==2:
                player = "Tijera"
                player1.set(player)
                if machine=="Papel":
                    resultado = "Tu ganas"
                    resultado1.set(resultado)
                    global c
                    a = a + 1
                    jresultado.set(a)
                elif machine=="Tijera":
                    resultado = "Empate"
                    resultado1.set(resultado)
                elif machine=="Piedra":
                    resultado = "Tu pierdes"
                    resultado1.set(resultado)
                    global z
                    x = x +1
                    rmachine1.set(x)
                   
    #Texto play

    
    Label(v,text="Play",font=("arial",20)).place(x=685,y=25)


    #Texto machine y player
    Label(v,textvariable=mach1,font=("arial",20)).place(x=285,y=100)
    Label(v,textvariable=player1,font=("arial",20)).place(x=955,y=100)


    #Texto resultado
    Label(v,textvariable=resultado1,font=("arial",20)).place(x=655,y=150)


    #Marcador
    Label(v,text="Marcador",font=("arial",20)).place(x=1160,y=10)
    Label(v,text="Machine",font=("arial",15)).place(x=1100,y=60)
    Label(v,text="You",font=("arial",15)).place(x=1275,y=60)
    #Resultado Marcador
    Label(v,textvariable=rmachine1,font=("arial",15)).place(x=1185,y=60)
    Label(v,textvariable=jresultado,font=("arial",15)).place(x=1250,y=60)


    #Botones
    b1=Button(v,text="Piedra",width=ab,height=al,command=lambda:btnClick(0)).place(x=15,y=200)
    b2=Button(v,text="Papel",width=ab,height=al,command=lambda:btnClick(1)).place(x=465,y=200)
    b3=Button(v,text="Tijeras",width=ab,height=al,command=lambda:btnClick(2)).place(x=915,y=200)

vent.geometry("700x300")
vent.title("El juego de Piedra, Papel y Tijera")


Label(vent,text="Bienvenido al juego de piedra, papel y tijera.",font=("arial",20)).place(x=80,y=100)

#Botones seleccion de juego
b4=Button(vent,text="El mejor de 3",width=wd,height=hg,command=lambda:Botonclick(1)).place(x=20,y=200)
b5=Button(vent,text="Juego libre",width=wd,height=hg,command=lambda:Botonclick(2)).place(x=390,y=200)


vent.mainloop()


#Al inserta esta ventan poner vent.destroy() despues del global de 
# seleccion para cerrar la ventana
