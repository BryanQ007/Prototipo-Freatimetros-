from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask Api - Pruebas"

    
@app.route('/user')
def allUser():
    return({
        
        'id': '001', 
        'name':'user',
        'birthday':'20-06-1994'        
    })
    
@app.route('/admin')
def showAdmin():
    data = {
        "id": "000",
        "name": "admin",
        "birthday": "20-06-1995"        
    }

    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:8080")
    return response  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
            
   
    