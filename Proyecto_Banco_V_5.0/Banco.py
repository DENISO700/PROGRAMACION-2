from CuentaBancaria import*
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from io import open
import pandas as pd
from datetime import date
from datetime import datetime,timedelta
from re import search, split, findall
from tkinter import filedialog
import numpy as np
import shutil
import matplotlib.pyplot as plt
import random
from tkcalendar import Calendar 

class BancoAzteca:

    def menu(self):
        self.ventanamenu=Tk()
        self.ventanamenu.title(110*" "+"Banco Azteca")
        self.configuracionmenu()
        self.labelbuttonMenu()
        self.center(self.ventanamenu)
        self.ventanamenu.mainloop()
    
    def configuracionmenu(self): 
        self.ventanamenu.geometry("762x820")   
        self.ventanamenu.resizable(False,False)  
        self.ventanamenu.iconbitmap("imagenes/icono.ico")
        #======Fondo Imagen================
        self.bg=PhotoImage(file="imagenes/fondo1.png")
        self.Fondo=Label(self.ventanamenu, image=self.bg)
        self.Fondo.place(x=0, y=0, width=self.bg.width(), height=self.bg.height())
        #=======Titulo=====================
        self.lbl1M=Label(self.ventanamenu, text="Sistema de Banco Azteca")
        self.lbl1M.config(font=("Impact",30), bg="red4", fg="white")
        self.lbl1M.place(x=0, y=10,width=800, height=80)
        #=======Menu Frame=================
        self.Frame_menu=Frame(self.ventanamenu, bg="OliveDrab4")
        self.Frame_menu.place(x=50,y=120, height=650,width=660)

    def labelbuttonMenu(self):
     #==== Seccion cuentas=============
        self.lbl1C=Label(self.ventanamenu, text="Acciones Cuenta:")
        self.lbl1C.config(font=("Goudy old style",18, "bold"),bg="OliveDrab4")
        self.lbl1C.place(x=80, y=150)
     #=========Nueva cuenta===============
        self.fondonuevo=PhotoImage(file="imagenes/nuevaCuenta.png")
        self.btn1Nuevo=Button(self.Frame_menu,image=self.fondonuevo)
        self.btn1Nuevo.place(x=60, y=80, width=90, height=90)
        self.btn1Nuevo.config(bg="OliveDrab4")
        self.btn1Nuevo.config(command=self.ventana_nueva_cuenta)
        self.lbl2C=Label(self.ventanamenu, text="Nueva")
        self.lbl2C.config(font=("Goudy old style",14), bg="OliveDrab4", fg="white") 
        self.lbl2C.place(x=125, y=295)
     #=========Deposito===============
        self.fondodeposito=PhotoImage(file="imagenes/deposito.png")
        self.btn2Deposito=Button(self.Frame_menu,image=self.fondodeposito)
        self.btn2Deposito.config(bg="OliveDrab4")
        self.btn2Deposito.place(x=210, y=80, width=90, height=90)
        self.btn2Deposito.config(command=self.ventana_cuenta_deposito)
        self.lbl3C=Label(self.ventanamenu, text="Depósito")
        self.lbl3C.config(font=("Goudy old style",14), bg="OliveDrab4", fg="white")
        self.lbl3C.place(x=264, y=295)
     #=========Retiro===============
        self.fondoRetiro=PhotoImage(file="imagenes/retiro.png")
        self.btn3Retiro=Button(self.Frame_menu,image=self.fondoRetiro)
        self.btn3Retiro.config(bg="OliveDrab4")
        self.btn3Retiro.place(x=360, y=80, width=90, height=90)
        self.btn3Retiro.config(command=self.ventana_cuenta_retiro)
        self.lbl4C=Label(self.ventanamenu, text="Retiro")              
        self.lbl4C.place(x=424, y=295)           
        self.lbl4C.config(font=("Goudy old style",14), bg="OliveDrab4", fg="white")
        #=========VerUsuario===============
        self.fondoUsuario=PhotoImage(file="imagenes/verUsuario.png")
        self.btn3Usuario=Button(self.Frame_menu,image=self.fondoUsuario)
        self.btn3Usuario.config(bg="OliveDrab4")
        self.btn3Usuario.place(x=510, y=80, width=90, height=90)
        self.btn3Usuario.config(command=self.ventana_vista_usuario)
        self.lbl4C=Label(self.ventanamenu, text="Ver Usuario")              
        self.lbl4C.place(x=554, y=295)           
        self.lbl4C.config(font=("Goudy old style",14), bg="OliveDrab4", fg="white")

     #====  Seccion Registros=============
        self.lbl6C=Label(self.ventanamenu, text="Acciones Registros:")
        self.lbl6C.config(font=("Goudy old style",18, "bold"),bg="OliveDrab4")
        self.lbl6C.place(x=80, y=350)
     #=========Cuentas del Banco===============
        self.fondoinfg=PhotoImage(file="imagenes/general.png")
        self.btn5G=Button(self.Frame_menu,image=self.fondoinfg)
        self.btn5G.config(bg="OliveDrab4")
        self.btn5G.place(x=60, y=282, width=90, height=90)
        self.btn5G.config(command=self.ventana_informe_general)
        self.lbl7C=Label(self.ventanamenu, text="General")              
        self.lbl7C.place(x=120, y=497)           
        self.lbl7C.config(font=("Goudy old style",14), bg="OliveDrab4", fg="white")
     #=========Cargar Historial Movimientos===============
        self.fondohistorialMovimientos=PhotoImage(file="imagenes/historial.png")
        self.btn5G=Button(self.Frame_menu,image=self.fondohistorialMovimientos)
        self.btn5G.config(bg="OliveDrab4")
        self.btn5G.place(x=230, y=282, width=90, height=90)
        self.btn5G.config(command=self.ventana_Movimientos)
        self.lbl8C=Label(self.ventanamenu, text="Movimientos")              
        self.lbl8C.place(x=270, y=497)           
        self.lbl8C.config(font=("Goudy old style",14), bg="OliveDrab4", fg="white")
     #=========Cargar Distribucion de Saldos===============
        self.fondoSaldosCiudad=PhotoImage(file="imagenes/distribucion.png")
        self.btn6G=Button(self.Frame_menu,image=self.fondoSaldosCiudad)
        self.btn6G.config(bg="OliveDrab4")
        self.btn6G.place(x=400, y=282, width=90, height=90)
        self.btn6G.config(command=self.ventana_distribucion_saldos)
        self.lbl9C=Label(self.ventanamenu, text="Distribucion Saldos")              
        self.lbl9C.place(x=420, y=497)           
        self.lbl9C.config(font=("Goudy old style",14), bg="OliveDrab4", fg="white")

        #====  Seccion Creditos=============
        self.lbl10C=Label(self.ventanamenu, text="Creditos:")
        self.lbl10C.config(font=("Goudy old style",18, "bold"),bg="OliveDrab4")
        self.lbl10C.place(x=80, y=550)
     #=========Creditos del Banco===============
        self.fondocreditos=PhotoImage(file="imagenes/creditos.png")
        self.btn7G=Button(self.Frame_menu,image=self.fondocreditos)
        self.btn7G.config(bg="OliveDrab4")
        self.btn7G.place(x=60, y=484, width=90, height=90)
        self.btn7G.config(command=self.ventana_Creditos)
        self.lbl11C=Label(self.ventanamenu, text="Creditos")              
        self.lbl11C.place(x=120, y=699)           
        self.lbl11C.config(font=("Goudy old style",14), bg="OliveDrab4", fg="white")
     #=========Nuevo Credito===============
        self.fondonuevoCredito=PhotoImage(file="imagenes/nuevoCredito.png")
        self.btn8G=Button(self.Frame_menu,image=self.fondonuevoCredito)
        self.btn8G.config(bg="OliveDrab4")
        self.btn8G.place(x=230, y=484, width=90, height=90)
        self.btn8G.config(command=self.ventana_nuevo_credito)
        self.lbl12C=Label(self.ventanamenu, text="Nuevo ")              
        self.lbl12C.place(x=290, y=699)           
        self.lbl12C.config(font=("Goudy old style",14), bg="OliveDrab4", fg="white")
     #=========Ingresos Futuros===============
        self.fondoIngresosFuturos=PhotoImage(file="imagenes/ingresosFuturos.png")
        self.btn9G=Button(self.Frame_menu,image=self.fondoIngresosFuturos)
        self.btn9G.config(bg="OliveDrab4")
        self.btn9G.place(x=400, y=484, width=90, height=90)
        self.btn9G.config(command=self.ventana_ingresosFuturos)
        self.lbl13C=Label(self.ventanamenu, text="Ingresos Futuros")              
        self.lbl13C.place(x=420, y=699)           
        self.lbl13C.config(font=("Goudy old style",14), bg="OliveDrab4", fg="white")

    #===============================acerca===================================

        #label Acerca de
        self.botonAcerca=Button(self.Frame_menu, text="Acerca de...", width=8, height=1, background="gainsboro",foreground="blue", relief="flat",command=lambda:self.acercaDe())
        self.botonAcerca.grid(row=5, column=5,)
        self.btn9G.place(x=400, y=484, width=90, height=90)

