import pymysql
import googlemaps
import geocoder
from datetime import datetime


try:
	conexion = pymysql.connect(host='localhost',
	                            user='root',
	                            password='12345',
	                            db='usuarios')
	print("Contectado")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Error de conexión: ", e)
cursor = db.cursor()

#Método POST
def create(self):
	sql = "INSERT INTO usuarios(id, nombre, apellido, direccion, ciudad, longitud, latitud, estadogeo) \
	   VALUES (NULL,'{nombre1}','{apellido1}','{direccion1}','{ciudad1}')"
	try:
	   cursor.execute(sql)
	   db.commit()
	except:
	   db.rollback()
#Método GETLIST
def getList(self):
	sql = "SELECT * FROM usuarios"
	try:
	   cursor.execute(sql)
	   db.commit()
	except:
	   db.rollback()
#Método GETUSERS
def getUsers(self, id):
	sql = "SELECT * FROM usuarios WHERE id ='id'"
	try:
	   cursor.execute(sql)
	   db.commit()
	except:
	   db.rollback()

#Método Delete
def delete(self, id):
	sql = "DELETE FROM usuarios WHERE id ='id'"
	try:
	   cursor.execute(sql)
	   db.commit()
	except:
	   db.rollback()

def obtenerCoordenadas(location):
    return location_lat, location_long
#Método getGoogle
def getGoogle(self):

	obtenerCiudad = "SELECT ciudad FROM usuarios WHERE longitud is NULL AND latitud is NULL"
	obtenerDireccion = "SELECT direccion FROM usuarios WHERE longitud is NULL AND latitud is NULL"
	try:
	   cursor.execute(obtenerCiudad)
	   cursor.execute(obtenerDireccion)
	   db.commit()
	except:
	   db.rollback()

	gmaps = googlemaps.Client(key='AlzaSyAyTyGuBvUitD_Qs_MzAtWfjctn5UkQ2lo')

	geocode_result = gmaps.geocode('obtenerCiudad','obtenerDireccion')

	loc_lat, loc_long = obtenerCoordenadas(location=location) 

	#actualizar = "ALTER TABLE usuarios..."



db.close()