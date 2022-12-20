#from mainGUI.Login import login
#login()
import tkinter as tk 
from mainGUI.Login import login
from util.utilidades import centrar_ventana
def main():
    ventana = tk.Tk()
    #ventana.overrideredirect(True)
    ventana.title('Inicio de sección')
    ventana.iconbitmap('img/loginx.ico')
    #ventana.geometry('350x400')
    ventana.resizable(width=0,height=0)
    centrar_ventana(ventana,350,400)
    
    
    app = login(root = ventana)
    
    app.mainloop()

if __name__ == '__main__':
    main()