#=========================Funcion para centrar Ventanas=========================== 
    def center(self,win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

#===========Funciones de Retroceso===================================================================
    def atras_nuevo(self):
        self.Nueva_cuenta.withdraw()
        self.ventanamenu.deiconify()
    def atras_deposito(self):
        self.root.withdraw()
        self.ventanamenu.deiconify()
    def atras_retiro(self):
        self.retiro_cuenta.withdraw()
        self.ventanamenu.deiconify()
    def atras_vista(self):
        self.vistaUsuario.withdraw()
        self.ventanamenu.deiconify()
    def atras_general(self):
        self.infgeneral.withdraw()
        self.ventanamenu.deiconify()
    def atras_movimientos(self):
        self.movimientos.withdraw()
        self.ventanamenu.deiconify()
    def atras_distribucion(self):
        self.distsaldo.withdraw()
        self.ventanamenu.deiconify()
    def atras_creditos(self):
        self.Creditos.withdraw()
        self.ventanamenu.deiconify()
    def atras_futuro(self):
        self.ingresosFuturos.withdraw()
        self.ventanamenu.deiconify()
    def atras_pagos(self):
        self.planPagos.destroy()
        self.ventana_Creditos()
    def atras_nuevocredito(self):
        self.Nuevo_credito.withdraw()
        self.ventanamenu.deiconify()

    def acercaDe(self):
            messagebox.showinfo(message="MM418-Programacion II\nGrupo 4\nProyecto: \n\tBanco\nIntegrates: \n\tDenis Ordoñez 20171002520 \n\tNotier Padilla 20161031441\n\tFredy Salgado 20181001344\n\tDunia García 20161000164 \n\tMaría  Reyes 20181005308", title="Acerca de")

#===========Ventana de Cuenta Nueva===================================================================
    def vaciarCampos(self):
        self.txtNC.delete(0, END)
        self.txtNC2.delete(0, END)
        self.txtNC3.delete(0, END)
        self.txtNC.focus()

    def vaciarCamposCreditos(self):
        self.idCredito
        self.idCredito.focus()

    def is_valid_date(self,action, char, text):
        # Solo chequear cuando se añade un carácter.
        if action != "1":
            return True
        return char in "0123456789/" and len(text) < 10
#===========Ventana de Cuenta Nueva===================================================================
    
    def ventana_nueva_cuenta(self):
        cb=CuentaBancaria()
        self.ventanamenu.withdraw()              
        self.Nueva_cuenta=Toplevel(self.ventanamenu)
        self.Nueva_cuenta.title("Creación de una nueva cuenta")
        self.Nueva_cuenta.geometry("694x340")
        self.Nueva_cuenta.resizable(False,False)
        self.center(self.Nueva_cuenta)

        self.validatecommand = self.ventanamenu.register(self.is_valid_date)

        self.Nueva_cuenta.title( "Creación de una cuenta nueva" )
        self.Nueva_cuenta.config( bg="#D8D6D6" )

        self.fnuevo=PhotoImage(file="imagenes/fondo1.png")
        self.Fondon=Label(self.Nueva_cuenta, image=self.fnuevo)
        self.Fondon.place(x=0, y=0)

        self.lbl1 = Label( self.Nueva_cuenta, text="Creación de una cuenta nueva" )
        self.lbl1.config( font=("Impact",25), bg="red4", fg="white" )
        self.lbl1.place( relx=0.04, rely=0.09, relwidth=0.93, relheight=0.12 )

        self.Frame_ncuenta=Frame(self.Nueva_cuenta, bg="DarkOliveGreen4")
        self.Frame_ncuenta.place(x=30,y=100, height=200,width=640)

        #variables
        self.nombreVN = StringVar()
        self.apellidoVN = StringVar()
        self.ciudadVN = StringVar()
        self.saldoVN = IntVar()
        self.t_cuenta = IntVar()
        #self.t_cuenta.set(1)

        self.lbl2 = Label( self.Nueva_cuenta, text="Nombre:" )
        self.lbl2.config( bg="DarkOliveGreen4",font=("Goudy old style",18, "bold") )
        self.lbl2.place( relx=0.06, rely=0.37)

        self.txtNC = Entry(self.Nueva_cuenta, textvariable=self.nombreVN,justify = "center")
        self.txtNC .place( relx=0.30, rely=0.39, relwidth=0.2, relheight=0.07)

        self.lbl4 = Label( self.Nueva_cuenta, text="Apellido:" )
        self.lbl4.config( bg="DarkOliveGreen4" ,font=("Goudy old style",18, "bold"))
        self.lbl4.place( relx=0.56, rely=0.37)

        self.txtNC3 = Entry( self.Nueva_cuenta, textvariable=self.apellidoVN,justify = "center" )
        self.txtNC3.place( relx=0.73, rely=0.39, relwidth=0.2, relheight=0.07 )
        
        self.lbl5 = Label( self.Nueva_cuenta, text="Ciudad:" )
        self.lbl5.config( bg="DarkOliveGreen4" ,font=("Goudy old style",18, "bold"))
        self.lbl5.place( relx=0.56, rely=0.54)

        self.txtNC4 = Entry( self.Nueva_cuenta, textvariable=self.ciudadVN,justify = "center" )
        self.txtNC4.place( relx=0.73, rely=0.56, relwidth=0.2, relheight=0.07 )

        self.lbl3 = Label( self.Nueva_cuenta, text="Saldo inicial:" )
        self.lbl3.config( bg="DarkOliveGreen4",font=("Goudy old style",18, "bold") )
        self.lbl3.place( relx=0.06, rely=0.54)

        self.txtNC2 = Entry( self.Nueva_cuenta, textvariable=self.saldoVN,justify = "center",validate="key",
                  validatecommand=(self.validatecommand, "%d", "%S", "%s") )
        self.txtNC2.place( relx=0.30, rely=0.56, relwidth=0.2, relheight=0.07 )
    
        self.menur = Button( self.Nueva_cuenta, text="Menú" )
        self.menur.config( bg='IndianRed4' )
        self.menur.config( command = self.atras_nuevo )
        self.menur.place( relx=0.80, rely=0.74,relwidth=0.13, relheight=0.07)


        self.guardar = Button( self.Nueva_cuenta, text="Guardar" )
        self.guardar.config( bg='IndianRed4' )
        self.guardar.config( command=lambda: cb.registrarCuenta(self.txtNC.get(),self.txtNC3.get(),self.txtNC4.get(),self.txtNC2.get()) )
        self.guardar.place( relx=0.65, rely=0.74,relwidth=0.13, relheight=0.07)
        
#===========Ventana de deposito===============================================================

    def ventana_cuenta_deposito(self):
        self.ventanamenu.withdraw()                
        self.root=Toplevel(self.ventanamenu)
        self.config()
          
    def config(self):
        cb =CuentaBancaria()
        self.root.geometry("494x300")
        self.root.resizable(False,False)

        self.root.title( "Depósito" )
        self.root.config( bg="#D8D6D6" )
        self.center(self.root)
        self.validatecommand = self.ventanamenu.register(self.is_valid_date)

        self.fdep=PhotoImage(file="imagenes/fondo1.png")
        self.Fondod=Label(self.root, image=self.fdep)
        self.Fondod.place(x=0, y=0)

        self.Frame_dep=Frame(self.root, bg="OliveDrab4")
        self.Frame_dep.place(x=30,y=100, height=160,width=430)

        self.lbl1 = Label( self.root, text="Depósito" )
        self.lbl1.config( font=("Impact",25), bg="red4", fg="white" )
        self.lbl1.place( relx=0.04, rely=0.09, relwidth=0.91, relheight=0.12 )

        #----------------------------------
        self.ncuentad=StringVar()
        self.depositoc=IntVar()
        #----------------------------------

        self.lbl2 = Label( self.root, text="N Cuenta:" )
        self.lbl2.config( bg="OliveDrab4",font=("Goudy old style",18, "bold"))
        self.lbl2.place(relx=0.06, rely=0.41)

        self.txtCamp1 = Entry(self.root, textvariable=self.ncuentad,validate="key",
                  validatecommand=(self.validatecommand, "%d", "%S", "%s"))
        self.txtCamp1.place(relx=0.26, rely=0.43, relwidth=0.2, relheight=0.07)


        self.lbl4 = Label( self.root, text="Monto:" )
        self.lbl4.config(bg="OliveDrab4",font=("Goudy old style",18, "bold"))
        self.lbl4.place(relx=0.06, rely=0.55)

        self.txtCamp3 = Entry(self.root, textvariable=self.depositoc,validate="key",
                  validatecommand=(self.validatecommand, "%d", "%S", "%s"))
        self.txtCamp3.place(relx=0.26, rely=0.57 , relwidth=0.2, relheight=0.07)

        self.menud = Button( self.root, text="Menú" )
        self.menud.config( bg='IndianRed4' )
        self.menud.config( command = self.atras_deposito )
        self.menud.place( relx=0.60, rely=0.75,relwidth=0.13, relheight=0.07)

       
        self.btn2 = Button( self.root, text="Depositar" )
        self.btn2.config( bg='IndianRed4' )
        self.btn2.config( command=lambda:cb.RealizarDeposito(self.ncuentad.get(),self.depositoc.get()))
        self.btn2.place( relx=0.48, rely=0.58, relwidth=0.12, relheight=0.07 )
        
#===========Ventana de Cuenta Retiro==================================================================
 
    def ventana_cuenta_retiro(self):
        self.ventanamenu.withdraw()              
        self.retiro_cuenta=Toplevel(self.ventanamenu)
        self.configRetiro()

    def configRetiro(self):

        cb=CuentaBancaria()
        #=======Titulo=====================
        self.retiro_cuenta.title("Retiro de una cuenta")
        self.retiro_cuenta.geometry("560x320")
        self.retiro_cuenta.resizable(False,False)
        self.center(self.retiro_cuenta)
        self.validatecommand = self.ventanamenu.register(self.is_valid_date)

        self.fretiro=PhotoImage(file="imagenes/fondo1.png")
        self.Fondor=Label(self.retiro_cuenta, image=self.fretiro)
        self.Fondor.place(x=0, y=0)

        self.Frame_retiro=Frame(self.retiro_cuenta, bg="DarkOliveGreen4")
        self.Frame_retiro.place(x=23,y=110, height=180,width=515)

        self.lbl1R=Label(self.retiro_cuenta, text="Retiro")
        self.lbl1R.place(x=23, y=35,width=515, height=50)
        self.lbl1R.config(font=("Impact",25), bg="red4", fg="white")

     #==== N cuenta=============

        self.lbl1vr=Label(self.retiro_cuenta, text="N Cuenta:")
        self.lbl1vr.config( bg="DarkOliveGreen4",font=("Goudy old style",18, "bold"))
        self.lbl1vr.place(x=140, y=125)

        self.ncuentar=StringVar()
        self.retiroc=IntVar()

        self.txtn=Entry(self.retiro_cuenta,validate="key",
                  validatecommand=(self.validatecommand, "%d", "%S", "%s"))
        self.txtn.config(textvariable=self.ncuentar)
        self.txtn.place(relx=0.47, rely=0.41, relwidth=0.24, relheight=0.07)

     #==== Retiro =============
        self.lbl3vr=Label(self.retiro_cuenta, text="Cantidad:")              
        self.lbl3vr.config( bg="DarkOliveGreen4",font=("Goudy old style",18, "bold"))

        self.lbl3vr.place(x=140, y=175)

        self.txtvr=Entry(self.retiro_cuenta,validate="key",
                  validatecommand=(self.validatecommand, "%d", "%S", "%s") )
        self.txtvr.config(textvariable=self.retiroc)
        self.txtvr.place(relx=0.47, rely=0.57, relwidth=0.24, relheight=0.07)

        self.menur = Button( self.retiro_cuenta, text="Menú" )
        self.menur.config( bg='IndianRed4' )
        self.menur.config( command = self.atras_retiro )
        self.menur.place( relx=0.82, rely=0.80,relwidth=0.13, relheight=0.07)
        
        #==== Realizarlo =============
        self.btn2 = Button( self.retiro_cuenta, text="Retirar" )
        self.btn2.config( bg='IndianRed4' )
        self.btn2.config( command=lambda:cb.RealizarRetiro(self.ncuentar.get(),self.retiroc.get()))
        self.btn2.place( relx=0.75, rely=0.57, relwidth=0.13, relheight=0.07 )   
      
#=====================VENTANA VISTA USUARIO================================================
    def ventana_vista_usuario(self):
        self.ventanamenu.withdraw()              
        self.vistaUsuario=Toplevel(self.ventanamenu)
        self.vistaUsuario.title("Creación de una nueva cuenta")
        self.vistaUsuario.geometry("594x480")
        self.vistaUsuario.resizable(False,False)
        self.center(self.vistaUsuario)
        self.validatecommand = self.ventanamenu.register(self.is_valid_date)

        self.vistaUsuario.title( "Creación de una cuenta nueva" )
        self.vistaUsuario.config( bg="#D8D6D6" )

        self.fnuevo=PhotoImage(file="imagenes/fondo1.png")
        self.Fondon=Label(self.vistaUsuario, image=self.fnuevo)
        self.Fondon.place(x=0, y=0)

        self.lbl1 = Label( self.vistaUsuario, text="Ver Usuario" )
        self.lbl1.config( font=("Impact",25), bg="red4", fg="white" )
        self.lbl1.place( relx=0.04, rely=0.09, relwidth=0.93, relheight=0.1 )

        self.Frame_ncuenta=Frame(self.vistaUsuario, bg="DarkOliveGreen4")
        self.Frame_ncuenta.place(x=23,y=110, height=335,width=550)

        #variables
        self.nombreVN = StringVar()
        self.apellidoVN = StringVar()
        self.saldoVN = IntVar()
        self.t_cuenta = IntVar()
        #self.t_cuenta.set(1)

        self.lbl2 = Label( self.vistaUsuario, text="Cuenta:" )
        self.lbl2.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
        self.lbl2.place( relx=0.30, rely=0.25)
           
        self.txtNC = Entry(self.vistaUsuario, textvariable=self.t_cuenta,justify = "center",validate="key",
                  validatecommand=(self.validatecommand, "%d", "%S", "%s"))
        self.txtNC .place( relx=0.46, rely=0.26, relwidth=0.2, relheight=0.05)
        
        self.menuv = Button( self.vistaUsuario, text="Menú" )
        self.menuv.config( bg='IndianRed4' )
        self.menuv.config( command = self.atras_vista )
        self.menuv.place( relx=0.80, rely=0.84,relwidth=0.13, relheight=0.05)
        
        self.lbl3 = Label( self.vistaUsuario, text="Nombre:" )
        self.lbl3.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
        self.lbl3.place( relx=0.30, rely=0.35)
        
       
        self.lbl4 = Label( self.vistaUsuario, text="Apellido:" )
        self.lbl4.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
        self.lbl4.place( relx=0.30, rely=0.45)
        
        self.lbl5 = Label( self.vistaUsuario, text="Ciudad:" )
        self.lbl5.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
        self.lbl5.place( relx=0.30, rely=0.55)
        
        self.lbl6 = Label( self.vistaUsuario, text="Estatus:" )
        self.lbl6.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
        self.lbl6.place( relx=0.30, rely=0.65)
        
        self.lbl7 = Label( self.vistaUsuario, text="Saldo:" )
        self.lbl7.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
        self.lbl7.place( relx=0.30, rely=0.75)
        
        self.btnVer = Button( self.vistaUsuario, text="Ver usuario" )
        self.btnVer.config( bg='IndianRed4' )
        self.btnVer.config( command=lambda:self.VerUsuario(self.txtNC.get()))
        self.btnVer.place( relx=0.68, rely=0.26, relwidth=0.13, relheight=0.05 )
  
    def VerUsuario(self,cuenta):
        usuarios = open("data/CuentasBanco.txt","r")
        usuario = usuarios.readlines()
        usuarios.close()
        existencia=False
        for i in range(len(usuario)):
            j = usuario[i].count(cuenta)
            if j == 1:
                existencia=True
                break

        if existencia:
            Nom = str(usuario[i].split(",")[1])
            Ape = str(usuario[i].split(",")[2]) 
            Ciu = str(usuario[i].split(",")[3])
            Est = str(usuario[i].split(",")[4])
            Sal = str(usuario[i].split(",")[5])
                
            self.lbl3 = Label( self.vistaUsuario, text="Nombre:" )
            self.lbl3.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
            self.lbl3.place( relx=0.30, rely=0.35)
            
            self.lbl9 = Label( self.vistaUsuario, text=str(Nom) )
            self.lbl9.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
            self.lbl9.place( relx=0.46, rely=0.35)
            
            self.lbl4 = Label( self.vistaUsuario, text="Apellido:" )
            self.lbl4.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
            self.lbl4.place( relx=0.30, rely=0.45)

            self.lbl10 = Label( self.vistaUsuario, text=str(Ape) )
            self.lbl10.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
            self.lbl10.place( relx=0.46, rely=0.45)
            
            self.lbl5 = Label( self.vistaUsuario, text="Ciudad:" )
            self.lbl5.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
            self.lbl5.place( relx=0.30, rely=0.55)

            self.lbl11 = Label( self.vistaUsuario, text=str(Ciu) )
            self.lbl11.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
            self.lbl11.place( relx=0.46, rely=0.55)
            
            self.lbl6 = Label( self.vistaUsuario, text="Estatus:" )
            self.lbl6.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
            self.lbl6.place( relx=0.30, rely=0.65)
            
            self.lbl12 = Label( self.vistaUsuario, text=str(Est) )
            self.lbl12.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
            self.lbl12.place( relx=0.46, rely=0.65)

            self.lbl7 = Label( self.vistaUsuario, text="Saldo:" )
            self.lbl7.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
            self.lbl7.place( relx=0.30, rely=0.75)

            self.lbl14 = Label( self.vistaUsuario, text=str(Sal) )
            self.lbl14.config( bg="DarkOliveGreen4",font=("Goudy old style",16, "bold") )
            self.lbl14.place( relx=0.46, rely=0.75)
        else:
            messagebox.showerror("Vista Usuario", "La cuenta no Existe")

#=====================Funciones de Carga de Datos================================================
    def clear_data(self):
            self.tabla.delete(*self.tabla.get_children())
            return None  

    def Load_texto_data(self,filtro,ruta):

        if(filtro == "Distribucion"):

            self.texto_filename = (ruta)
            df = pd.read_csv(self.texto_filename)

            espacio=130


        if(filtro == "General"):

            self.texto_filename = (ruta)
            df = pd.read_csv(self.texto_filename)
            espacio=100
            

        if(filtro == "Movimientos"):

            self.texto_filename = (ruta)
            df = pd.read_csv(self.texto_filename)
            espacio=100

        if(filtro == "Creditos"):

            self.texto_filename = (ruta)
            df = pd.read_csv(self.texto_filename)
            espacio=115


        if(filtro == "Futuro"):

            self.filtrado()
            self.texto_filename = (ruta)
            df = pd.read_csv(self.texto_filename)
            

            espacio=115

        if(filtro == "Plan"):

            
            self.texto_filename = (ruta)
            df = pd.read_csv(self.texto_filename)
            espacio=100

            self.tablap.delete(*self.tablap.get_children())
            #Asigna el nombre de las columnas
            self.tablap["column"] = list(df.columns)
            #declara que las columnas se muestren la tablap de la ventana
            self.tablap["show"] = "headings"

            #Muestra cada interfaz en la interfaz
            for column in self.tablap["columns"]:
               self.tablap.heading(column, text=column,anchor=W) #Hace el encabezado= nombre de la columna
               self.tablap.column(column, width=espacio, stretch=False)

            df_rows = df.to_numpy().tolist() # convierte el marco de datos en una lista de listas
            for row in df_rows:
                self.tablap.insert("", "end", values=row) # inserta cada lista en la treeview.
            

            
        self.clear_data()
        #Asigna el nombre de las columnas
        self.tabla["column"] = list(df.columns)
        #declara que las columnas se muestren la tabla de la ventana
        self.tabla["show"] = "headings"

        #Muestra cada interfaz en la interfaz
        for column in self.tabla["columns"]:
           self.tabla.heading(column, text=column,anchor=W) #Hace el encabezado= nombre de la columna
           self.tabla.column(column, width=espacio, stretch=False)

           

        df_rows = df.to_numpy().tolist() # convierte el marco de datos en una lista de listas
        for row in df_rows:
            self.tabla.insert("", "end", values=row) # inserta cada lista en la treeview.

    def filtrado(self):

            creditos = open('data/CreditosBanco.txt', 'r+')
            datos = creditos.readlines()
            filtrado = []

            fecha=datetime.now()
            for i in range(len(datos)):
                    
                if i != len(datos)-1:
                    datos[i] = split(r"\n|,", datos[i])
                    datos[i].pop(-1)
                else:
                    datos[i] = split(r"\n|,", datos[i])

            for j in range(1,len(datos)):

                fecha_dt = datetime.strptime(datos[j][3], '%m/%d/%y')

                if fecha_dt.date()>fecha.date():
                    filtrado.append(datos[j])

            creditos.close()  


            ingresosFuturos="ID_Credito,Monto,FechaOtorgamiento,FechaVencimiento,TasaIntereses\n"

            for i in range(1,len(filtrado)):

                ingresosFuturos += filtrado[i][0] + ","+ filtrado[i][1] + "," + filtrado[i][2]+ ","+ filtrado[i][3] + ","+filtrado[i][4]+"\n"

            futuro = open('data/IngresosFuturos.txt', 'w')
            futuro.write(ingresosFuturos)
            futuro.close()

#===========Ventana de informe general===================================
    def ventana_informe_general(self):
        self.ventanamenu.withdraw() 
        self.infgeneral = tk.Toplevel()
        self.infgeneral.geometry("750x600")
        self.infgeneral.title("Cuentas Bancarias")
        self.infgeneral.iconbitmap("imagenes/icono.ico")
        self.infgeneral.resizable(0,0)
        self.center(self.infgeneral)

        self.fdep=PhotoImage(file="imagenes/fondo2.png")
        self.Fondod=Label(self.infgeneral, image=self.fdep)
        self.Fondod.place(x=0, y=0)

        self.lbl1R=Label(self.infgeneral, text="Informe General de Cuentas")
        self.lbl1R.place(x=43, y=25,width=664, height=50)
        self.lbl1R.config(font=("Impact",25), bg="red4", fg="white")

        self.frame1 = tk.LabelFrame(self.infgeneral, text="Detalles de todas las cuentas ",bg="snow3",font=("Goudy old style",15))
        self.frame1.place(relx=0.1, rely=0.16, height=350, width=600)


        self.tabla = ttk.Treeview(self.frame1)
        self.tabla.place(relheight=1, relwidth=1)

        self.treescrolly = tk.Scrollbar(self.frame1, orient="vertical", command=self.tabla.yview) 
        self.treescrollx = tk.Scrollbar(self.frame1, orient="horizontal", command=self.tabla.xview) 
        self.tabla.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set) # assigna el scrollbarsen el Treeview Widget
        self.treescrollx.pack(side="bottom", fill="x") # hacer que la barra de desplazamiento llene el eje x del widget Treeview
        self.treescrolly.pack(side="right", fill="y") # hacer que la barra de desplazamiento llene el eje y del widget Treeview

        self.lbl7R=Label(self.infgeneral, text="Total Fondos")
        self.lbl7R.place(x=380, y=460,width=150, height=25)
        self.lbl7R.config(font=("Impact",15), bg="red4", fg="white")

        self.lbl8R=Label(self.infgeneral, text=str(self.totalFondos()))
        self.lbl8R.place(x=520, y=460,width=150, height=25)
        self.lbl8R.config(font=("Impact",15), bg="red4", fg="white")

        self.menur = Button( self.infgeneral, text="Menú" )
        self.menur.config( bg='IndianRed4' )
        self.menur.config( command = self.atras_general)
        self.menur.place( relx=0.78, rely=0.84,relwidth=0.13, relheight=0.05)

        self.cargar = Button( self.infgeneral, text="Cargar" )
        self.cargar.config( bg='IndianRed4' )
        self.cargar.config( command = lambda:self.abrir("General"))
        self.cargar.place( relx=0.60, rely=0.84,relwidth=0.13, relheight=0.05)

        self.load_general()
    
    def load_general(self,ruta="data/CuentasBanco.txt"):
     self.Load_texto_data("General",ruta)

