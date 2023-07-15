

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
    query = "SELECT `numero_serie`,`nombre_producto`,`descripcion_producto`,`precio` FROM `catalogo_producto` WHERE `deleted`='0';"
    return query


def change_state(numero_serie,data):
    delete = data['delete']
    query = "UPDATE `catalogo_producto` SET `deleted` = %s WHERE (`numero_serie`=%s);"
    values = (delete, numero_serie)
    return query, values


def update_product(data):
    numero_serie = data['numero_serie']
    nombre = data['nombre']
    marca = data['marca']
    descripcion = data['descripcion']
    presentacion = data['presentacion']
    precio = data['precio']
    categoria_id = data['categoria_id']
    modified_date = data['modified_date']
    modified_by = data['modified_by']
    query = "UPDATE `catalogo_producto` SET `numero_serie`=%s, `nombre_producto`=%s, `marca`=%s,`descripcion_producto`=%s,`presentacion`=%s,`precio`=%f,`catalogo_tipos_id_tipo`=%i,`modified_date`=%s, `modified_by` = %s WHERE (`numero_serie` = %s);"
    values = (numero_serie, nombre, marca, descripcion, presentacion, precio,categoria_id,modified_date, modified_by)
    return query, values