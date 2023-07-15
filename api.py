from flask import Flask, jsonify, request
import Tables.CategoryTable as categoryTable
import Tables.ProductTable as productTable
import Tables.InventoryTable as inventoryTable
from SQL import ConnectionToMySQL as sql

app = Flask(__name__)

conexion = sql.MySQLConnector()
BADMETHOD = {"message":"Metodo no permitido"}    
    
@app.route("/categories", methods=['POST'])
def add_category():
    if request.method == 'POST':
        data = request.json
        sSQL, values = categoryTable.insert_category(data)
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
        pass
    else:
        return jsonify(BADMETHOD),405



@app.route('/products',methods=['POST'])
def add_product():
    if request.method == 'POST':
        data = request.json
        sSQL, values = productTable(data)
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


@app.route('/inventory', methods=['POST'])
def add_inventory():
    if request.method == 'POST':
        data = request.json
        sSQL, values = inventoryTable(data)
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





if __name__ == "__main__":
    app.run()