#=====================Ventana Movimientos==============================
    def ventana_Movimientos(self):
        self.ventanamenu.withdraw() 
        self.movimientos = tk.Toplevel()
        self.movimientos.geometry("750x560")
        self.movimientos.title("Movimientos")
        self.movimientos.iconbitmap("imagenes/icono.ico")
        self.movimientos.resizable(0,0)
        self.center(self.movimientos)

        self.fdep=PhotoImage(file="imagenes/fondo2.png")
        self.Fondod=Label(self.movimientos, image=self.fdep)
        self.Fondod.place(x=0, y=0)

        self.lbl1R=Label(self.movimientos, text="Informe Movimientos Bancarios")
        self.lbl1R.place(x=43, y=25,width=664, height=50)
        self.lbl1R.config(font=("Impact",25), bg="red4", fg="white")

        self.frame1 = tk.LabelFrame(self.movimientos, text="Detalles de todas las transacciones ",bg="snow3",font=("Goudy old style",15))
        self.frame1.place(relx=0.1, rely=0.16, height=350, width=600)


        self.tabla = ttk.Treeview(self.frame1)
        self.tabla.place(relheight=1, relwidth=1)

        self.treescrolly = tk.Scrollbar(self.frame1, orient="vertical", command=self.tabla.yview) 
        self.treescrollx = tk.Scrollbar(self.frame1, orient="horizontal", command=self.tabla.xview) 
        self.tabla.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set) # assigna el scrollbarsen el Treeview Widget
        self.treescrollx.pack(side="bottom", fill="x") # hacer que la barra de desplazamiento llene el eje x del widget Treeview
        self.treescrolly.pack(side="right", fill="y") # hacer que la barra de desplazamiento llene el eje y del widget Treeview


        self.menur = Button( self.movimientos, text="Menú" )
        self.menur.config( bg='IndianRed4' )
        self.menur.config( command = self.atras_movimientos)
        self.menur.place( relx=0.80, rely=0.84,relwidth=0.13, relheight=0.05)

        self.cargar = Button( self.movimientos, text="Cargar" )
        self.cargar.config( bg='IndianRed4' )
        self.cargar.config( command = lambda:self.abrir("Movimientos"))
        self.cargar.place( relx=0.62, rely=0.84,relwidth=0.13, relheight=0.05)

       
        

        self.load_movimientos()

    def load_movimientos(self,ruta="data/MovimientosCuentas.txt"):
     self.Load_texto_data("Movimientos",ruta)
