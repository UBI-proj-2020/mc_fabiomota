from app import db
from app.models import Jogador, Equipa, Jogo, Competicao
import time

jogador = Jogador.query.all()
equipa = Equipa.query.all()
jogo = Jogo.query.all()
competicao = Competicao.query.all()


#JOGADOR
"""
for x in competicao:
     print('ID: ', x.id, ' // NOME: ', x.nome)
"""

#EQUIPA
"""
for e in equipa:
     print('ID: ', e.id, '// NOME: ', e.nome, '// LOCAL: ', e.local)
"""

#print(jogador)
#print(equipa)
#print(jogo)
#print(competicao)

"""
c = Competicao(id=1, nome='Placard')
db.session.add(c)
db.session.commit()

c = Competicao(id=2, nome='TaçaPlacard')
db.session.add(c)
db.session.commit()
"""


"""
c = Competicao.query.get(1)
db.session.delete(c)
db.session.commit()
"""
"""
for x in jogo:
     print('ID: ', x.id, ' // EQUIPA_CASA: ', x.equipa_casa, 
     ' // EQUIPA_FORA: ', x.equipa_fora, ' // LOCAL: ', x.local, 
     ' // HORA ', x.hora, ' // DATA ', x.data, '// COMPETIÇÃO ', x.competicao)
"""

c = db.engine.execute('select id from competicao')
for i in c:
     i