

def insert_product_in_a_ticket(product,id_ticket):
    numero_serie = product['numero_serie']
    cantidad = product['cantidad']
    values = (numero_serie, cantidad,id_ticket)
    query = "INSERT INTO `ticket_inventario`(`producto`,`cantidad_ti_inv`,`ticket_id`) VALUES (%s,%s,%s);"
    #print(values, type(values))
    return query, values