#=====================Ventana Distribucion Saldos==============================
    def ventana_distribucion_saldos(self):
        self.ventanamenu.withdraw() 
        self.distsaldo = tk.Toplevel()
        self.distsaldo.geometry("600x560")
        self.distsaldo.title("Distribucion de saldos por ciudad de residencia")
        self.distsaldo.iconbitmap("imagenes/icono.ico")
        self.distsaldo.resizable(0,0)
        self.center(self.distsaldo)

        self.fdep=PhotoImage(file="imagenes/fondo2.png")
        self.Fondod=Label(self.distsaldo, image=self.fdep)
        self.Fondod.place(x=0, y=0)

        self.lbl1R=Label(self.distsaldo, text="Distribucion de saldos por ciudad")
        self.lbl1R.place(x=23, y=25,width=554, height=50)
        self.lbl1R.config(font=("Impact",25), bg="red4", fg="white")

        self.frame1 = tk.LabelFrame(self.distsaldo, text="Distribucion: ",bg="snow3",font=("Goudy old style",15))
        self.frame1.place(relx=0.13, rely=0.16, height=350, width=450)


        self.tabla = ttk.Treeview(self.frame1)
        self.tabla.place(relheight=1, relwidth=1)

        self.treescrolly = tk.Scrollbar(self.frame1, orient="vertical", command=self.tabla.yview) 
        self.treescrollx = tk.Scrollbar(self.frame1, orient="horizontal", command=self.tabla.xview) 
        self.tabla.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set) # assigna el scrollbarsen el Treeview Widget
        self.treescrollx.pack(side="bottom", fill="x") # hacer que la barra de desplazamiento llene el eje x del widget Treeview
        self.treescrolly.pack(side="right", fill="y") # hacer que la barra de desplazamiento llene el eje y del widget Treeview

        self.graficar = Button( self.distsaldo, text="Graficar" )
        self.graficar.config( bg='IndianRed4' )
        self.graficar.config( command = self.grafico)
        self.graficar.place( relx=0.63, rely=0.84,relwidth=0.13, relheight=0.05)


        self.menur = Button( self.distsaldo, text="Menú" )
        self.menur.config( bg='IndianRed4' )
        self.menur.config( command = self.atras_distribucion)
        self.menur.place( relx=0.80, rely=0.84,relwidth=0.13, relheight=0.05)

        self.DistribucionSaldos()
        self.load_distribucion()
        
    def DistribucionSaldos(self):
        ciudades=[]
        temp=[]
        filtro=[]
        cuentas = open('data/CuentasBanco.txt', 'r')
        datos = cuentas.readlines()

        for i in range(1,len(datos)):
            temp=datos[i].split(",")
            ciudades.append(temp[3])


        ciudades=list(set(ciudades))

        for i in range(len(ciudades)):
            filtro.append([ciudades[i],0])

        for i in range(1,len(datos)):
             temp2 = datos[i].split(",")
             
             for j in range(len(filtro)):
                 if filtro[j][0]==temp2[3]:
                    
                    filtro[j][1] +=float(temp2[5])


        cuentas.close()

        Distribucion="Ciudad,Total\n"
        for k in range(len(filtro)):

            Distribucion+=str(filtro[k][0]) + "," + str(filtro[k][1]) + "\n"


        DistribucionArchivo = open("data/DistSaldos.txt","w")
        DistribucionArchivo.write(Distribucion)

        DistribucionArchivo.close()

    def grafico(self):
        plotDis = pd.read_csv(self.texto_filename)
        my_plot = plotDis.plot("Ciudad","Total", kind="barh",figsize=(8, 4))
        
        plt.show()

    def load_distribucion(self,ruta="data/DistSaldos.txt"):
     self.Load_texto_data("Distribucion",ruta)

