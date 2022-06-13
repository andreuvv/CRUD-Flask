from utils.db import db

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clase = db.Column(db.String(100))
    dia = db.Column(db.String(100))

    def __init__(self, clase, dia):
        self.clase = clase
        self.dia = dia