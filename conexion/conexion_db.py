#from __future__ import print_function
#from sqlite3 import connect
import sqlite3
# Replace username with your own A2 Hosting account username:

class conexionDB:
    global base_datos
    global conexion
    base_datos = ""
    def __init__(self):
        self.base_datos = "data/tabla.db"
        self.conexion = sqlite3.connect(self.base_datos)
        #self.cursor = self.conexion.cursor()
        
        
    
        
        