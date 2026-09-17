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

