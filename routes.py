from app import app
from flask import redirect,request,jsonify
import os 
from app import config
import urllib.parse
import urllib.request
import json

@app.route('/')
@app.route('/index')
def index():
    client_id = os.getenv('CLIENT_ID')
    redirect_uri = os.getenv('REDIRECT_URI')
    url = f"http://auth.mercadolibre.com.mx/authorization?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
    req = urllib.request.Request(url)
    f = urllib.request.urlopen(req) 
    the_page = f.geturl()
    return redirect(str(the_page), code=302)

@app.route('/user')
def show_user_profile():
    number_code = request.args.get("code")
    url = "https://api.mercadolibre.com/oauth/token"
    data = {
            'grant_type':'authorization_code', 
            'client_id': os.getenv('CLIENT_ID'), 
            'client_secret': os.getenv('CLIENT_SECRET'), 
            'code':number_code, 
            'redirect_uri': os.getenv('REDIRECT_URI')
    }
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    json_data = json.dumps(data)    
    json_data_bytes = json_data.encode('utf-8')
    req.add_header('Content-Length', len(json_data_bytes))
    response = urllib.request.urlopen(req, json_data_bytes)
    decode_response = response.read().decode()
    return jsonify(decode_response) 
