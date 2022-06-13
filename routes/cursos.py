from flask import Blueprint, render_template, request, redirect, flash
from models.curso import Curso
from utils.db import db

cursos = Blueprint('cursos', __name__)

@cursos.route('/indexcursos')
def index():
    cursos = Curso.query.all()
    return render_template('indexcursos.html', cursos=cursos)

@cursos.route('/newcurso', methods=['POST'])
def createcurso():
    clase = request.form['clase']
    dia = request.form['dia']

    nuevoCurso = Curso(clase, dia)

    db.session.add(nuevoCurso)
    db.session.commit()

    flash('Curso creado correctamente')
    return redirect('/indexcursos')

@cursos.route('/deletecurso/<id>')
def deletecurso(id):
    curso = Curso.query.get(id)
    db.session.delete(curso)
    db.session.commit()
    flash('Curso eliminado correctamente')
    return redirect('/indexcursos')    

@cursos.route('/updatecurso/<id>', methods=['POST', 'GET'])
def updatecurso(id):
    curso = Curso.query.get(id)
    if request.method == 'POST':
        curso.clase = request.form['clase']
        curso.dia = request.form['dia']

        db.session.commit()
        flash('Curso actualizado correctamente')

        return redirect('/indexcursos')

    return render_template('updatecurso.html', curso=curso)