#=====================Ventana Creditos==============================
    def ventana_Creditos(self):

        self.ventanamenu.withdraw() 
        self.Creditos = tk.Toplevel()
        self.Creditos.geometry("750x550")
        self.Creditos.title("Creditos")
        self.Creditos.iconbitmap("imagenes/icono.ico")
        self.Creditos.resizable(0,0)
        self.center(self.Creditos)
        self.validatecommand = self.ventanamenu.register(self.is_valid_date)

        self.fdep=PhotoImage(file="imagenes/fondo2.png")
        self.Fondod=Label(self.Creditos, image=self.fdep)
        self.Fondod.place(x=0, y=0)

        self.lbl1R=Label(self.Creditos, text="Informe Creditos Bancarios")
        self.lbl1R.place(x=23, y=25,width=704, height=50)
        self.lbl1R.config(font=("Impact",25), bg="red4", fg="white")

        self.frame1 = tk.LabelFrame(self.Creditos, text="Detalles de todos los creditos ",bg="snow3",font=("Goudy old style",15))
        self.frame1.place(relx=0.1, rely=0.16, height=350, width=600)


        self.tabla = ttk.Treeview(self.frame1)
        self.tabla.place(relheight=1, relwidth=1)

        self.treescrolly = tk.Scrollbar(self.frame1, orient="vertical", command=self.tabla.yview) 
        self.treescrollx = tk.Scrollbar(self.frame1, orient="horizontal", command=self.tabla.xview) 
        self.tabla.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set) # assigna el scrollbarsen el Treeview Widget
        self.treescrollx.pack(side="bottom", fill="x") # hacer que la barra de desplazamiento llene el eje x del widget Treeview
        self.treescrolly.pack(side="right", fill="y") # hacer que la barra de desplazamiento llene el eje y del widget Treeview


        self.menur = Button( self.Creditos, text="Menú" )
        self.menur.config( bg='IndianRed4' )
        self.menur.config( command = self.atras_creditos)
        self.menur.place( relx=0.85, rely=0.85,relwidth=0.13, relheight=0.05)

        self.cargar = Button( self.Creditos, text="Cargar" )
        self.cargar.config( bg='IndianRed4' )
        self.cargar.config( command = lambda:self.abrir("Creditos"))
        self.cargar.place( relx=0.70, rely=0.85,relwidth=0.13, relheight=0.05)


        self.lblb=Label(self.Creditos, text="Id del Credito")
        self.lblb.place(x=100, y=472,width=100, height=20)
        self.lblb.config(font=("Impact",10), bg="OliveDrab4", fg="white")


        self.id_buscar = tk.StringVar()

        
        self.idCredito = Entry(self.Creditos, textvariable=self.id_buscar,validate="key",
                  validatecommand=(self.validatecommand, "%d", "%S", "%s"))
        self.idCredito.place(relx=0.28, rely=0.86 , relwidth=0.2, relheight=0.03)


        self.Plan = Button( self.Creditos, text="Ver Plan" )
        self.Plan.config( bg='IndianRed4' )
        self.Plan.config( command = lambda:self.buscarPlan(self.id_buscar.get()))
        self.Plan.place( relx=0.50, rely=0.86,relwidth=0.13, relheight=0.035)


        

        self.load_creditos()

    def load_creditos(self,ruta="data/CreditosBanco.txt"):
     self.Load_texto_data("Creditos",ruta)
     
