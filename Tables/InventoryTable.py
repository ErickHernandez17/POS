
def insert(data):
    numero_serie = data['numero_serie']
    cantidad = data['cantidad']
    created_by = data['created_by']
    delete = data['delete']
    query = "INSERT INTO `inventario` (`numero_serie`,`cantidad`, `created_by`, `deleted`) VALUES (%s,%s,%s,%s);"
    values = (numero_serie, cantidad, created_by, delete)
    return query, values


def selectt_all_inventories():
    query = "SELECT * FROM vw_show_inventory WHERE `deleted`='0';"
    return query


def change_state(numero_serie,data):
    delete = data['delete']
    query = "UPDATE `inventario` SET `deleted` = %s WHERE (`numero_serie`=%s);"
    values = (delete, numero_serie)
    return query, values


def update_a_inventory(numero_serie, data):
    numero_serie = data['numero_serie']
    cantidad = data['cantidad']
    modified_date = data['modified_date']
    modified_by = data['modified_by']
    query = "UPDATE `inventario` SET `numero_serie`=%s, `cantidad`=%i, `modified_date`=%s, `modified_by`=%s WHERE (`numero_serie`=%s);"
    values = (numero_serie, cantidad, modified_date, modified_by)
    return query, values