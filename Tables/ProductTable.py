

def insert(data):
    numero_serie = data['numero_serie']
    nombre = data['nombre']
    marca = data['marca']
    presentacion = data['presentacion']
    descripcion = data['descripcion']
    precio = data['presentacion']
    id_categoria = data['id_categoria']
    created_by = data['created_by']
    delete = data['delete']
    
    query = "INSERT INTO `catalogo_producto`(`numero_serie`, `presentacion`, `marca`, `nombre_producto`, `descripcion_producto`, `catalogo_tipos_id_tipo`, `precio`, `created_by`, `deleted`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    values = (numero_serie, presentacion, marca, nombre, descripcion, id_categoria, precio, created_by, delete)
    return query, values


def select_all_products():
    query = "SELECT `numero_Serie`,`nombre_producto`,`descripcion_producto`,`precio` FROM `catalogo_producto` WHERE `deleted`='0';"
    return query