from flask import Flask, jsonify, request
import Tables.CategoryTable as categoryTable
import Tables.ProductTable as productTable
import Tables.InventoryTable as inventoryTable
import Tables.UsersTable as usersTable
import Tables.TicketsTable as ticketTable
import Tables.AddressTables as addressTables
import Tables.EmployeeTable as employeeTable
import get_ip
from SQL import ConnectionToMySQL as sql

app = Flask(__name__)

conexion = sql.MySQLConnectorMaster()
BADMETHOD = {"message":"Metodo no permitido"}    
   
   
"""
======================== ENDPOINTTS OF THE EXISTENCES ========================
"""
   
   
#CATEGORY
    
    
@app.route("/categories", methods=['POST'])
def add_category():
    if request.method == 'POST':
        data = request.json
        sSQL, values = categoryTable.insert(data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message": "Categoria agregada exitosamente"}
            return jsonify(response)
        except Exception as e:
            return f"Error al agregar la categoria: {str(e)}"
    else:
        return jsonify(BADMETHOD), 405


@app.route('/categories', methods=['GET'])
def get_categories():
    if request.method == 'GET':
        sSQL =  categoryTable.select_all_categories()
        try:
            conexion.connect()
            result = conexion.execute_select_withoutt_values(sSQL)
            conexion.disconnect()
            return jsonify({"response": result})
        except Exception as e:
            return f'Error al obtener las categorias: {str(e)}'
    else:
        return jsonify(BADMETHOD),405


@app.route('/categories/<name>', methods=['GET'])
def get_category_by_name(name):
    if request.method == 'GET':
        sSQL, values =  categoryTable.select_category_by_name(name)
        try:
            conexion.connect()
            result = conexion.execute_select_with_values(sSQL, values)
            conexion.disconnect()
            return jsonify({"response":result})
        except Exception as e:
            return f'Error al obtener la categoria: {str(e)}'
    else:
        return jsonify(BADMETHOD),405


@app.route('/categories/<category_id>', methods=['PATCH'])
def change_state_of_a_category(category_id):
    if request.method == 'PATCH':
        data = request.json
        sSQL, values = categoryTable.change_state(category_id,data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect
            response = {"message":"Estado de la categoria cambiada exitosamente"}
            return jsonify(response)
        except Exception as e:
            return f'Error al cambiar el estado de la categoria: {str(e)}'
    else:
        return jsonify(BADMETHOD),405
    
    
@app.route('/categories/<category_id>', methods=['PUT'])
def update_category(category_id):
    if request.method == 'PUT':
        data = request.json
        sSQL, values = categoryTable.update_product(category_id,data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message": "Categoria actualizada exitasamente"}
            return jsonify(response)
        except Exception as e:
            return f"Error al actualizar la cattegoria: {str(e)}"
    else:
        return jsonify(BADMETHOD), 405


#PRODUCTS


@app.route('/products',methods=['POST'])
def add_product():
    if request.method == 'POST':
        data = request.json
        sSQL, values = productTable.insert(data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message":"Producto agregado exitosamente"} 
            return response
        except Exception as e:   
            return f'Error al agregar el producto: {str(e)}'
    else:
        return jsonify(BADMETHOD),405
    

@app.route('/products', methods=['GET'])
def get_products():
    if request.method == 'GET':
        sSQL=  productTable.select_all_products()
        try:
            conexion.connect()
            result = conexion.execute_select_withoutt_values(sSQL)
            conexion.disconnect()
            return jsonify({"response": result})
        except Exception as e:
            return f'Error al obtener las categorias: {str(e)}'
    else:
        return jsonify(BADMETHOD),405


@app.route('/products/<name>', methods=['GET'])
def get_product_by_name(name):
    if request.method == 'GET':
        try:
            conexion.connect()
            result = conexion.execute_procedure('obtener_producto_por_nombre',name)
            conexion.disconnect()
            return jsonify({"response":result})
        except Exception as e:
            return f"Error al obtner el producto: {str(e)}"
    else:
        return jsonify(BADMETHOD),405


@app.route('/products/<numero_serie>', methods=['PATCH'])
def change_state_of_a_product(numero_serie):
    if request.method == 'PATCH':
        data = request.json
        sSQL, values = productTable.change_state(numero_serie, data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            return jsonify({"message":"Estado del producto cambiado exittosamente"})
        except Exception as e:
            return f"Error al cambiar el estado del producto {str(e)}"
    else:
        return jsonify(BADMETHOD),405
    
    
@app.route('/products/<numero_serie>/update', methods=['PUT'])
def update_product(numero_serie):
    if request.method == 'PUT':
        data = request.json
        sSQL, values = productTable.update_product(numero_serie,data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message": "Producto actualizada exitasamente"}
            return jsonify(response)
        except Exception as e:
            return f"Error al actualizar el producto: {str(e)}"
    else:
        return jsonify(BADMETHOD), 405


#INVENTORY


@app.route('/inventory', methods=['POST'])
def add_inventory():
    if request.method == 'POST':
        data = request.json
        sSQL, values = inventoryTable.insert(data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message":"Inventario agregado exitosamente"}
            return jsonify(response)
        except Exception as e:
            return f"Error al agregar el inventario: {str(e)}"
    else:
        return jsonify(BADMETHOD),405


@app.route('/inventory',methods=['GET'])
def get_inventories():
    if request.method == 'GET':
        sSQL = inventoryTable.selectt_all_inventories()
        try:
            conexion.connect()
            result =  conexion.execute_select_withoutt_values(sSQL)
            conexion.disconnect()
            return jsonify({"response":result})
        except Exception as e:
            return f"Error al obtener el inventario: {str(e)}"
    else:
        return jsonify(BADMETHOD),405


@app.route('/inventory/<name>', methods=['GET'])
def get_inventory_by_name(name):
    if request.method == 'GET':
        try:
            conexion.connect()
            result = conexion.execute_procedure('obtener_inventario_por_nombre',name)
            conexion.disconnect()
            return jsonify({'response': result})
        except Exception as e:
            return f"Error al obtener el inventario: {str(e)}"
    else:
        return jsonify(BADMETHOD),405


@app.route('/inventory/<numero_serie>', methods=['PATCH'])
def change_state_of_a_inventory(numero_serie):
    if request.method == 'PATCH':
        data = request.json
        sSQL, values = inventoryTable.change_state(numero_serie, data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message":"Estado del inventario cambiado exitosamente"}
            return response
        except Exception as e:
            return f"Error al cambiar el estado del inventario: {str(e)}"
    else:
        return jsonify(BADMETHOD),405
    
    
@app.route('/inventory/<id_inventory>/update', methods=['PUT'])
def update_inventory(id_inventory):
    if request.method == 'PUT':
        data = request.json
        sSQL, values = inventoryTable.update_a_inventory(id_inventory, data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message":"Cambios realizados al inventario exitosamente"}
            return jsonify(response)
        except Exception as e:
            return f"Error al actualizar el inventario: {str(e)}"
    else:
        return jsonify(BADMETHOD), 405
    
    
"""
======================== ENDPOINT TO LOGIN ========================
"""


@app.route('/login', methods=['GET'])
def get_user_password():
    if request.method == 'GET':
        data = request.json
        user = data['user']
        password = data['password']
        ip = get_ip.get_host_ip()
        try:
            conexion.connect()
            result = conexion.execute_procedure("obtener_informacion_usuario", user)
            validacion = usersTable.validar_credenciales(password, result)
            if validacion:
                try:
                    """
                    Si pudimos iniciar sesion de manera exitosa entonce obtenemos la ip del equipo y hacemos las
                    actualizaciones necesarias en la base de datos
                    """
                    sSQL, values = usersTable.update_ip_count(result[0],ip)
                    conexion.execute_post(sSQL, values)
                    conexion.disconnect()
                except Exception as e:
                    return f"Error al actualizar la ip {str(e)}"
                response = {"RFC":result[0][2],"privilage":result[0][3],"count":result[0][4],"ip":result[0][5]}
                return jsonify(response)
            else:
                return "Credenciales invalidas"
        except Exception as e:
            return f"Error al obtener informacion de usuario {str(e)}"
    else:
        return jsonify(BADMETHOD),405


@app.route('/sell', methods=['POST'])
def sell_products():
    if request.method == 'POST':
        data = request.json
        rfc = data['rfc']
        fecha = data['fecha']
        products = data['productos']
        try:
            conexion.connect()
            id_ticket = conexion.execute_procedure("create_new_ticket", rfc, fecha)
            if id_ticket != None:
                for product in products:
                    sSQL, values = ticketTable.insert_product_in_a_ticket(product, id_ticket[0][0])
                    conexion.execute_post(sSQL, values)       
            response = {"ticket id":id_ticket[0][0],"fecha":fecha}
            tmp = []
            for product in products:
                sSQL, values = productTable.get_price(product['numero_serie'])
                result = conexion.execute_select_with_values(sSQL, values)
                total = float(result[0][1])* int(product['cantidad'])
                tmp.append({"Producto":result[0][0], "Cantidad":product['cantidad'], "$$$":total})
            response['productos'] = tmp
            conexion.disconnect()
            return jsonify(response)
        except Exception as e:
            return f"Error al realizar la venta: {str(e)}"
    else:
        return jsonify(BADMETHOD), 405


@app.route('/add-country', methods=['POST'])
def add_country():
    if request.method == 'POST':
        data = request.json
        sSQL, values = addressTables.add_country(data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message":"Pais agregado exitosamente"}
            return jsonify(response)
        except Exception as e:
            return f"Erro al agregar el pais {str(e)}"
    else:
        return jsonify(BADMETHOD),405


@app.route('/add-city',methods=['POST'])
def add_city():
    if request.method == 'POST':
        data= request.json
        sSQL, values = addressTables.add_city(data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message":"Ciudad agregada exitosamente"}
            return jsonify(response)
        except Exception as e:
            return f"Error al agregar la ciudad {str(e)}"
    else:
        return jsonify(BADMETHOD),405
    
    
@app.route('/add-address',methods=['POST'])
def add_address():
    if request.method == 'POST':
        data = request.json
        sSQL, values = addressTables.add_address(data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message":"Direccion agregado exitosamente"}
            return jsonify(response)
        except Exception as e:
            return f"Error al agregar la direccion {str(e)}"
    else:
        return jsonify(BADMETHOD),405
    
    
@app.route('/add-username', methods=['POST'])
def add_username():
    if request.method == 'POST':
        data = request.json
        sSQL, values =  usersTable.add_username(data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message":"Usuario agregado exitosamente"}
            return jsonify(response)
        except Exception as e:
            return f"Erro al agregar el usuario {str(e)}"
    else:
        return jsonify(BADMETHOD),405
    
    
@app.route('/add-employee', methods=['POST'])
def add_employee():
    if request.method == 'POST':
        data = request.json
        sSQL, values = employeeTable.add_employee(data)
        try:
            conexion.connect()
            conexion.execute_post(sSQL, values)
            conexion.disconnect()
            response = {"message":"Empleado agregado exitosamente"}
            return jsonify(response)
        except Exception as e:
            return f"Error al agregar el empleado {str(e)}"
    else:
        return jsonify(BADMETHOD),405


if __name__ == "__main__":
    app.run()