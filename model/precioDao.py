from conexion.conexion_db import conexionDB

class precioDao:
    def __init__(self,nombre,pu):
        self.id_producto = None
        self.nombre = nombre
        self.pu = pu
        
    def __str__(self):
        return f'producto[{self.nombre},{self.pu}]'
    
def guardarP(precioDao):
    conexion = conexionDB().conexion
    #conexion.cursor.execute("SELECT * FROM cliente")
    sql = f"""INSERT INTO producto (nombre, pu)
    VALUES('{precioDao.nombre}','{precioDao.pu}')"""
    conexion.execute(sql)
    conexion.commit()
    conexion.close()
def get_precio():
    conexion = conexionDB().conexion
    #conexion.cursor.execute("SELECT * FROM cliente")
    sql = f"""SELECT * FROM producto"""
    rs = conexion.execute(sql)
    return rs
    """for record in rs:
        print ('ID : '+str(record[0]))"""
def listar_producto():
    conexion = conexionDB().conexion
    listar_produc = []
    sql = f"""SELECT * FROM producto"""
    
    try:
        conexion.execute(sql)
        listar_produc =conexion.execute(sql).fetchall()
        conexion.commit()
        conexion.close()
    except:
        pass
    return listar_produc
def editar_prod(precio,id_producto):
    conexion = conexionDB().conexion
    sql = f"""UPDATE producto
    SET nombre = '{precio.nombre}', pu = {precio.pu}
    WHERE id_producto = {id_producto} """
    try:
        conexion.execute(sql)
        
        conexion.commit()
        conexion.close()
    except:
        pass

def delete_prod(id_producto):
    conexion = conexionDB().conexion
    sql = f'DELETE FROM producto WHERE id_producto = {id_producto}'
    try:
        conexion.execute(sql)
        
        conexion.commit()
        conexion.close()
    except:
        pass
    