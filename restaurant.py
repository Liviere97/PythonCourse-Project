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

#FUNCION PARA EL REGISTRO
def get_registro(conn):
    first_name = input('INGRESA TU NOMBRE:  ')
    last_name = input('INGRESA TU APELLIDO:  ')
    email = input('INGRESA TU EMAIL:  ')
    phone = int(input('INGRESA TU NUMERO DE TELEFONO:  '))
    password = input('INGRESA CONTRASEÑA:   ')
    

    sql = '''
        INSERT INTO
        usuarios (first_name, last_name, email, phone, password)
        VALUES (?, ?, ?, ?, ?)
    '''
    values = (first_name, last_name, email, phone,password)
    
    conn.execute(sql, values)
    conn.commit()

    print('REGISTRO EXITOSO')
#FUNCION PARA EL INICIO DE SESION
def get_inicio_sesion(conn):
    EMAIL = print (input('INGRESA EMAIL: '))
    CONTRASEÑA = print( input ('INGRESA PASSWORD: '))

    sql = '''
        SELECT 
            first_name, last_name, email, phone, password, timestamp
        FROM
            usuarios
        WHERE
            email = ? 
            password = ?
    '''
    values = (EMAIL , CONTRASEÑA ,)
    cursor = conn.execute(sql, values)

    data=cursor.fetchall()
    if len(data) == 0:
        print('USUARIO NO VALIDO , VE A REGISTRARTE ')
    
    #VALIDACION DE LA OPCION ELEGIDA
def validate_user_selection(selection):
    return isinstance(selection, int) and selection >0 and selection < 4

def handle_user_selection(selection, conn):
    if selection == 1:
        get_inicio_sesion(conn) 
        
    elif selection == 2:
        get_registro(conn)
    else :
        #salir_del_programa(conn)
        pass
#NUESTRO MAIN    
def main():
    getOut = 'N'
    while getOut == 'N':
        conn = create_or_get_database()
        create_table_usuario(conn)
        create_table_dish(conn)
        create_table_orden(conn) 
        print('\nMENU DE SESION ')
        print('Te presentamos el menu de opciones')
        print('1. INICIAR SESION')
        print('2. REGISTRATE')
        print('3. SALIR DE LA SESION')
        selection = int(input('¿Qué opción eliges? '))
        if validate_user_selection(selection):
            handle_user_selection(selection, conn)
            getOut = input('¿Deseas salir de la app? (S/N) ')
            while getOut != 'S' and getOut != 'N':
                print('La opcion que ingresaste no es valida')
                getOut = input('¿Deseas salir de la app? (S/N) ')
        else:
            print("VALOR INVALIDO")


main()    
    



