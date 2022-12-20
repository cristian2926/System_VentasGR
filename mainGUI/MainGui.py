import time
import datetime
from datetime import date
import tkinter as tk
from tkinter.ttk import Combobox
from conexion.conexion_db import conn
from util.utilidades import centrar_ventana
#============================Es un metodo para introducir barra de menu==================================
def barra_menu(ventana):
    barra_menu = tk.Menu(ventana)
    ventana.config(menu = barra_menu, width = 300, height = 300)
    menu_inicio = tk.Menu(barra_menu)
#===========================Menu de opciones Inicio=====================================================
    barra_menu.add_cascade(label='Inicio', menu= menu_inicio)
    menu_inicio.add_command(label='HOLA')
    menu_inicio.add_command(label='SALIR')

def Jframe_master():
    ventana = tk.Tk()
    ventana.title('Sistema de venta de Grifo Grupo Incapacarita')
    #ventana.iconbitmap('img/loginx.ico')
    w,h = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
    ventana.geometry("%dx%d+0+0" % (w,h))
    ventana.resizable(width=1,height=1) 
    barra_menu(ventana)
    app = master(root = ventana)
    
    app.mainloop()
    
class master(tk.Frame):
    def __init__(self, root ):
        super().__init__(root,bg = 'black',width = root.winfo_screenwidth(),height = root.winfo_screenheight())
        self.root = root
        self.pack()
        self.create_paneles()
        self.hora()
        self.fecha()
    def create_paneles(self):
#==========================Panel 1=================================================================================    
        panel_1 = tk.Frame(self,width=550,height=120, bg='pale green')
        panel_1.place(x=5,y=5)
        
        self.lbl_titulo = tk.Label(panel_1,text="GRIFO GRUPO INCAPACARITA",bg='orange3',
                                   font=("Gill Sans Ultra Bold Condensed", 28))
        self.lbl_titulo.place(x=0,y=0,width=550,height=120)
        
#============================Panel_2 HORA  y FECHA===================================================================    
        panel_2 =tk.Frame(self, height=60, bg='SkyBlue3')
        panel_2.place(x=560,y=5,relwidth=1)
        
        self.lbl_SysVentas = tk.Label(panel_2,text="VENTA DE PRODUCTOS",font=("Copperplate Gothic Bold", 17,"bold"),bg='SkyBlue3')
        self.lbl_SysVentas.place(x=80,y=15)
        #hora
        self.lbl_hora = tk.Label(panel_2,text="",font=("Tahoma",25,"bold"),fg="brown4",bg='SkyBlue3')
        self.lbl_hora.place(x=1180,y=5)
        #fecha
        self.lbl_fecha = tk.Label(panel_2,text="",font=("Courier New",20,"bold"),bg='SkyBlue3')
        self.lbl_fecha.place(x=790,y=9)

