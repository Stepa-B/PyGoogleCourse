import requests
import socket
def check_localhost(host):
        host = socket.gethostbyname(host)
        return host>""
def check_connectivity(url):
        request = requests.get(url)
        return request.status_code == 200
print(check_localhost('localhost'))
print(check_connectivity("http://www.google.com"))