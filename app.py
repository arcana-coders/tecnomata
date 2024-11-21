from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_email
import os

app = Flask(__name__)

# base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_method = db.Column(db.String(50), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    selected_pack = db.Column(db.String(50), nullable=True)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cases")
def cases():
    return render_template('cases.html')

@app.route("/contacto")
def contacto():
    return render_template("contact.html")

@app.route("/send_form", methods=["POST"])
def send_form():
    name = request.form.get("name")
    contact_method = request.form.get("contactMethod")
    contact_info = request.form.get("phone")
    selected_pack = request.form.get("selectedPack")

    if not name or not contact_method or not contact_info:
        return jsonify({"error": "Por favor, completa todos los campos"}), 400
    
    new_contact = Contact(
        name=name,
        contact_method=contact_method,
        contact_info=contact_info,
        selected_pack=selected_pack,
    )
    db.session.add(new_contact)
    db.session.commit()

    send_email(name, contact_method, contact_info, selected_pack)
    return redirect(url_for("gracias"))

@app.route("/gracias")
def gracias():
    return render_template("thankyou.html")

@app.route("/busca")
def busca():
    return render_template("busca.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))