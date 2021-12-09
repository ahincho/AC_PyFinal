
# Script para obtener la conexion e informacion de la Base de Datos

import mysql.connector as db

import json

# Establecer conexion con la Base de Datos

with open('keys.json') as json_file:
    keys = json.load(json_file)

# Convertir el archivo a un formato binario

def convertToBinaryData(filename):
    try:
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    except:
        return 0

# Metodo para escribir datos en una ruta especificada

def writeFile(data, path):
    # Convertir los datos a binario y escribirlo en nuestro archivo
    with open(path, 'wb') as file:
        file.write(data)

# Metodo para Registrar un Usuario con su Foto en la Base de Datos

def registerUser(name, photo):
    # Variables auxiliar para el ID del Usuario y si esta registro en la Base de Datos
    id = 0
    inserted = 0
    
    try:
        con = db.connect(host = keys["host"], user = keys["user"], password = keys["password"], database = keys["database"])
        cursor = con.cursor()
        sql = "INSERT INTO `user`(name, photo) VALUES (%s,%s)"
        pic = convertToBinaryData(photo)
        if pic:
            cursor.execute(sql, (name, pic))
            con.commit()
            inserted = cursor.rowcount
            id = cursor.lastrowid
        
    except db.Error as e:
        print(f"Failed inserting image: {e}")
    
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
    
    return {"id": id, "affected":inserted}

# Metodo para Buscar y obtener las Keys de un Usuario con su Foto en la Base de Datos

def getUser(name, path):
    # Variables auxiliar para el ID del Usuario y recuperar su Foto de la Base de Datos
    id = 0
    rows = 0

    try:
        con = db.connect(host = keys["host"], user = keys["user"], password = keys["password"], database = keys["database"])
        cursor = con.cursor()
        sql = "SELECT * FROM `user` WHERE name = %s"

        cursor.execute(sql, (name,))
        records = cursor.fetchall()

        for row in records:
            id = row[0]
            writeFile(row[2], path)
        rows = len(records)

    except db.Error as e:
        print(f"Failed to read image: {e}")

    finally:
        if con.is_connected():
            cursor.close()
            con.close()
    
    return {"id": id, "affected": rows}