#===========Ventana de nuevo credito===================================================================
    def ventana_nuevo_credito(self):
        self.ventanamenu.withdraw()              
        self.Nuevo_credito=Toplevel(self.ventanamenu)
        self.Nuevo_credito.title("Creación de un nuevo crédito")
        self.Nuevo_credito.geometry("694x450")
        self.Nuevo_credito.resizable(False,False)
        self.center(self.Nuevo_credito)
        self.validatecommand = self.ventanamenu.register(self.is_valid_date)

        self.Nuevo_credito.title( "Creación de un Nuevo Crédito" )
        self.Nuevo_credito.config( bg="#D8D6D6" )

        self.fnuevo=PhotoImage(file="imagenes/fondo1.png")
        self.Fondon=Label(self.Nuevo_credito, image=self.fnuevo)
        self.Fondon.place(x=0, y=0)

        self.lbl1 = Label( self.Nuevo_credito, text="Creación de un Nuevo Crédito" )
        self.lbl1.config( font=("Impact",25), bg="red4", fg="white" )
        self.lbl1.place( relx=0.04, rely=0.09, relwidth=0.92, relheight=0.1 )

        self.Frame_ncredito=Frame(self.Nuevo_credito, bg="OliveDrab4")
        self.Frame_ncredito.place(x=30,y=110, height=310,width=634)

        #variables
        self.montoNC = IntVar()
        self.otorgamientoNC = StringVar()
        self.vencimientoNC = StringVar()
        self.tasaNC = IntVar()

        self.lbl2 = Label( self.Nuevo_credito, text="Monto del crédito:" )
        self.lbl2.config( bg="OliveDrab4",font=("Goudy old style",18, "bold") )
        self.lbl2.place( relx=0.06, rely=0.27)

        self.txtNC = Entry(self.Nuevo_credito, textvariable=self.montoNC,justify = "center",validate="key",
                  validatecommand=(self.validatecommand, "%d", "%S", "%s"))
        self.txtNC .place( relx=0.50, rely=0.28, relwidth=0.2, relheight=0.06)

        self.lbl4 = Label( self.Nuevo_credito, text="Fecha de Otorgamiento:" )
        self.lbl4.config( bg="OliveDrab4" ,font=("Goudy old style",18, "bold"))
        self.lbl4.place( relx=0.06, rely=0.39)

        self.fo = Button( self.Nuevo_credito, text="Obtener Fecha" )
        self.fo.config( bg='IndianRed4' )
        self.fo.config( command = self.calendarioOtorgamiento )
        self.fo.place( relx=0.75, rely=0.39,relwidth=0.13, relheight=0.05)

        self.txtNC3 = Label( self.Nuevo_credito, textvariable=self.otorgamientoNC,justify = "center" )
        self.txtNC3.place( relx=0.50, rely=0.40, relwidth=0.2, relheight=0.06 )
        
        self.lbl5 = Label( self.Nuevo_credito, text="Fecha de Vencimiento:" )
        self.lbl5.config( bg="OliveDrab4" ,font=("Goudy old style",18, "bold"))
        self.lbl5.place( relx=0.06, rely=0.51)

        self.fv = Button( self.Nuevo_credito, text="Obtener Fecha" )
        self.fv.config( bg='IndianRed4' )
        self.fv.config( command = self.calendarioVencimiento )
        self.fv.place( relx=0.75, rely=0.51,relwidth=0.13, relheight=0.05)

        self.txtNC4 = Label( self.Nuevo_credito, textvariable=self.vencimientoNC,justify = "center" )
        self.txtNC4.place( relx=0.50, rely=0.52, relwidth=0.2, relheight=0.06 )

        self.lbl3 = Label( self.Nuevo_credito, text="Tasa de Interes:" )
        self.lbl3.config( bg="OliveDrab4",font=("Goudy old style",18, "bold") )
        self.lbl3.place( relx=0.06, rely=0.63)

        self.txtNC2 = Entry( self.Nuevo_credito, textvariable=self.tasaNC,justify = "center" ,validate="key",
                  validatecommand=(self.validatecommand, "%d", "%S", "%s"))
        self.txtNC2.place( relx=0.50, rely=0.64 , relwidth=0.2, relheight=0.06 )
    
        self.menur = Button( self.Nuevo_credito, text="Menú" )
        self.menur.config( bg='IndianRed4' )
        self.menur.config( command = self.atras_nuevocredito )
        self.menur.place( relx=0.80, rely=0.84,relwidth=0.13, relheight=0.05)

        self.guardar = Button( self.Nuevo_credito, text="Guardar" )
        self.guardar.config( bg='IndianRed4' )
        self.guardar.config( command=lambda: self.agregarCredito(self.txtNC.get(),self.otorgamientoNC.get(),self.vencimientoNC.get(),self.txtNC2.get()) )
        self.guardar.place( relx=0.62, rely=0.84,relwidth=0.13, relheight=0.05)  

    def calendarioOtorgamiento(self):
        #self.Nuevo_credito.withdraw()
        self.calendario=Tk() 
        #self.calendario = tk.Toplevel() 
        self.calendario.geometry("240x220")
        self.calendario.title("Fecha Otorgamiento") 
        self.center(self.calendario)
        self.date=datetime.now()
       
          
        cal = Calendar(self.calendario, selectmode = 'day',cursor="hand1", 
                       year = 2021, month = 12, 
                       day = 3) 
          
        cal.pack(pady = 2) 
          
        def grad_date(): 

                self.otorgamientoNC.set(cal.get_date())
                self.calendario.withdraw()           
                
            

        Button(self.calendario, text = "Obtener Fecha", 
                   command = grad_date).pack(pady = 2) 

    def calendarioVencimiento(self):
        #self.Nuevo_credito.withdraw()
        self.calendario=Tk() 
        #self.calendario = tk.Toplevel() 
        self.calendario.geometry("240x220")
        self.calendario.title("Fecha Vencimiento") 
        self.center(self.calendario)
          
        cal = Calendar(self.calendario, selectmode = 'day',cursor="hand1", 
                       year = 2021, month = 12, 
                       day = 3) 
          
        cal.pack(pady = 2) 
          
        def grad_date(): 

                self.vencimientoNC.set(cal.get_date())
                self.calendario.withdraw()           
                


        Button(self.calendario, text = "Obtener Fecha", 
                   command = grad_date).pack(pady = 2)    