#===========================Panel_3 PRODUCTOS================================================================================
        panel_3 =tk.Frame(self, height=400, bg='gray82')
        panel_3.place(x=560,y=70,relwidth=1)
        "=================Panel diesel=============================================================================="
        self.lbl_Diesel = tk.Label(panel_3,text="DIESEL",font=("Arial",25,"bold"),fg="white",bg="gray8")
        self.lbl_Diesel.place(x=60,y=10,width=210,height=70)
        self.btn_Diesel = tk.Button(panel_3,text="B S50-UV",)
        self.btn_Diesel.config(width=10,height=1,font=("Arial",25,"bold"),fg="white",
                              bg='gray8', cursor='hand2',activebackground='gray31')
        self.btn_Diesel.place(x=60,y=80)
        self.lbl_PrecioD = tk.Label(panel_3,text="SOLES",font=("Cooper Black",15),fg="black",bg="gray82")
        self.lbl_PrecioD.place(x=60,y=160)
        self.lbl_S = tk.Label(panel_3,text="S/",font=("Cooper Black",15),fg="blue",bg="gray82")
        self.lbl_S.place(x=60,y=190)
        self.Entry_s = tk.Entry(panel_3,font=("Courier New",18,"bold"))
        self.Entry_s.place(x=110,y=190,width=120,height=30)
        self.lbl_cantidad = tk.Label(panel_3,text="CANTIDAD",font=("Cooper Black",15),fg="black",bg="gray82")
        self.lbl_cantidad.place(x=60,y=230)
        self.lbl_cant = tk.Label(panel_3,text="Glns",font=("Cooper Black",15),fg="red",bg="gray82")
        self.lbl_cant.place(x=60,y=260)
        self.Entry_cant = tk.Entry(panel_3,font=("Courier New",18,"bold"))
        self.Entry_cant.place(x=110,y=260,width=120,height=30)
        "====================Panel GASOHOL_84 plus==================================================================="
        self.lbl_84 = tk.Label(panel_3,text="GASOHOL",font=("Arial",25,"bold"),fg="white",bg="red")
        self.lbl_84.place(x=320,y=10,width=210,height=70)
        self.btn_84 = tk.Button(panel_3,text="84 PLUS",)
        self.btn_84.config(width=10,height=1,font=("Arial",25,"bold"),fg="white",
                              bg='red', cursor='hand2',activebackground='tomato')
        self.btn_84.place(x=320,y=80)
        self.lbl_Precio84 = tk.Label(panel_3,text="SOLES",font=("Cooper Black",15),fg="black",bg="gray82")
        self.lbl_Precio84.place(x=320,y=160)
        self.lbl_S84 = tk.Label(panel_3,text="S/",font=("Cooper Black",15),fg="blue",bg="gray82")
        self.lbl_S84.place(x=320,y=190)
        self.Entry_s84 = tk.Entry(panel_3,font=("Courier New",18,"bold"))
        self.Entry_s84.place(x=370,y=190,width=120,height=30)
        self.lbl_cantidad84 = tk.Label(panel_3,text="CANTIDAD",font=("Cooper Black",15),fg="black",bg="gray82")
        self.lbl_cantidad84.place(x=320,y=230)
        self.lbl_cant84 = tk.Label(panel_3,text="Glns",font=("Cooper Black",15),fg="red",bg="gray82")
        self.lbl_cant84.place(x=320,y=260)
        self.Entry_cant84 = tk.Entry(panel_3,font=("Courier New",18,"bold"))
        self.Entry_cant84.place(x=370,y=260,width=120,height=30)
        "======================Panel GASOHOL_90======================================================================"
        self.lbl_90 = tk.Label(panel_3,text="GASOHOL",font=("Arial",25,"bold"),fg="white",bg="#158645")
        self.lbl_90.place(x=570,y=10,width=210,height=70)
        self.btn_90 = tk.Button(panel_3,text="90 PLUS",)
        self.btn_90.config(width=10,height=1,font=("Arial",25,"bold"),fg="white",
                              bg='#158645', cursor='hand2',activebackground='#35BD6F')
        self.btn_90.place(x=570,y=80)
        self.lbl_Precio90 = tk.Label(panel_3,text="SOLES",font=("Cooper Black",15),fg="black",bg="gray82")
        self.lbl_Precio90.place(x=570,y=160)
        self.lbl_S90 = tk.Label(panel_3,text="S/",font=("Cooper Black",15),fg="blue",bg="gray82")
        self.lbl_S90.place(x=570,y=190)
        self.Entry_s90 = tk.Entry(panel_3,font=("Courier New",18,"bold"))
        self.Entry_s90.place(x=620,y=190,width=120,height=30)
        self.lbl_cantidad90 = tk.Label(panel_3,text="CANTIDAD",font=("Cooper Black",15),fg="black",bg="gray82")
        self.lbl_cantidad90.place(x=570,y=230)
        self.lbl_cant90 = tk.Label(panel_3,text="Glns",font=("Cooper Black",15),fg="red",bg="gray82")
        self.lbl_cant90.place(x=570,y=260)
        self.Entry_cant90 = tk.Entry(panel_3,font=("Courier New",18,"bold"))
        self.Entry_cant90.place(x=620,y=260,width=120,height=30)
        "=====================Panel GASOHOL_95====================================================================="
        self.lbl_95 = tk.Label(panel_3,text="GASOHOL",font=("Arial",25,"bold"),fg="white",bg="blue")
        self.lbl_95.place(x=820,y=10,width=210,height=70)
        self.btn_95 = tk.Button(panel_3,text="95 PLUS",)
        self.btn_95.config(width=10,height=1,font=("Arial",25,"bold"),fg="white",
                              bg='blue', cursor='hand2',activebackground='dodger blue')
        self.btn_95.place(x=820,y=80)
        self.lbl_Precio95 = tk.Label(panel_3,text="SOLES",font=("Cooper Black",15),fg="black",bg="gray82")
        self.lbl_Precio95.place(x=820,y=160)
        self.lbl_S95 = tk.Label(panel_3,text="S/",font=("Cooper Black",15),fg="blue",bg="gray82")
        self.lbl_S95.place(x=820,y=190)
        self.Entry_s95 = tk.Entry(panel_3,font=("Courier New",18,"bold"))
        self.Entry_s95.place(x=870,y=190,width=120,height=30)
        self.lbl_cantidad95 = tk.Label(panel_3,text="CANTIDAD",font=("Cooper Black",15),fg="black",bg="gray82")
        self.lbl_cantidad95.place(x=820,y=230)
        self.lbl_cant95 = tk.Label(panel_3,text="Glns",font=("Cooper Black",15),fg="red",bg="gray82")
        self.lbl_cant95.place(x=820,y=260)
        self.Entry_cant95 = tk.Entry(panel_3,font=("Courier New",18,"bold"))
        self.Entry_cant95.place(x=870,y=260,width=120,height=30)
        "====================Panel GASOHOL_97======================================================================"
        self.lbl_97 = tk.Label(panel_3,text="GASOHOL",font=("Arial",25,"bold"),fg="white",bg="gold2")
        self.lbl_97.place(x=1070,y=10,width=210,height=70)
        self.btn_97 = tk.Button(panel_3,text="97 PLUS",)
        self.btn_97.config(width=10,height=1,font=("Arial",25,"bold"),fg="white",
                              bg='gold2', cursor='hand2',activebackground='khaki1')
        self.btn_97.place(x=1070,y=80)
        self.lbl_Precio97 = tk.Label(panel_3,text="SOLES",font=("Cooper Black",15),fg="black",bg="gray82")
        self.lbl_Precio97.place(x=1070,y=160)
        self.lbl_S97 = tk.Label(panel_3,text="S/",font=("Cooper Black",15),fg="blue",bg="gray82")
        self.lbl_S97.place(x=1070,y=190)
        self.Entry_s97 = tk.Entry(panel_3,font=("Courier New",18,"bold"))
        self.Entry_s97.place(x=1120,y=190,width=120,height=30)
        self.lbl_cantidad97 = tk.Label(panel_3,text="CANTIDAD",font=("Cooper Black",15),fg="black",bg="gray82")
        self.lbl_cantidad97.place(x=1070,y=230)
        self.lbl_cant97 = tk.Label(panel_3,text="Glns",font=("Cooper Black",15),fg="red",bg="gray82")
        self.lbl_cant97.place(x=1070,y=260)
        self.Entry_cant97 = tk.Entry(panel_3,font=("Courier New",18,"bold"))
        self.Entry_cant97.place(x=1120,y=260,width=120,height=30)
