import socket
def get_host_ip():
    hostname = socket.gethostname()
    _,_,ip_address = socket.gethostbyname_ex(hostname)
    return ip_address[-1]