#===========Ventana de ingresos Futuros===================================
    def ventana_ingresosFuturos(self):
        self.ventanamenu.withdraw() 
        self.ingresosFuturos = tk.Toplevel()
        self.ingresosFuturos.geometry("750x550")
        self.ingresosFuturos.title("Cuentas Bancarias")
        self.ingresosFuturos.iconbitmap("imagenes/icono.ico")
        self.ingresosFuturos.resizable(0,0)
        self.center(self.ingresosFuturos)

        self.fdep=PhotoImage(file="imagenes/fondo2.png")
        self.Fondod=Label(self.ingresosFuturos, image=self.fdep)
        self.Fondod.place(x=0, y=0)

        self.lbl1R=Label(self.ingresosFuturos, text="Ingresos Futuros")
        self.lbl1R.place(x=23, y=25,width=704, height=50)
        self.lbl1R.config(font=("Impact",25), bg="red4", fg="white")

        self.frame1 = tk.LabelFrame(self.ingresosFuturos, text="Detalles de todos los creditos aun sin cancelar ",bg="snow3",font=("Goudy old style",15))
        self.frame1.place(relx=0.1, rely=0.16, height=350, width=600)


        self.tabla = ttk.Treeview(self.frame1)
        self.tabla.place(relheight=1, relwidth=1)

        self.treescrolly = tk.Scrollbar(self.frame1, orient="vertical", command=self.tabla.yview) 
        self.treescrollx = tk.Scrollbar(self.frame1, orient="horizontal", command=self.tabla.xview) 
        self.tabla.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set) # assigna el scrollbarsen el Treeview Widget
        self.treescrollx.pack(side="bottom", fill="x") # hacer que la barra de desplazamiento llene el eje x del widget Treeview
        self.treescrolly.pack(side="right", fill="y") # hacer que la barra de desplazamiento llene el eje y del widget Treeview


        self.menur = Button( self.ingresosFuturos, text="Menú" )
        self.menur.config( bg='IndianRed4' )
        self.menur.config( command = self.atras_futuro)
        self.menur.place( relx=0.82, rely=0.84,relwidth=0.13, relheight=0.05)

        self.guardar1 = Button( self.ingresosFuturos, text="Guardar" )
        self.guardar1.config( bg='IndianRed4' )
        self.guardar1.config( command = self.guardar)
        self.guardar1.place( relx=0.65, rely=0.84,relwidth=0.13, relheight=0.05)
        self.load_futuro()
    
    def load_futuro(self,ruta="data/IngresosFuturos.txt"):
     self.Load_texto_data("Futuro",ruta)
