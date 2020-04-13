from app import db
from app.models import Jogador, Equipa, Jogo, Competicao

jogador = Jogador.query.all()
equipa = Equipa.query.all()
jogo = Jogo.query.all()
competicao = Competicao.query.all()


#JOGADOR
for x in competicao:
     print('ID: ', x.id, ' // NOME: ', x.nome)

#print(jogador)
#print(equipa)
#print(jogo)
#print(competicao)
