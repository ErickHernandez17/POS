from mysql.connector import connect as conn
from mysql.connector import Error as error


class MySQLConnectorMaster:
    
    
    def __init__(self):
        self._host = "localhost"
        self._user = "root"
        self._password = "Yale101122."
        self._database = "zyzzplementsdb"
        self._connection = None


    def connect(self):
        try:
            self._connection = conn(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
            if self._connection.is_connected():
                pass
        except error as err:
            return {"Codigo de estado": 100, "Contexto": "No hay conexion a la base de datos", "Tipo de error": err}


    def disconnect(self):
        if self._connection.is_connected():
            self._connection.close()
        return {"Codigo de estado": 200}


    def execute_post(self, sSQL, values):
        try:
            cursor = self._connection.cursor()
            cursor.execute(sSQL, values)
            self._connection.commit()
        except error as err:
            return {"Error en funcion execute_post": str(err)}


    def execute_select_withoutt_values(self, sSQL):
        try:
            cursor = self._connection.cursor()
            cursor.execute(sSQL)
            result = cursor.fetchall()
            return result
        except error as err:
            print(f"Error al ejecutar la consulta:\n{err}")


    def execute_select_with_values(self, sSQL, values):
        try:
            cursor = self._connection.cursor()
            cursor.execute(sSQL, values)
            result = cursor.fetchall()
            return result
        except error as err:
            print(f"Error al ejecutar la consulta:\n{err}")


    def execute_procedure(self, procedure_name, *args):
        cursor = self._connection.cursor()
        try:

            cursor.callproc(procedure_name, args=args)
            for result in cursor.stored_results():
                resultados = result.fetchall()
            cursor.close()
            return resultados
        except error as err:
            return {"Codigo de estados": 102, "Contexto": "Error al ejecutar el procedimiento", "Tipo de error": err}


    def execute_function(self, function_name, *args):
        cursor = self._connection.cursor()
        try:
            placeholders = ','.join(['%s'] * len(args))
            query = f"SELECT {function_name}({placeholders})"
            cursor.execute(query, args)
            result = cursor.fetchone()
            cursor.close()
            return result[0]
        except error as err:
            print(f"Error al llamar la función: {str(err)}")


