

def add_country(data):
    country = data['pais']
    query = "INSERT INTO `paises`(`nombre_pais`) VALUES(%s);"
    values = (country,)
    return query,values


def get_country():
    query = "SELECT * FROM `paises`"
    return query


def add_city(data):
    city = data['ciudad']
    id_country = int(data['id_pais'])
    query = "INSERT INTO `ciudades`(`ciudad`,`id_pais`) VALUES (%s,%s);"
    values = (city,id_country)
    return query, values


def get_cities():
    query = "SELECT * FROM `ciudades`"
    return query


def add_address(data):
    direccion = data['direccion']
    id_ciudad = int(data['id_ciudad'])
    codigo_postal = data['cp']
    query = "INSERT INTO `address`(`direccion`,`id_ciudad`,`codigo_postal`) values(%s,%s,%s);"
    values = (direccion, id_ciudad, codigo_postal)
    return query, values