#=====================================Panel_4======================================================================
        panel_4 = tk.Frame(self,width=550,height=60, bg='SkyBlue3')
        panel_4.place(x=5,y=130)
        
        self.lbl_RegistroClien = tk.Label(panel_4,text="EMITIR FACTURA",font=("Copperplate Gothic Bold", 17,"bold"),bg='SkyBlue3')
        self.lbl_RegistroClien.place(x=120,y=17)

#=======================================Panel_5 EMITIR FACTURA========================================================
        panel_5 = tk.Frame(self,width=550, bg='gray82')
        panel_5.place(x=5,y=195,relheight=1)
        
        self.lbl_NombreR = tk.Label(panel_5,text="NOMBRE o RAZON SOCIAL:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_NombreR.place(x=20,y=15)
        self.Entry_Nombre = tk.Entry(panel_5,font=("Courier New",18,"bold"))
        self.Entry_Nombre.place(x=20,y=55,width=510,height=30)
        self.lbl_DniRuc = tk.Label(panel_5,text="DNI o RUC:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_DniRuc.place(x=20,y=95)
        self.Entry_DniRuc = tk.Entry(panel_5,font=("Courier New",18,"bold"))
        self.Entry_DniRuc.place(x=20,y=135,width=510,height=30)
        self.lbl_TipoCon = tk.Label(panel_5,text="TIPO DE CONTRIBUYENTE:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_TipoCon.place(x=20,y=175)
        self.Entry_Tipocon = tk.Entry(panel_5,font=("Courier New",18,"bold"))
        self.Entry_Tipocon.place(x=20,y=215,width=510,height=30)
        self.lbl_Direccion = tk.Label(panel_5,text="DIRECCION:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_Direccion.place(x=20,y=255)
        self.Entry_Direccion = tk.Entry(panel_5,font=("Courier New",18,"bold"))
        self.Entry_Direccion.place(x=20,y=295,width=510,height=30)
        self.lbl_Subtotal = tk.Label(panel_5,text="SUBTOTAL:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_Subtotal.place(x=20,y=335)
        self.Entry_Subtotal = tk.Entry(panel_5,font=("Courier New",18,"bold"))
        self.Entry_Subtotal.place(x=20,y=375,width=510,height=30)
        self.lbl_ValorNeto = tk.Label(panel_5,text="VALOR VENTA:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_ValorNeto.place(x=20,y=415)
        self.Entry_ValorNeto = tk.Entry(panel_5,font=("Courier New",18,"bold"))
        self.Entry_ValorNeto.place(x=20,y=455,width=510,height=30)
        self.lbl_Igv = tk.Label(panel_5,text="IGV:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_Igv.place(x=20,y=495)
        self.Entry_Igv = tk.Entry(panel_5,font=("Courier New",18,"bold"))
        self.Entry_Igv.place(x=20,y=535,width=510,height=30)
        self.lbl_Total = tk.Label(panel_5,text="IMPORTE TOTAL:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_Total.place(x=20,y=575)
        self.Entry_Total = tk.Entry(panel_5,font=("Courier New",18,"bold"))
        self.Entry_Total.place(x=20,y=615,width=510,height=30)
        #======BOTONES=======
        #self.btn_Nuevo = tk.Button(panel_5,text="NUEVO")
        #self.btn_Nuevo.config(width=10,height=1,font=("Arial",17,"bold"),fg="white",
        #                      bg='#158645', cursor='hand2',activebackground='#35BD6F')
        #self.btn_Nuevo.place(x=10,y=450)
        #self.btn_Registar = tk.Button(panel_5,text="REGISTRAR")
        #self.btn_Registar.config(width=10,height=1,font=("Arial",17,"bold"),fg="white",
        #                      bg='#1658A2', cursor='hand2',activebackground='#3586DF')
        #self.btn_Registar.place(x=190,y=450)
        #self.btn_Cancelar = tk.Button(panel_5,text="CANCELAR")
        #self.btn_Cancelar.config(width=10,height=1,font=("Arial",17,"bold"),fg="white",
        #                      bg='#BD152E', cursor='hand2',activebackground='#E15370')
        #self.btn_Cancelar.place(x=370,y=450)
        
#=======================================panel_6===================================================================
        panel_6 =tk.Frame(self,width=700, height=60, bg='SkyBlue3')
        panel_6.place(x=560,y=475)
        
        self.lbl_Tfactura = tk.Label(panel_6,text="REGISTRO CLIENTES",font=("Copperplate Gothic Bold", 17,"bold"),bg='SkyBlue3')
        self.lbl_Tfactura.place(x=180,y=16)

#======================================Panel_7====================================================================
        panel_7 =tk.Frame(self, height=60, bg='SkyBlue3')
        panel_7.place(x=1265,y=475,relwidth=1)
        
        self.lbl_Tstock = tk.Label(panel_7,text="GESTION DE PRODUCTOS Y PRECIOS",font=("Copperplate Gothic Bold", 17,"bold"),bg='SkyBlue3')
        self.lbl_Tstock.place(x=90,y=16)

#=====================================Panel_8 REGISTRO CLIENTES=================================================== 
        panel_8 =tk.Frame(self,width=700, bg='gray82')
        panel_8.place(x=560,y=540,relheight=1)
        
        self.lbl_NombreR = tk.Label(panel_8,text="NOMBRE o RAZON SOCIAL:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_NombreR.place(x=60,y=20)
        self.Entry_Nombre = tk.Entry(panel_8,font=("Courier New",18,"bold"))
        self.Entry_Nombre.place(x=60,y=55,width=510,height=30,)
        self.lbl_DniRuc = tk.Label(panel_8,text="DNI o RUC:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_DniRuc.place(x=60,y=90)
        self.Entry_DniRuc = tk.Entry(panel_8,font=("Courier New",18,"bold"))
        self.Entry_DniRuc.place(x=60,y=125,width=510,height=30)
        self.lbl_TipoCon = tk.Label(panel_8,text="TIPO DE CONTRIBUYENTE:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_TipoCon.place(x=60,y=160)
        self.opciones = ["Seleccione","Persona Natural","Persona Juridica"]
        self.cmbox_Opciones = Combobox(panel_8,width=20,height=30,values=self.opciones,state="readonly")
        self.cmbox_Opciones.configure(font=("Courier New",18,"bold"))
        self.cmbox_Opciones.place(x=60,y=195)
        self.cmbox_Opciones.current(0)
        self.lbl_Direccion = tk.Label(panel_8,text="DIRECCION:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_Direccion.place(x=60,y=230)
        self.Entry_Direccion = tk.Entry(panel_8,font=("Courier New",18,"bold"))
        self.Entry_Direccion.place(x=60,y=265,width=510,height=30)
        #======BOTONES=======
        self.btn_Nuevo = tk.Button(panel_8,text="NUEVO")
        self.btn_Nuevo.config(width=14,height=1,font=("Arial",17,"bold"),fg="white",
                              bg='#158645', cursor='hand2',activebackground='#35BD6F')
        self.btn_Nuevo.place(x=20,y=350)
        self.btn_Registar = tk.Button(panel_8,text="REGISTRAR")
        self.btn_Registar.config(width=14,height=1,font=("Arial",17,"bold"),fg="white",
                              bg='#1658A2', cursor='hand2',activebackground='#3586DF')
        self.btn_Registar.place(x=248,y=350)
        self.btn_Cancelar = tk.Button(panel_8,text="CANCELAR")
        self.btn_Cancelar.config(width=14,height=1,font=("Arial",17,"bold"),fg="white",
                              bg='#BD152E', cursor='hand2',activebackground='#E15370')
        self.btn_Cancelar.place(x=475,y=350)

#=====================================Panel_9====================================================================
        panel_9 =tk.Frame(self, bg='gray82')
        panel_9.place(x=1265,y=540,relwidth=1,relheight=1)
        self.lbl_NomProd = tk.Label(panel_9,text="PRODUCTO:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_NomProd.place(x=60,y=20)
        self.Entry_NomProd = tk.Entry(panel_9,font=("Courier New",18,"bold"))
        self.Entry_NomProd.place(x=60,y=55,width=200,height=30,)
        self.lbl_Precio = tk.Label(panel_9,text="PRECIO:",font=("Britannic Bold",18,"bold"),bg='gray82')
        self.lbl_Precio.place(x=60,y=90)
        self.Entry_Precio = tk.Entry(panel_9,font=("Courier New",18,"bold"))
        self.Entry_Precio.place(x=60,y=125,width=200,height=30)   
        #======BOTONES=======
        self.btn_Nuevo = tk.Button(panel_9,text="NUEVO")
        self.btn_Nuevo.config(width=15,height=1,font=("Arial",17,"bold"),fg="white",
                              bg='#158645', cursor='hand2',activebackground='#35BD6F')
        self.btn_Nuevo.place(x=350,y=10)
        self.btn_Anadir = tk.Button(panel_9,text="AÑADIR")
        self.btn_Anadir.config(width=15,height=1,font=("Arial",17,"bold"),fg="white",
                              bg='#1658A2', cursor='hand2',activebackground='#3586DF')
        self.btn_Anadir.place(x=350,y=65)
        self.btn_Cancelar = tk.Button(panel_9,text="CANCELAR")
        self.btn_Cancelar.config(width=15,height=1,font=("Arial",17,"bold"),fg="white",
                              bg='#BD152E', cursor='hand2',activebackground='#E15370')
        self.btn_Cancelar.place(x=350,y=120)
    #def desbolitta
    def hora(self):
        now=time.strftime("%H:%M:%S")
        self.lbl_hora.configure(text=now)
        self.root.after(1000,self.hora)  
    def fecha(self):
        datetime_objet = datetime.datetime.now()
        week_day = datetime_objet.strftime("%A")
        today = date.today()
        d=today.strftime("%d /%m / %Y")
        self.lbl_fecha.configure(text=d + ' | '+ week_day)
    def registrarcon(self):
        con = conn()   
        curs = con.conexion()
        
        """data = (name, age, gender, salary,)
            query = "INSERT into USERS (name, age, gender, salary) VALUES (?, ?, ?,?)"
            curs.execute(query, data)
        #curs.execute("CREATE TABLE employees (firstname varchar(32), lastname varchar(32), title varchar(32));")
        curs.execute("INSERT INTO cliente VALUES('nombre','ruc','tipo','direccion');")
        con.commit()

        curs.execute("SELECT nombrers, dni_ruc, tipo, direccion FROM cliente;")
        for nombres, dni, tipo, direccion in curs.fetchall():
          print(nombres, dni,tipo,direccion)"""

        