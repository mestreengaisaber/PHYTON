#conexion a firebase

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Read a document from Firestore
def read_document(collection, document_id):
    db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    document = doc_ref.get()
    if document.exists:
        print("Document data:", document.to_dict())
    else:
        print("No such document!")


# Usage example
read_document("comida", "14IPZv9PWfG7iqOx5NAb")



"""def create_document(collection, document_d
    db = firestore.client()
    doc_ref = db.collection(collection).document()
    doc_ref.set(document_data)
    print("Document created with ID:", doc_ref.id)
"""