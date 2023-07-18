import encrypt

def validar_credenciales(password, result):
    return encrypt.verify_password(password, result[0][1])


def update_ip_count(data, ip,):
    count = int(data[4]) + 1
    user = data[0]
    query = "UPDATE usuarios SET `login_count` = %s, `ip` = %s WHERE `usuario` = %s;"
    values = (count, ip, user)
    return query, values