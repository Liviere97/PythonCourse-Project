import sqlite3
import os
#CREAMOS LA BASE DE DATOS
def create_or_get_database():
    conn = sqlite3.connect('restaurant.db')
    print("Database connected")
    return conn
#CREAREMOS LAS TABLAS
#TABLA USUARIO
def create_table_usuario(conn):
    sql = '''
        CREATE TABLE IF NOT EXISTS usuarios (
            first_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            phone INT NOT NULL,
            password VARCHAR,
            logged INT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    '''
    conn.execute(sql)
    print("the table user  has been created succesfully")  
#tabla dish    
def create_table_dish(conn):
    sql = '''
        CREATE TABLE IF NOT EXISTS dish (
            name VARCHAR NOT NULL,
            description VARCHAR NOT NULL,
            price DOUBLE NOT NULL,
            ingredients TEXT,
            preparation_time DOUBLE NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
    conn.execute(sql)
    print("the table dish has been created succesfully")
#TABLA ORDER
def create_table_orden(conn):
    sql = '''
        CREATE TABLE IF NOT EXISTS orden (
            notes VARCHAR NOT NULL,
            preparatontime DOUBLE NOT NULL,
            total_price DOUBLE NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
    conn.execute(sql)
    print("the tables orden has been created succesfully")

def main():
        conn = create_or_get_database()
        create_table_usuario(conn)
        create_table_dish(conn)
        create_table_orden(conn)       
main()    
    





