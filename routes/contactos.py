from flask import Blueprint, render_template, request, redirect, flash
from models.contacto import Contacto
from utils.db import db

contactos = Blueprint('contactos', __name__)

@contactos.route('/')
def index():
    contactos = Contacto.query.all()
    return render_template('index.html', contactos=contactos)

@contactos.route('/new', methods=['POST'])
def create():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']

    nuevoContacto = Contacto(nombre, email, telefono)

    db.session.add(nuevoContacto)
    db.session.commit()

    flash('Contacto creado correctamente')
    return redirect('/')

@contactos.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    contacto = Contacto.query.get(id)
    if request.method == 'POST':
        contacto.nombre = request.form['nombre']
        contacto.email = request.form['email']
        contacto.telefono = request.form['telefono']

        db.session.commit()
        flash('Contacto actualizado correctamente')

        return redirect('/')

    return render_template('update.html', contacto=contacto)

@contactos.route('/delete/<id>')
def delete(id):
    contact = Contacto.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contacto eliminado correctamente')
    return redirect('/')

