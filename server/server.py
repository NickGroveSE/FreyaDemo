from flask import Flask, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import string

# app instance 
app = Flask(__name__)
CORS(app)

# firebase configuration
cred = credentials.Certificate(r"C:\Users\Nick\Desktop\FreyaDemo\server\freya-initial-build-firebase-adminsdk-2wt6c-30291df0e9.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/api/products", methods=["GET"])
def get_products():

    docs = db.collection('items').stream()

    doc_ref = db.collection('items').document()
    doc = doc_ref.get()

    # if doc.exists:
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
    return jsonify({'success':"got products"})
    #     return jsonify({'success':"that exists"})
    # else:
    #     return jsonify({'error message':"collection doesn't exist"})
        


@app.route("/api/add", methods=['POST'])
def add():
    data = {
        'name':''.join(random.choices(string.ascii_lowercase, k=15)),
        'other':''.join(random.choices(string.ascii_lowercase, k=15))
    }
    doc_ref = db.collection('items').document()
    doc_ref.set(data)

    return jsonify({'success':"you did it"})

if __name__ == "__main__":
    app.run(debug=True, port=8080)