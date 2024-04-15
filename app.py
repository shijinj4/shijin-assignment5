from flask import Flask
import socket
 
app = Flask(__name__)
 
 
hostname = socket.gethostname()
try:
    ip_address = socket.gethostbyname(hostname)
except socket.gaierror:
    ip_address = 'Unable to resolve IP'
 
@app.route('/')
def hello_cloud():
  return "Hello from Kiran Sajan -new ECS Container"
 
@app.route('/host')
def host_name():
  return hostname
 
@app.route('/ip')
def host_ip():
  return ip_address
 
app.run(host='0.0.0.0')