#================ventana Plan de pagos==========================
    def ventana_planPagos(self,idCredito="000000"):

        self.Creditos.withdraw() 
        self.planPagos = tk.Toplevel()
        self.planPagos.geometry("750x600")
        self.planPagos.title("Plan de Pago")
        self.planPagos.iconbitmap("imagenes/icono.ico")
        self.planPagos.resizable(0,0)
        self.center(self.planPagos)

        self.fpp=PhotoImage(file="imagenes/fondo2.png")
        self.fplanes=Label(self.planPagos, image=self.fdep)
        self.fplanes.place(x=0, y=0)

        self.lbl1p=Label(self.planPagos, text="Plan de Pago " + str(idCredito))
        self.lbl1p.place(x=13, y=25,width=750, height=50)
        self.lbl1p.config(font=("Impact",25), bg="red4", fg="white")

        self.frame1p = tk.LabelFrame(self.planPagos, text="Detalles del plan de pago seleccionado ",bg="snow3",font=("Goudy old style",15))
        self.frame1p.place(relx=0.1, rely=0.16, height=350, width=600)


        self.tablap = ttk.Treeview(self.frame1p)
        self.tablap.place(relheight=1, relwidth=1)

        self.treescrollyp = tk.Scrollbar(self.frame1p, orient="vertical", command=self.tablap.yview) 
        self.treescrollxp = tk.Scrollbar(self.frame1p, orient="horizontal", command=self.tablap.xview) 
        self.tablap.configure(xscrollcommand=self.treescrollxp.set, yscrollcommand=self.treescrollyp.set) # assigna el scrollbarsen el Treeview Widget
        self.treescrollxp.pack(side="bottom", fill="x") # hacer que la barra de desplazamiento llene el eje x del widget Treeview
        self.treescrollyp.pack(side="right", fill="y") # hacer que la barra de desplazamiento llene el eje y del widget Treeview

        self.volver = Button( self.planPagos, text="Volver" )
        self.volver.config( bg='white' )
        self.volver.config( command = self.atras_pagos)
        self.volver.place( relx=0.85, rely=0.84,relwidth=0.13, relheight=0.07)

        self.guardar2 = Button( self.planPagos, text="Guardar" )
        self.guardar2.config( bg='white' )
        self.guardar2.config( command = self.guardar_Plan)
        self.guardar2.place( relx=0.65, rely=0.84,relwidth=0.13, relheight=0.07)

        self.load_plan()

    def load_plan(self,ruta="data/PlanPago.txt"):
     self.Load_texto_data("Plan",ruta)
#====================Funciones de Manejo de Archivos===========================================
    def guardar(self):
        
        # Llame al método askopenfilenames para obtener los nombres de archivo de varios archivos
        ruta = filedialog.asksaveasfile(title='guardar documento', filetypes=[('Archivo de texto', '*.txt')],  # Solo procesa tipos de archivos
                                       initialdir='d:/',mode='w', defaultextension=".txt")  # Directorio inicial

        if ruta is not None:

            temp = open('data/IngresosFuturos.txt', 'rb')
           
            dest = open(ruta.name, 'wb')

            shutil.copyfileobj(temp, dest)

    def guardar_Plan(self):
        
        # Llame al método askopenfilenames para obtener los nombres de archivo de varios archivos
        ruta = filedialog.asksaveasfile(title='guardar documento', filetypes=[('Archivo de texto', '*.txt')],  # Solo procesa tipos de archivos
                                       initialdir='d:/',mode='w', defaultextension=".txt")  # Directorio inicial

        if ruta is not None:

            temp = open('data/PlanPago.txt', 'rb')
           
            dest = open(ruta.name, 'wb')

            shutil.copyfileobj(temp, dest)

    def abrir(self,tipo):
        # Llame al método askopenfilename para obtener el nombre de archivo de un solo archivo
        ruta = filedialog.askopenfilename(title='Abrir', filetypes=[('Archivo de texto', '*.txt')],
                                         # Solo procesa tipos de archivos
                                         initialdir='d:/') # Directorio inicial
        if ruta != '':
            if tipo=="Creditos":

                self.load_creditos(ruta)

            if tipo=="Movimientos":

                self.load_movimientos(ruta)

            if tipo=="General":

                self.load_general(ruta)

    def buscarPlan(self,idCredito):
        creditos = open('data/CreditosBanco.txt', 'r+')
        datos = creditos.readlines()
        filtrado = []

        for i in range(1,len(datos)):

            if i != len(datos)-1:
                datos[i] = split(r"\n|,", datos[i])
                datos[i].pop(-1)
            else:
                datos[i] = split(r"\n|,", datos[i])

        for j in datos:
            
            if j[0]==idCredito:
                filtrado=j
              

        creditos.close()  

        if filtrado and filtrado[0] ==idCredito :

            fecha_dst = datetime.strptime(filtrado[2], '%m/%d/%y')
            fecha_dt = datetime.strptime(filtrado[3], '%m/%d/%y')                 
            NoPago=1
            Monto=float(filtrado[1])
            SaldoInicial = float(filtrado[1])
            SaldoFinal = float(filtrado[1])
            Capital = 0
            Intereses =0
            Plazo=float(fecha_dt.date().year  - fecha_dst.date().year)
            Tasa=round(float(filtrado[4])/100,2)
            Cuota = round(Monto/((1-(1+Tasa/12)**(-Plazo*12))/(Tasa/12)),2) 
            fecha=fecha_dst
            PlanPago="ID_Credito,NoPago,FechaPago,SaldoInicial,CapitalPagado,InteresesPagados,SaldoFinal\n"
            
            while NoPago<=Plazo*12:

                Intereses = round(SaldoInicial*Tasa/12,2)
                Capital = round(Cuota-Intereses,2)
                SaldoFinal=round(SaldoInicial-Capital,2)
                fecha=fecha+timedelta(days=30)
                while fecha.date().day !=15:
                     fecha=fecha+timedelta(days=1)



                if NoPago ==Plazo*12 and SaldoInicial<Cuota:
                    
                    SaldoFinal=0
                    PlanPago+=str(idCredito)+","+str(NoPago) + ","+str(fecha.date()).replace("-","/")+","+ str(SaldoInicial) + "," + str(Capital) + ","+str(Intereses)+","+str(0)+"\n"
                    NoPago+=1
                    SaldoInicial=round(SaldoFinal,2)
                else:


                    PlanPago+=str(idCredito)+","+str(NoPago)+ ","+str(fecha.date()).replace("-","/") + ","+ str(SaldoInicial) + "," + str(Capital) + ","+str(Intereses)+","+str(SaldoFinal)+"\n"
                    NoPago+=1
                    SaldoInicial=round(SaldoFinal,2)

           
            PlanPagoArchivo = open("data/PlanPago.txt","w")
            PlanPagoArchivo.write(PlanPago)

            PlanPagoArchivo.close()

            self.ventana_planPagos(idCredito)
        else:
            messagebox.showerror("Plan de Pago", "Id de Credito Invalido")

    def agregarCredito(self, monto, fechaOtorgamiento,fechaVencimiento, tasaInteres):
        totalf=self.totalFondos()
        disponible=totalf*0.8
        fecha_dt = datetime.strptime(fechaOtorgamiento, '%m/%d/%y')
        fecha_dst = datetime.strptime(fechaVencimiento, '%m/%d/%y') 
        if int(monto)<disponible:
            if fecha_dt.date()<fecha_dst.date():
                archivo = open('data/CreditosBanco.txt', 'a')
                NuevoId=random.randint(50000,99999)
                registro = str(NuevoId) + ',' + str(monto) + ',' + str(fechaOtorgamiento) + ',' + str(fechaVencimiento) + ',' + str(tasaInteres) + '\n' 
                archivo.write(registro)
                archivo.close()
                messagebox.showinfo("Registro de Credito", "Credito registrado con éxito.") 
            else:
                messagebox.showinfo("Registro de Credito", "Credito denegado\nLa fecha de Vencimiento debe ser mayor a la de otorgamiento")

        else:
            messagebox.showinfo("Registro de Credito", "Credito denegado\nEl monto excede el valor disponible del banco") 
#====================Funciones de historial movimieentos===========================================

    def totalFondos(self):
        archivo = open('data/CuentasBanco.txt')
        total = 0
        archivo.readline()
        for linea in archivo:
            total = total + int(linea.split(',')[5])

        archivo.close()
        return total

Sistema=BancoAzteca()
Sistema.menu()  
