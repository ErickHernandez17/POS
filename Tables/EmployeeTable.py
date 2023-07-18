

def add_employee(data):
    rfc = data['rfc']
    curp = data['curp']
    correo = data['correo']
    numero_celular = data['numero_celular']
    nombre = data['nombre']
    apellidos = data['apellidos']
    id_address = int(data['id_address'])
    id_usuario = int(data['id_usuario'])
    query = "INSERT INTO `empleados`(`RFC`,`CURP`,`correo`,`numero_celular`,`nombre`,`apellidos`,`id_address`,`id_usuario`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
    values = (rfc, curp, correo, numero_celular, nombre, apellidos, id_address, id_usuario)
    return query, values