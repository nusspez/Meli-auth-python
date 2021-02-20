from flask import Flask,redirect,request,jsonify,render_template
import os
import urllib.parse
import urllib.request
import json

os.environ['CLIENT_ID'] = '7322743982300021'
os.environ['CLIENT_SECRET'] = 'ovxdNELVxYexN388ULyM8ViGOA7rCk8s'
os.environ['REDIRECT_URI'] = 'https://fathomless-taiga-09672.herokuapp.com/user'

app = Flask(__name__)
PORT = 5000
DEBUG = True

@app.route('/')
@app.route('/index', methods=["GET", "POST"])
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

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            return 'cuaxk'
    return render_template("home.html")


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)