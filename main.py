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
    except Exception as e:
        print(f'Error al conectar: {e}')
        return None

def agregar_tareas(titulo):
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tareas (titulo) VALUES(?)", titulo)
        cursor.commit()
        cursor.close()
        print('¡Tarea guardada en SQL Server con éxito!')
    else:
        conexion.rollback()
        return "Hubo un problema"

def ver_tareas():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tareas")

        filas = cursor.fetchall()
        for fila in filas:
            estado = "Completada" if fila[2] == 1 else "Pendiente"
            print(f"ID: {fila[0]} | Titulo: {fila[1]} | Estado: {estado}")
    else:
        conexion.rollback()
        return "Hubo un problema"