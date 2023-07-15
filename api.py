from flask import Flask, jsonify, request
import Tables.CategoryTable as categoryTable
import Tables.ProductTable as productTable
import Tables.InventoryTable as inventoryTable
from SQL import ConnectionToMySQL as sql

app = Flask(__name__)

conexion = sql.MySQLConnectorMaster()
BADMETHOD = {"message":"Metodo no permitido"}    
   
   
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
            result = conexion.execute_select(sSQL)
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


@app.route('/categories/<category_id>/state', methods=['PATCH'])
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
    
    
@app.route('/categories/<category_id>/update', methods=['PUT'])
def update_category(category_id):
    if request.method == 'PUT':
        data = request.json
        sSQL, values = categoryTable.update_product(data)
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
            result = conexion.execute_select(sSQL)
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
        sSQL, values = productTable.change_state(numero_serie)
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

if __name__ == "__main__":
    app.run()