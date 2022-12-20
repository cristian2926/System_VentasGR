from conexion.conexion_db import conexionDB

class clienteDao:
    def __init__(self,nombre,dni,tipo,direccion):
        self.nombre = nombre
        self.dni = dni
        self.tipo = tipo
        self.direccion = direccion
    def __str__(self):
        return f'cliente[{self.nombre},{self.dni},{self.tipo},{self.direccion}]'
def guardar(clienteDao):
    conexion = conexionDB().conexion
    #conexion.cursor.execute("SELECT * FROM cliente")
    sql = f"""INSERT INTO cliente (nombrers, dni_ruc, tipo, direccion)
    VALUES('{clienteDao.nombre}','{clienteDao.dni}','{clienteDao.tipo}','{clienteDao.direccion}')"""
    conexion.execute(sql)
    conexion.commit()
    conexion.close()
    #conexion.cursor.fetchall
    
    
"""def Crear_Tabla1():
    conexion = conexionDB()
    sql = '''
    CREATE TABLE cliente(
        nombre VARCHAR(100),
        dni VARCHAR(100),
        tipo VARCHAR(100),
        direccion VARCHAR(100),
        PRIMARY KEY(nombre)    
    )'''
    conexion.cursor.execute(sql)
    conexion.cerrar()"""    