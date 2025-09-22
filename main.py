from flask import Flask , request , jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials , auth , firestore
from functools import wraps

app = Flask(__name__)

#cors

CORS(app)

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def verify_token(f):
    @wraps(f)
    
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error" : "Missing Token"})
        try:
            if token.startswith("Bearer"):
                token = token.split(" ")[1]
 
            decoded_token = auth.verify_id_token(token)
            request.user = decoded_token

        except Exception as e:
            return jsonify({ "error" : "Something went wrong" })
        
        return f(*args , **kwargs)
    return decorated


@app.route('/todos', methods=["GET"])
@verify_token

def get_todo():
    # print(request.user)
    userE = request.user["email"]
    todos = db.collection("users").document(userE).collection("todos").stream()
    todolist = [{  **t.to_dict() , "id" : t.id } for t in todos   ] 
    
    return jsonify(todolist)


@app.route("/todos", methods=["POST"])
@verify_token

def add_todo():
    userE = request.user["email"]
    data = request.json
    db.collection("users").document(userE).collection("todos").add({
        "title" : data["title"],
        "done" : data['done']
    })
    
    return jsonify({"message" : "task added !"})


@app.route("/todos/<id>" , methods=["PUT"])
@verify_token
def update_todo(id):
    userE = request.user["email"]
    data = request.json
    db.collection("users").document(userE).collection("todos").document(id).update({
        "done" : data["done"]
    })
    return jsonify({"message" : "task updated !"})

@app.route("/todos/<id>" , methods=["DELETE"])
@verify_token
def delete_todo(id):
    userE = request.user["email"]
    db.collection('users').document(userE).collection("todos").document(id).delete()
    return jsonify({"message" : "task deleted !"})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000 , debug=True)
