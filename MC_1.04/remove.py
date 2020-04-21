from app import db
from app.models import Jogador, Equipa, Jogo, Competicao
import time

jogador = Jogador.query.all()
equipa = Equipa.query.all()
jogo = Jogo.query.all()
competicao = Competicao.query.all()




for e in equipa:
    db.session.delete(e)
    db.session.commit()

"""
for x in jogo:
    print('ID: ', x.id, ' // EQUIPA_CASA: ', x.equipa_casa, 
    ' // EQUIPA_FORA: ', x.equipa_fora, ' // LOCAL: ', x.local, 
    ' // HORA ', x.hora, ' // DATA ', x.data)
"""