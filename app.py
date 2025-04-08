from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
    return 'Welcome to upadhyay Final Test API Server'

@app.route('/host')
def host_name():
    return hostname

@app.route('/ip')
def host_ip():
    return ip_address

if __name__ == '__main__':
    app.run(host='0.0.0.0')
