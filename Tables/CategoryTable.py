
def insert_category(data):
    nombre = data['nombre']
    descripcion = data['descripcion']
    created_by = data['created_by']
    delete = data['delete']
    query = "INSERT INTO `catalogo_tipos` (`nombre_tipo`,`descripcion_tipo`, `created_by`, `delete`) VALUES (%s,%s,%s,%s);"
    values = (nombre, descripcion, created_by, delete)
    
    return query, values


def select_all_categories():
    query = "SELECT `id_tipo`,`nombre_tipo`,`descripcion_tipo` FROM `catalogo_tipos` WHERE `delete`=%s;"
    values = ('0')
    return query, values