import tkinter as tk

from util.utilidades import centrar_ventana
from mainGUI.MainGui import Jframe_master
class login(tk.Frame):
    
    def __init__(self, root ):
        super().__init__(root,bg = 'gray92',width = 350,height = 400)
        self.root = root
        self.pack()
        self.inicio_logion()
        
    def inicio_logion(self):
        #================================Etiqueta para inicio seccion=======================================
        self.usuario = tk.Label(self,text = "INICIAR SECCION ", bg= 'black' , font=("Arial black", 20), fg= "white")
        self.usuario.place(x = 0, y = 0, width = 350, height = 65)
        
        # ===============================etiqueta para imagen de usuario====================================
        self.image_user = tk.PhotoImage(file = 'img/usser.png')
        self.lbl_imge = tk.Label(image = self.image_user)
        self.lbl_imge.place(x = 40, y = 100)
        
        #================================Etiqueta para imagen de contraseña=================================
        self.image_passw = tk.PhotoImage(file = 'img/passw.png')
        self.lbl_passw = tk.Label(image = self.image_passw)
        self.lbl_passw.place(x = 40, y = 200)
        
        #================================Campos de usuario y contraseña=====================================
        self.Entry_usuariox = tk.Entry(self,bg= 'white' , font=("Constantia", 17), fg= "black")
        self.Entry_usuariox.place(x = 120 , y = 110, width = 180, height = 40)
        
        self.Entry_passwx = tk.Entry(self,bg= 'white' , font=("Constantia", 17), fg= "black",show="*")
        self.Entry_passwx.place(x = 120 , y = 210, width = 180, height = 40)

        #==============================crear botones Ingresar y salir======================================
        self.btn_Ingresar = tk.Button(self,text = "INGRESAR",bg= 'black' , font=("Arial black", 15), fg= "white",
                                      command = self.verificar)
        self.btn_Ingresar.place(x = 43 , y = 270, width = 260, height = 40)
        
        self.btn_cerrar = tk.Button(self,text = "CERRAR",bg= 'black' , font=("Arial black", 15), fg= "white")
        self.btn_cerrar.place(x = 43 , y = 320, width = 260, height = 40)
    
    def verificar(self):
        ussuer= self.Entry_usuariox.get()
        password =self.Entry_passwx.get()
        if (ussuer=="ubnt" and password=="ubnt"):
            self.root.destroy()
            Jframe_master()
        else:
            pass