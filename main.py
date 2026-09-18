import pyodbc

SERVER = 'localhost'
DATABASE = 'GestorTareas'

conexion_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'Trusted_Connection=yes;'
)

def conectar_db():
    try:
        conexion = pyodbc.connect(conexion_str)
        return conexion
    except:
        print(f'Error al conectar')
        return None

def agregar_tareas():
    conexion = conectar_db()
    titulo = input("Ingrese el titulo de la tarea: ")
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tareas (titulo) VALUES(?)", titulo)
        cursor.commit()
        cursor.close()
        print('\n¡Tarea guardada en SQL Server con éxito!')
    except:
        conexion.rollback()
        print("Hubo un error, se han revertido los cambios")

def ver_tareas():
    conexion = conectar_db()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tareas")

        filas = cursor.fetchall()
        for fila in filas:
            estado = "Completada" if fila[2] == 1 else "Pendiente"
            print(f"ID: {fila[0]} | Titulo: {fila[1]} | Estado: {estado}")
    except:
        conexion.rollback()
        print("\nHubo un error, se han revertido los cambios")

def menu():
    while True:
        opcion = input("\n1. Agregar tareas\n" \
                    "2. Ver Tareas\n" \
                    "3. Salir\n" \
                    "Elige una opcion: ")
        
        if opcion == "1":
            agregar_tareas()
        elif opcion == "2":
            ver_tareas()
        else:
            break


menu()