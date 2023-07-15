
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