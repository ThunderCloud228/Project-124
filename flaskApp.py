from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [
    {
        'id': 1,
        'name': u'Joe',
        'contact': u'7293647534',
        'done': False
    },
    {
        'id': 2,
        'name': u'Ligma',
        'contact': u'8923845735',
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])

def add_contact():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data!"
        }, 400)

    contact = {
        'id': contacts[-1]['id']+1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }

    contact.append(contact)
    return jsonify({
        "status": "success",
        "message": "Contact added successfully"
    })

@app.route("/get-data")

def get_contact():
    return jsonify({
        "data": contacts
    })

if (__name__ == "__main__"):
    app.run(debug=True)

