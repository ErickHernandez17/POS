
def insert(data):
    nombre = data['nombre']
    descripcion = data['descripcion']
    created_by = data['created_by']
    delete = data['delete']
    query = "INSERT INTO `catalogo_tipos` (`nombre_tipo`,`descripcion_tipo`, `created_by`, `delete`) VALUES (%s,%s,%s,%s);"
    values = (nombre, descripcion, created_by, delete)
    
    return query, values


def select_all_categories():
    query = "SELECT `id_tipo`,`nombre_tipo`,`descripcion_tipo` FROM `catalogo_tipos` WHERE `delete`='0';"
    return query


def select_category_by_name(name):
    name = f"%{name}%"
    query = "SELECT `id_tipo`,`nombre_tipo`,`descripcion_tipo` FROM `catalogo_tipos` WHERE `nombre_tipo` LIKE %s;"
    values = (name,)
    return query, values


def change_state(category_id, data):
    delete = data['delete']
    query = "UPDATE `catalogo_tipos` SET `delete` = %s WHERE (`id_tipo` = %i);"
    values = (delete, category_id)
    return query, values


def update_product(category_id, data):
    nombre = data['nombre']
    modified_date = data['modified_date']
    descripcion = data['descripcion']
    modified_by = data['modified_by']
    query = "UPDATE `catalogo_tipos` SET `nombre_tipo` = %s, `modified_date` = %s,`descripcion_tipo` = %s, `modified_by` = %s WHERE (`id_tipo` = %i);"
    values = (nombre, modified_date, descripcion, modified_by)
    return query, values
    
        