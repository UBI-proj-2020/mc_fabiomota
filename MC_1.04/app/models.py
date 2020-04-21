from datetime import datetime
from app import db

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    data_nascimento = db.Column(db.String(50))
    nacionalidade = db.Column(db.String(50))
    equipa = db.Column(db.Integer, db.ForeignKey('equipa.id'))

    def __repr__(self):
        return '<Jogador {}>'.format(self.id)

class Equipa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    modalidade = db.Column(db.String(50))
    local = db.Column(db.String(50))

    def __repr__(self):
        return '<Equipa {}>'.format(self.id)

class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipa_casa = db.Column(db.Integer, db.ForeignKey('equipa.id'))
    equipa_fora = db.Column(db.Integer, db.ForeignKey('equipa.id'))
    data = db.Column(db.String(50))
    hora = db.Column(db.String(50))
    local = db.Column(db.String(50))
    competicao = db.Column(db.Integer, db.ForeignKey('equipa.id'))
    
    def __repr__(self):
        return '<Jogo {}>'.format(self.id)

class Competicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    def __repr__(self):
        return '<Competicao {}>'.format(self.id)